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
import xbmc
import xbmcaddon
#######################################################################

#######################################################################
# Addon Related Variables
ADDON      = xbmcaddon.Addon()
ADDONTITLE = ADDON.getAddonInfo('name')
DEBUGPREFIX= '[COLOR red][ ' + ADDONTITLE + ' DEBUG ] : [/COLOR]' # Using color coding, for color formatted log viewers like Assassin's Tools
DEBUG      = ADDON.getSetting('debug')
#######################################################################

#######################################################################
# Debug Related Variables
LOGDEBUG   = xbmc.LOGDEBUG
LOGERROR   = xbmc.LOGERROR
LOGFATAL   = xbmc.LOGFATAL
LOGINFO    = xbmc.LOGINFO
LOGNONE    = xbmc.LOGNONE
LOGNOTICE  = xbmc.LOGNOTICE
LOGSEVERE  = xbmc.LOGSEVERE
LOGWARNING = xbmc.LOGWARNING
#######################################################################

#######################################################################
# Primary Log Function
def log(msg, level=xbmc.LOGDEBUG):
    # override message level to force logging when addon logging turned on
    if DEBUG == 'true' and level == xbmc.LOGDEBUG:
        level = xbmc.LOGNOTICE
    
    try:
        if isinstance(msg, unicode):
            msg = '%s (ENCODED)' % (msg.encode('utf-8'))
        xbmc.log('%s: %s' % (DEBUGPREFIX, msg), level)
    except Exception as e:
        try: xbmc.log('Logging Failure: %s' % (e), level)
        except: pass  # just give up
#######################################################################