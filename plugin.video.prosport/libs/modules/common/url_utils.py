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
import json
import urllib, urllib2
import urlparse
import xbmcgui, xbmcplugin

from libs.modules.globals import * 
from libs.modules.log import log_utils
#######################################################################

UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'

def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

def GetURL(url, referer=None, output=None, timeout=None, headers=None):
    if 'streamm.eu' in url:
        import cfscrape
        scraper = cfscrape.create_scraper()
        if headers:
            return scraper.get(url, headers=headers).content
        else: return scraper.get(url).content
    url = url.replace('///','//')
    request = urllib2.Request(url)
    request.add_header('User-agent', UA)
    if referer:
        request.add_header('Referer', referer)
    try:
        if timeout:
            response = urllib2.urlopen(request, timeout=int(timeout))
        else:
            response = urllib2.urlopen(request, timeout=20)
        if output == 'geturl':
            return response.geturl()
        if output == 'cookie':
            return response.info()['Set-Cookie']
        html = response.read()
        return html
    except:
        if 'reddit' in url:
            xbmcgui.Dialog().ok(THISADDONNAME, 'Looks like '+url+' is down... Please try later...')
        return None


def getUrl(url,data=None,header={},cookies=None):
    if not header:
        header = {'User-Agent':UA}
    req = urllib2.Request(url,data,headers=header)
    response = urllib2.urlopen(req, timeout=15)
    if cookies=='':
        cookies=response.info()['Set-Cookie']
    link = response.read()
    response.close()
    return link


def GetJSON(url, referer=None):
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:36.0) Gecko/20100101 Firefox/36.0')
    if referer:
        request.add_header('Referer', referer)
    try:
        response = urllib2.urlopen(request, timeout=5)
        f = response.read()
        jsonDict = json.loads(f)
        return jsonDict
    except:
        xbmcgui.Dialog().ok(THISADDONNAME, 'Looks like '+url+' is down... Please try later...')
        return None
