#######################################################################
 # ----------------------------------------------------------------------------
 # "THE BEER-WARE LICENSE" (Revision 42):
 # @tantrumdev wrote this file.  As long as you retain this notice you
 # can do whatever you want with this stuff. If we meet some day, and you think
 # this stuff is worth it, you can buy me a beer in return. - Muad'Dib
 # ----------------------------------------------------------------------------
#######################################################################

#######################################################################
# Import Modules Section
import xbmc, xbmcaddon, xbmcgui, xbmcplugin, base64
import os
#######################################################################

#######################################################################
# Set this to True to see the menu on non-android devices for dev work
DEVELOPER           = False
#######################################################################

#######################################################################
# Primary Addon Variables
AddonID             = xbmcaddon.Addon().getAddonInfo('id')
ADDON               = xbmcaddon.Addon(id=AddonID)
HOME                = xbmc.translatePath('special://home/')
ADDONS              = os.path.join(HOME, 'addons')
USERDATA            = os.path.join(HOME, 'userdata')
ADDON_DATA          = xbmc.translatePath(os.path.join(USERDATA, 'addon_data'))
ownAddon            = xbmcaddon.Addon(id=AddonID)
URL                 = base64.b64decode(b'aHR0cDovL3JlcG8udGFudHJ1bXR2LmNvbS9hcGt3aXphcmQv')
NEWSURL             = base64.b64decode(b'aHR0cDovL3JlcG8udGFudHJ1bXR2LmNvbS9hcGt3aXphcmQvbmV3cy54bWw=')
ADDONTITLE          = base64.b64decode(b'W0NPTE9SIHNwcmluZ2dyZWVuXVtCXVRhbnRydW1bL0JdWy9DT0xPUl0gW0NPTE9SIHNub3ddQVBLIFdpemFyZFsvQ09MT1Jd')
#######################################################################

#######################################################################
# Filename Variables 
BASEURL             = URL
EMU_FILE            = BASEURL + base64.b64decode(b'ZW11bGF0b3JzLnR4dA==')
KODI_FILE           = BASEURL + base64.b64decode(b'a29kaS50eHQ=')
LIVETV_FILE         = BASEURL + base64.b64decode(b'bGl2ZXR2LnR4dA==')
VOD_FILE            = BASEURL + base64.b64decode(b'dm9kLnR4dA==')
MUSIC_FILE          = BASEURL + base64.b64decode(b'bXVzaWMudHh0')
SECURITY_FILE       = BASEURL + base64.b64decode(b'c2VjdXJpdHkudHh0')
SPORTS_FILE         = BASEURL + base64.b64decode(b'c3BvcnRzLnR4dA==')
TOOLS_FILE          = BASEURL + base64.b64decode(b'dG9vbHMudHh0')
#######################################################################

#######################################################################
# Theme Variables
FONTHEADER          = base64.b64decode(b'Rm9udDE0')
FANART              = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID, 'fanart.jpg'))
ICON                = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID, 'icon.png'))
ART                 = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID, 'resources/art/'))
#######################################################################

#######################################################################
ADDONDATA           = os.path.join(USERDATA, 'addon_data', AddonID)
dialog              = xbmcgui.Dialog()
DIALOG              = xbmcgui.Dialog()
dp                  = xbmcgui.DialogProgress()
DP                  = xbmcgui.DialogProgress()
LOG                 = xbmc.translatePath('special://logpath/')
PLUGIN              = os.path.join(ADDONS, AddonID)
skin                = xbmc.getSkinDir()
USER_AGENT          = base64.b64decode(b'TW96aWxsYS81LjAgKFdpbmRvd3M7IFU7IFdpbmRvd3MgTlQgNS4xOyBlbi1HQjsgcnY6MS45LjAuMykgR2Vja28vMjAwODA5MjQxNyBGaXJlZm94LzMuMC4z')
#######################################################################