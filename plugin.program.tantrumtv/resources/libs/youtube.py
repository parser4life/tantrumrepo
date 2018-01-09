#######################################################################
#Import Modules Section
import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,sys,xbmcvfs
import shutil
import glo_var
import time
from resources.libs import extract
#######################################################################

#######################################################################
# Primary Addon Variables
AddonID             = glo_var.AddonID
ADDONTITLE          = glo_var.ADDONTITLE
#######################################################################

#######################################################################
# Path Variables
YOUTUBEPATH         = glo_var.YOUTUBE
YOUTUBEDATAPATH     = glo_var.YOUTUBEDATA
#######################################################################

def YoutubeFix():

    ytDialog = xbmcgui.Dialog()
    if not os.path.exists(YOUTUBEPATH):
        ytDialog(ADDONTITLE,"[COLOR springgreen]The YouTube Addon is not installed. Canceling fix....[/COLOR]")
        quit()
    if os.path.exists(YOUTUBEDATAPATH):
        try:
            shutil.rmtree(YOUTUBEDATAPATH)
        except:
            ytDialog.ok(ADDONTITLE,"[COLOR red]There was an error removing the YouTube addon data folder[/COLOR]")
            quit()
    try:
        YOUTUBE_FOLDER = xbmc.translatePath('special://home/userdata/addon_data/plugin.video.youtube')
        os.makedirs(YOUTUBE_FOLDER)
        PATCH_FILE = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID, 'resources/files/youtube_settings.xml'))
        FILE_TO_PATCH = xbmc.translatePath('special://home/userdata/addon_data/plugin.video.youtube/settings.xml')
        shutil.copyfile(PATCH_FILE, FILE_TO_PATCH)
    except:
        ytDialog.ok(ADDONTITLE,"[COLOR red]There was an error patching the YouTube addon data settings[/COLOR]")
        quit()
    ytDialog.ok(ADDONTITLE,"[COLOR snow]The YouTube addon has been patched. Daily Limit error should be resolved.[/COLOR]")