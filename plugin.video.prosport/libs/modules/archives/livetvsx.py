#######################################################################
 # ----------------------------------------------------------------------------
 # "THE BEER-WARE LICENSE" (Revision 42):
 # @tantrumdev wrote this file.  As long as you retain this notice you
 # can do whatever you want with this stuff. If we meet some day, and you think
 # this stuff is worth it, you can buy me a beer in return. - Muad'Dib
 # ----------------------------------------------------------------------------
#######################################################################

# Addon Name: Sports Hub
# Addon id: plugin.video.prosport
# Addon Provider: MuadDib

#######################################################################
# Import Modules Section
from datetime import date, datetime, timedelta
import sys
import re
import urllib
import urlparse
import xbmc, xbmcgui, xbmcplugin
import CommonFunctions
try:
    import json
except:
    import simplejson as json

from urlresolver.hmf import HostedMediaFile
from libs.modules.globals import *
from libs.modules.log import log_utils
from libs.modules.menu import basemenu
from libs.modules.common import url_utils
#######################################################################

common = CommonFunctions

#######################################################################
# URLs for LiveTV.SX
livetv_base = 'http://livetv.sx'
livetv_nba = 'http://livetv.sx/enx/videotourney/3'
livetv_nhl = 'http://livetv.sx/enx/videotourney/2'
livetv_nfl = 'http://livetv.sx/enx/videotourney/142/'
#######################################################################

def get_list(base):
    list = []
    for i in range(0, 12):
        year = (datetime.utcnow() - timedelta(days = i*30)).strftime("%Y")
        month = (datetime.utcnow() - timedelta(days = i*30)).strftime("%m")
        monthDict = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12' : 'December'}

        name = '%s %s' % (monthDict[month], year)
        if any(name == i['name'] for i in list): continue
        name = name.encode('utf-8')

        url = '%s/%s%s/' % (base, year, month)
        url = url.encode('utf-8')
        list.append({'name': name, 'url': url})
        log_utils.log('LiveTV.SX: get_list - Append To List - Name: ' + str(name) + ' / URL: ' + url)
    return list

def list_season(seasonList):
    if seasonList == None or len(seasonList) == 0: return
    
    total = len(seasonList)
    log_utils.log('LiveTV.SX: list_season - Count: ' + str(total))
    for i in seasonList:
        try:
            try: name = i['name'].encode("utf-8")
            except: name = i['name']
            log_utils.log('LiveTV.SX: list_season - Name: ' + str(name))
            image = i['image']
            log_utils.log('LiveTV.SX: list_season - Icon: ' + str(image))
            root = i['mode']
            u = '%s?mode=%s' % (sys.argv[0], root)
            try: u += '&url=%s' % urllib.quote_plus(i['url'])
            except: pass
            if u == '': raise Exception()

            cm = []

            item = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=image)
            item.setInfo(type="Video", infoLabels={"title": name, "plot": THISADDONNAME})
            item.setProperty("Fanart_Image", 'http://')
            item.addContextMenuItems(cm, replaceItems=False)
            xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item,totalItems=total,isFolder=True)
        except:
            pass

    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True)

def get_season(mode):
    url = livetv_base
    iconImage = 'http://'
    if mode == 'nhltvrex':
        url = livetv_nhl
        iconImage = LOGO_ARCHIVE['nhl']
    elif mode == 'nbatvrex':
        url = livetv_nba
        iconImage = LOGO_ARCHIVE['nba']
    elif mode == 'nfltvrex':
        url = livetv_nfl
        iconImage = LOGO_ARCHIVE['nfl']
    log_utils.log('LiveTV.SX: get_season - Mode: ' + str(mode) + ' / URL: ' + url)

    list = get_list(url)
    log_utils.log('LiveTV.SX: get_season - List Count: ' + str(len(list)))
    for i in range(0, len(list)): list[i].update({'image': iconImage, 'mode': 'livetvsxarchive'})
    list_season(list)

def get_games(url):
    log_utils.log('LiveTV.SX: get_games - URL: ' + str(url))
    try:
        result = url_utils.GetURL(url)
        result = result.decode('iso-8859-1').encode('utf-8')
        result = result.replace('\n','')
        videos = common.parseDOM(result, "table", attrs = { "height": "27" })
    except:
        log_utils.log('LiveTV.SX: get_games - GetURL Exception')
        return

    videoList = []
    log_utils.log('LiveTV.SX: get_games - Videos Count: ' + str(len(videos)))
    for video in videos:
        try:
            title = re.compile('<b>(.+?)</b>').findall(video)
            title = [i for i in title if '&ndash;' in i or '-' in i][-1]
            title = title.split('<b>')[-1]
            title = title.replace('&ndash;', '-')
            title = common.replaceHTMLCodes(title)
            title = title.encode('utf-8')
            log_utils.log('LiveTV.SX: get_games - Title: ' + str(title))

            dateDict = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06', 'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December' : '12'}

            try:
                date = common.parseDOM(video, "span", attrs = { "class": "date" })[0]
                date = re.findall('(\d+)[.](\d+)[.](\d+)', date, re.I)[0]
                date = '%s-%s-%s' % ('20' + '%02d' % int(date[2]), '%02d' % int(date[1]), '%02d' % int(date[0]))
                log_utils.log('LiveTV.SX: get_games - Date: ' + str(date))
            except:
                year = common.parseDOM(result, "a", attrs = { "class": "mwhite" })
                year = [i for i in year if i.isdigit()][0]
                date = result.split(video.encode('utf-8'))[0]
                date = date.split('#2862a8')[-1]
                date = re.compile('<b>(\d+?)\s(.+?),\s.+?</b>').findall(date)[0]
                date = '%s-%s-%s' % (year, dateDict[date[1]], '%02d' % int(date[0]))
                log_utils.log('LiveTV.SX: get_games - Date Exception: ' + str(date))
            
            name = '[COLOR=yellow]%s[/COLOR] %s' % (date, title)
            name = common.replaceHTMLCodes(name)
            name = name.encode('utf-8')
            log_utils.log('LiveTV.SX: get_games - Name: ' + str(name))

            u = [('Full match record', ''), ('First Half', ' (1)'), ('Second Half', ' (2)'), ('First Period', ' (1)'), ('Second Period', ' (2)'), ('Third Period', ' (3)'), ('Fourth Period', ' (4)'), ('First Part', ' (1)'), ('Second Part', ' (2)'), ('Third Part', ' (3)'), ('Fourth Part', ' (4)')]
            uDict, uList = dict(u), [i[0] for i in u]
            u = re.compile('href="(.+?)">(.+?)<').findall(video)
            u = [i for i in u if i[1] in uList]
            u.sort(key=lambda x: uList.index(x[1]))
            url =  livetv_base + u[0][0]
            if len(url) == 0: raise Exception()
            type = 'games'

            url = url.encode('utf-8')
            log_utils.log('LiveTV.SX: get_games - url: ' + str(url))

            videoList.append({'name': name, 'url': url, 'date': date, 'genre': 'Sports', 'title': title, 'type': type})
        except:
            log_utils.log('LiveTV.SX: get_games - Videos Loop Exception')
            pass
    
    try:
        videoList = [i for n,i in enumerate(videoList) if i not in videoList[:n]]
        videoList = sorted(videoList, key=itemgetter('date'))
        videoList = videoList[::-1]
    except:
        pass

    if videoList == None or len(videoList) == 0: return

    total = len(videoList)
    log_utils.log('LiveTV.SX: get_games - videoList Count: ' + str(total))
    basemenu.addSectionItem('[COLOR=limegreen]Streams May Require Pairing[/COLOR]', '', '')
    for i in videoList:
        try:
            basemenu.addLink(i['name'], i['name'], i['url'], mode="play")
        except:
            pass

    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True)

def resolve(url):
    try:
        result = url_utils.GetURL(url)
        result = result.replace('\n','')
        result = re.sub(r'<script.+?</script>', '', result, flags=re.DOTALL)
        
        try:
            url = re.search("data-config\s*=\s*(?:\'|\")(.+?)(?:\'|\")", result).groups()[0]
        except:    
            url = common.parseDOM(result, "iframe", ret="src")[0]
            
        if '=http' in url: url = re.search("=(https?://.+)", url).groups()[0]
        elif url.startswith("//"): url = 'http:%s' % url
        
        if 'video.nhl.com' in url: url = resolve_nhl(url)
        else: url = HostedMediaFile(url=url).resolve()
        return url
    except:
        return

def resolve_nhl(url):
    try:
        url = url.split("playlist=")[-1]
        url = 'http://video.nhl.com/videocenter/servlets/playlist?ids=%s&format=json' % url
        result = url_utils.GetURL(url)
        url = re.compile('"publishPoint":"(.+?)"').findall(result)[0]
        return url
    except:
        return