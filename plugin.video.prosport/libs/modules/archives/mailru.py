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
import urllib, urllib2, urlparse, sys, cookielib, base64, re
import xbmc, xbmcgui, xbmcplugin
import CommonFunctions, cookielib
try:
    import json
except:
    import simplejson as json

from libs.modules.globals import *
from libs.modules.log import log_utils
from libs.modules.menu import basemenu
from libs.modules.common import url_utils
#######################################################################

common = CommonFunctions

def nhl_archive_ru(url, page, mode):
    page = int(page)-1
    link = 'https://my.mail.ru/cgi-bin/my/ajax?user=atl17@bk.ru&xemail=&ajax_call=1&func_name=video.get_list&mna=&mnb=&arg_type=album_items&arg_all=1&sort=default&arg_offset='+str(page)+'&arg_limit=20'
    json = url_utils.GetJSON(link)
    json = json[2]['items']
    for el in json:
        title = el['Title']
        videoUrl = el['MetaUrl']
        img = el['ImageUrlP']
        if 'NHL' in title:
            titlelist = list(title)
            if 'On the Fly' in title:
                titlelist.insert(22, '[/COLOR]')
            else:
                titlelist.insert(20, '[/COLOR]')
            titlelist.insert(11, '[COLOR yellow]')
            titlelist.insert(7, '[/COLOR]')
            titlelist.insert(0, '[COLOR yellow]')
            title = ''.join(titlelist)
            basemenu.oldAddDir(title, videoUrl, iconImg=img, mode="playnhlruarchive")
    uri = sys.argv[0] + '?mode=%s&page=%s&url=%s' % (mode, str(int(page)+10),url)
    item = xbmcgui.ListItem("next page...", iconImage='', thumbnailImage='')
    xbmcplugin.addDirectoryItem(int(sys.argv[1]), uri, item, True)
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True)

def play_nhl_archive_ru(url):
    orig_title = xbmc.getInfoLabel('ListItem.Title')
    cookieJar = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar), urllib2.HTTPHandler())
    conn = urllib2.Request(url)
    connection = opener.open(conn)
    f = connection.read()
    connection.close()
    js = json.loads(f)
    for cookie in cookieJar:
        token = cookie.value
    js = js['videos']
    for el in js:
        basemenu.addDirectLink('mail.ru - '+el['key'], {'Title': orig_title}, 'http:'+el['url']+'|Cookie=video_key='+token)
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True)
    