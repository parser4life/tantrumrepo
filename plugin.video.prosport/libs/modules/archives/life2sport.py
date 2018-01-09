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
import datetime
import sys
import re
import urllib
import urlparse
import xbmc, xbmcgui, xbmcplugin
import CommonFunctions

from libs.modules.globals import *
from libs.modules.log import log_utils
from libs.modules.menu import basemenu
from libs.modules.common import url_utils
#######################################################################

common = CommonFunctions

NBAL2SWordList = ['-nba.','-nba-', 'boston-celtics', 'charlotte-hornets', 'chicago-bulls', 'cleveland-cavaliers', 'detroit-pistons', 'indiana-pacers', 
            'indiana-papcers', 'miami-heat', 'milwaukee-bucks', 'brooklyn-nets', 'new-york-knicks', 'orlando-magic', 'philadelphia-76ers', 'toronto-raptors', 
            'washington-wizards', 'denver-nuggets', 'golden-state-warriors', 'houston-rockets', 'los-angeles-clippers', 'los-angeles-lakers', 'memphis-grizzlies', 
            'minnesota-timberwolves', 'new-orleans-pelicans', 'oklahoma-city-thunder', 'phoenix-suns', 'portland-trail-blazers', 'sacramento-kings', 
            'san-antonio-spurs', 'utah-jazz' ]

def get_links(url):
    orig_title = xbmc.getInfoLabel('ListItem.Title')
    html = url_utils.GetURL(url)
    html = html.split('>ENGLISH<')[-1]
    links = common.parseDOM(html, "iframe", ret="src")
    lnks = common.parseDOM(html, "a", ret="href")
    links = links+lnks
    for i, link in enumerate(links):
        if 'mail.ru/vid' in link:
            link = link.replace('https://videoapi.my.mail.ru/videos/embed/mail/','https://my.mail.ru/+/video/meta/')
            link = link.replace('https://my.mail.ru/video/embed/','https://my.mail.ru/+/video/meta/')
            link = link.replace('html','json')
            cookieJar = cookielib.CookieJar()
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar), urllib2.HTTPHandler())
            conn = urllib2.Request(link)
            connection = opener.open(conn)
            f = connection.read()
            connection.close()
            js = json.loads(f)
            for cookie in cookieJar:
                token = cookie.value
            js = js['videos']
            for el in js:
                basemenu.addDirectLink('mail.ru - '+el['key'], {'Title': orig_title}, 'https:'+el['url']+'|Cookie=video_key='+token)
        elif 'openload.co' in link:
            basemenu.addLink('openload', orig_title, link, mode="play")
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True)

def get_games(page, mode):
    if mode == 'nhllife2sport':
        url = 'http://www.life2sport.com/category/online-video/hockey/nhl/page/'+str(page)
    elif mode == 'nbalife2sport':
        url = 'http://www.life2sport.com/category/online-video/basketbol/nba/page/'+str(page)
    elif mode == 'nfllife2sport':
        url = 'http://www.life2sport.com/category/online-video/american-football/page/'+str(page)
    elif mode == 'mlblife2sport':
        url = 'http://www.life2sport.com/category/online-video/mlb/page/'+str(page)
    log_utils.log('Page: ' + str(page) + ' / Mode: ' + str(mode) + ' / URL: ' + url)
    html = url_utils.GetURL(url)
    links = common.parseDOM(html, "a", attrs={"rel": "bookmark"}, ret="href")
    if links:
        del links[1::2]
    for i, el in enumerate(links):
        log_utils.log('Link: ' + el)
#        try:
        found_match = False
        if mode == 'nbalife2sport':
            for word in NBAL2SWordList:
                if word in el:
                    found_match = True
        if '-nfl-' in el or '-nfl.' in el or '-nhl-' in el or '-nhl.' in el or '-mlb-' in el or found_match:
            title = common.parseDOM(html, "a", attrs={"href": el}, ret="title")[0]
            title = url_utils.strip_non_ascii(title)
            log_utils.log('Title Check: ' + title)
            title = title.replace('&#8211;','@').strip()
            titles = title.split('/')
            season = ''
            gameday = ''
            loop_check = 0
            for tit in titles:
                log_utils.log('Title Loop Check: ' + tit)
                if len(tit)>25:
                    title = tit
                if mode == 'nhllife2sport':
                    if loop_check == 2:
                        log_utils.log('Season Loop Check: ' + tit.strip())
                        season = '[COLOR yellow]' + tit.strip() + '[/COLOR]'
                    elif loop_check == 3:
                        log_utils.log('Gameday Loop Check: ' + tit.strip())
                        tit = tit[:-4]
                        gameday = '[COLOR yellow]' + tit.strip() + '[/COLOR] '
                elif mode == 'nfllife2sport':
                    if loop_check == 2:
                        log_utils.log('Season Loop Check: ' + tit.strip())
                        season = '[COLOR yellow]' + tit.strip() + '[/COLOR]'
                    elif loop_check == 3:
                        log_utils.log('Gameday Loop Check: ' + tit.strip())
                        gameday = '[COLOR yellow]' + tit.strip() + '[/COLOR] '
                elif mode == 'nbalife2sport':
                    if loop_check == 2:
                        log_utils.log('Season Loop Check: ' + tit.strip())
                        season = '[COLOR yellow]' + tit.strip() + '[/COLOR]'
                    elif loop_check == 4:
                        log_utils.log('Gameday Loop Check: ' + tit.strip())
                        gameday = '[COLOR yellow]' + tit.strip()[:10] + '[/COLOR] '
                elif mode == 'mlblife2sport':
                    if loop_check == 2:
                        log_utils.log('Season Loop Check: ' + tit.strip())
                        season = '[COLOR yellow]' + tit.strip() + '[/COLOR]'
                    elif loop_check == 3:
                        log_utils.log('Game or Post Season Loop Check: ' + tit.strip())
                        if 'game' in tit.strip().lower():
                            season = season + '[COLOR green] ' + tit.strip() + '[/COLOR]'
                    elif loop_check == 4:
                        log_utils.log('World Series or Date Loop Check: ' + tit.strip())
                        if 'series' in tit.strip().lower():
                            season = season + '[COLOR green] ' + tit.strip() + '[/COLOR]'
                        else:
                            gameday = '[COLOR yellow]' + tit.strip()[:10] + '[/COLOR] '
                    elif loop_check == 5:
                        log_utils.log('Game of World Series Loop Check: ' + tit.strip())
                        season = season + '[COLOR green] ' + tit.strip() + '[/COLOR]'
                    elif loop_check == 6:
                        log_utils.log('Gameday Loop Check: ' + tit.strip())
                        gameday = '[COLOR yellow]' + tit.strip()[:10] + '[/COLOR] '
                loop_check = loop_check +1
            title = gameday + title + season
            basemenu.addStreamFolder(title, el, iconImg=LOGOS[mode[0:3]], mode="playlife2sportarchive")
#        except:
#            log_utils.log('Exception with Link: ' + el)
#            pass
    uri = sys.argv[0] + '?mode=%s&page=%s' % (mode, str(int(page)+1))
    item = xbmcgui.ListItem("next page...", iconImage='', thumbnailImage='')
    xbmcplugin.addDirectoryItem(int(sys.argv[1]), uri, item, True)
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True)