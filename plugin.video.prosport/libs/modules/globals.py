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
from datetime import datetime
import base64, os, urllib, urlparse
import xbmc, xbmcaddon
#######################################################################

THISADDON           = xbmcaddon.Addon('plugin.video.prosport')
THISADDONNAME       = THISADDON.getAddonInfo('name')
ADDON_ID            = xbmcaddon.Addon().getAddonInfo('id')
path                = THISADDON.getAddonInfo('path')
display_score       = THISADDON.getSetting('score')
display_status      = THISADDON.getSetting('status')
display_start_time  = THISADDON.getSetting('start_time')
display_pattern     = THISADDON.getSetting('pattern')
username            = THISADDON.getSetting('username')
password            = THISADDON.getSetting('password')
show_tor            = THISADDON.getSetting('show_tor')

#######################################################################
# Path Variables
HOMEPATH            = xbmc.translatePath('special://home/')
ADDONSPATH          = os.path.join(HOMEPATH, 'addons')
USERDATAPATH        = os.path.join(HOMEPATH, 'userdata')
ADDONDATAPATH       = xbmc.translatePath(os.path.join(USERDATAPATH, 'addon_data'))
PSADDONPATH         = os.path.join(ADDONSPATH, ADDON_ID)
PSDATAPATH          = os.path.join(ADDONDATAPATH, ADDON_ID)
#######################################################################

#######################################################################
# Filename Variables 
BASEURL             = base64.b64decode(b'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL211YWRkaWJ0dHYvbmVvc3BvcnQvbWFzdGVyLw==')
NEWSFILE            = BASEURL + base64.b64decode(b'bmV3cy54bWw=')
LOCALNEWS           = os.path.join(PSADDONPATH, base64.b64decode(b'd2hhdHNuZXcudHh0'))
#######################################################################

LOGOS = {'reddit':'https://raw.githubusercontent.com/muaddibttv/neosport/master/icons/reddit.png',
'nba':'https://raw.githubusercontent.com/muaddibttv/neosport/master/icons/nba.png',
'nbafan':'https://raw.githubusercontent.com/muaddibttv/neosport/master/fanart/nba.png',
'nhl':'https://raw.githubusercontent.com/muaddibttv/neosport/master/icons/nhl.png',
'nhlfan':'https://raw.githubusercontent.com/muaddibttv/neosport/master/fanart/nhl.png',
'nfl':'https://raw.githubusercontent.com/muaddibttv/neosport/master/icons/nfl.png',
'nflfan':'https://raw.githubusercontent.com/muaddibttv/neosport/master/fanart/nfl.png',
'mlb':'https://raw.githubusercontent.com/muaddibttv/neosport/master/icons/mlb.png',
'mlbfan':'https://raw.githubusercontent.com/muaddibttv/neosport/master/fanart/mlb.png',
'soccer':'https://raw.githubusercontent.com/muaddibttv/neosport/master/icons/soccer.png',
'soccerfan':'https://raw.githubusercontent.com/muaddibttv/neosport/master/fanart/soccer.png'}

LOGO_ARCHIVE ={'nba':'https://raw.githubusercontent.com/muaddibttv/neosport/master/icons/nbaarchive.png',
'nbafan':'https://raw.githubusercontent.com/muaddibttv/neosport/master/fanart/nbaarchive.png',
'nhl':'https://raw.githubusercontent.com/muaddibttv/neosport/master/icons/nhlarchive.png',
'nhlfan':'https://raw.githubusercontent.com/muaddibttv/neosport/master/fanart/nhlarchive.png',
'nfl':'https://raw.githubusercontent.com/muaddibttv/neosport/master/icons/nflarchive.png',
'nflfan':'https://raw.githubusercontent.com/muaddibttv/neosport/master/fanart/nflarchive.png',
'mlb':'https://raw.githubusercontent.com/muaddibttv/neosport/master/icons/mlbarchive.png',
'mlbfan':'https://raw.githubusercontent.com/muaddibttv/neosport/master/fanart/mlbarchive.png',
'soccer':'https://raw.githubusercontent.com/muaddibttv/neosport/master/icons/soccerarchive.png',
'soccerfan':'https://raw.githubusercontent.com/muaddibttv/neosport/master/fanart/soccerarchive.png'}

SD_STREAMS = ['giostreams.eu','watch-sportstv.boards.net', 'hdstream4u.com', 'stream24k.com', 'wizhdsports.com', 'antenasport.com', 
            'sportsnewsupdated.com', 'watchnba.tv', 'feedredsoccer.at.ua', 'jugandoes.com', 'wiz1.net', 'bosscast.net', 
            'watchsportstv.boards.net', 'tv-link.in', 'klivetv.co', 'videosport.me', 'livesoccerg.com', 'zunox.hk', 'singidunum.', 
            'zona4vip.com', 'ciscoweb.ml', 'streamendous.com','streamm.eu', 'sports-arena.net', 'stablelivestream.com', 
            'iguide.to', 'sportsleague.me','kostatz.com', 'soccerpluslive.com', 'zunox', 'apkfifa.com','watchhdsports.xyz','lovelysports2016.ml',
            'sports4u.live','tusalavip3.es.tl', 'neymargoals.com', 'crichd.sx', 'unitedstream.live','stream4us.info','freecast.xyz','focustream.info',
            's4power.club', 'footystreams.net', 'topstream.es.tl', 'pushmycar.cf','zifootball.us','hehestreams.xyz/nba/games',
            'bubbysports.ml', 'sportz-hd.com','immortal-tv.net','besasport.top', 'nbalivestreams.net','genti.stream', 'yaboy.xyz',
            'eplstreams.club', 'gentistream.com','streamtoday.us','yoursportsinhd.com','nbastream.pw', 'watchkobe.info', 'apkadsense.com',
            'sportshd.me', 'imabee.ca', 'pop-sports.ml', 'bilasport.pw', 'primealpha.ml' ]