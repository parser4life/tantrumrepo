#######################################################################
 # ----------------------------------------------------------------------------
 # "THE BEER-WARE LICENSE" (Revision 42):
 # @tantrumdev wrote this file.  As long as you retain this notice you
 # can do whatever you want with this stuff. If we meet some day, and you think
 # this stuff is worth it, you can buy me a beer in return. - Muad'Dib
 # ----------------------------------------------------------------------------
#######################################################################

#######################################################################
#Import Modules Section
import xbmcplugin, xbmcaddon
import sys
import urllib
import re
import base_info
import glo_var
global parse

###################################################################################
#Main Menu
def MainMenu():
    if ('android' in base_info.platform()) or (glo_var.DEVELOPER == True):
        base_info.addDir2('[COLOR springgreen]News and Updates[/COLOR]','http://','news',glo_var.ICON,glo_var.ART,'')
        base_info.addDir2('','url','',glo_var.ICON,glo_var.ART,'')
        base_info.addDir('Emulator Menu','url','emu_menu',glo_var.ICON,glo_var.ART,'')
        base_info.addDir('Kodi Menu','url','kodi_menu',glo_var.ICON,glo_var.ART,'')
        base_info.addDir('Live TV Menu','url','livetv_menu',glo_var.ICON,glo_var.ART,'')
        base_info.addDir('Movie and TV Show Menu','url','vod_menu',glo_var.ICON,glo_var.ART,'')
        base_info.addDir('Music Menu','url','music_menu',glo_var.ICON,glo_var.ART,'')
        base_info.addDir('Security Menu','url','security_menu',glo_var.ICON,glo_var.ART,'')
        base_info.addDir('Sports Menu','url','sports_menu',glo_var.ICON,glo_var.ART,'')
        base_info.addDir('Tools Menu','url','tools_menu',glo_var.ICON,glo_var.ART,'')
    else:
        base_info.addDir2('[COLOR red][B]This Add-on is made for Android Devices[/B][/COLOR]', 'http://', 'mainmenu', glo_var.ICON, glo_var.ART, '')
    xbmc.executebuiltin('Container.SetViewMode(50)')
###################################################################################

###################################################################################
#Emulators Menu
def Emulator_Menu():  
    base_info.addDir2('[COLOR dodgerblue]ROM Emulators APK Menu[/COLOR]', 'http://', 'section', glo_var.ICON, glo_var.ART, '')
    base_info.addDir2('[COLOR red]============================================[/COLOR]', 'http://', 'section', glo_var.ICON, glo_var.ART, '')
    base_info.addDir2(' ', 'http://', 'section', glo_var.ICON, glo_var.ART, '')
    link = base_info.OPEN_URL(glo_var.EMU_FILE).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?ersion="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,image,fanart,version,description in match:
        base_info.addDir2(name + ' v' + version, url, 'apkinstall', image, fanart, description)
        xbmc.executebuiltin('Container.SetViewMode(50)')

####################################################################################    

###################################################################################
#Kodi Menu
def Kodi_Menu():
    base_info.addDir2('[COLOR dodgerblue]Kodi APK Menu[/COLOR]', 'http://', 'section', glo_var.ICON, glo_var.ART, '')
    base_info.addDir2('[COLOR red]============================================[/COLOR]', 'http://', 'section', glo_var.ICON, glo_var.ART, '')
    base_info.addDir2(' ', 'http://', 'section', glo_var.ICON, glo_var.ART, '')
    link = base_info.OPEN_URL(glo_var.KODI_FILE).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?ersion="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,image,fanart,version,description in match:
        base_info.addDir2(name + ' v' + version, url, 'apkinstall', image, fanart, description)
        xbmc.executebuiltin('Container.SetViewMode(50)')
        
####################################################################################   

###################################################################################
#Backup Menu
def LiveTV_Menu():
    base_info.addDir2('[COLOR dodgerblue]Live TV Streaming APK Menu[/COLOR]', 'http://', 'section', glo_var.ICON, glo_var.ART, '')
    base_info.addDir2('[COLOR red]============================================[/COLOR]', 'http://', 'section', glo_var.ICON, glo_var.ART, '')
    base_info.addDir2(' ', 'http://', 'section', glo_var.ICON, glo_var.ART, '')
    link = base_info.OPEN_URL(glo_var.LIVETV_FILE).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?ersion="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,image,fanart,version,description in match:
        base_info.addDir2(name + ' v' + version, url, 'apkinstall', image, fanart, description)
        xbmc.executebuiltin('Container.SetViewMode(50)')
####################################################################################	
		
###################################################################################
#Movie and TV Show Menu
def VOD_Menu():
    base_info.addDir2('[COLOR dodgerblue]Movie and TV Show Streaming APK Menu[/COLOR]', 'http://', 'section', glo_var.ICON, glo_var.ART, '')
    base_info.addDir2('[COLOR red]============================================[/COLOR]', 'http://', 'section', glo_var.ICON, glo_var.ART, '')
    base_info.addDir2(' ', 'http://', 'section', glo_var.ICON, glo_var.ART, '')
    link = base_info.OPEN_URL(glo_var.VOD_FILE).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?ersion="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,image,fanart,version,description in match:
        base_info.addDir2(name + ' v' + version, url, 'apkinstall', image, fanart, description)
        xbmc.executebuiltin('Container.SetViewMode(50)')
####################################################################################    

###################################################################################
#Music Menu
def Music_Menu():  
    base_info.addDir2('[COLOR dodgerblue]Music APK Menu[/COLOR]', 'http://', 'section', glo_var.ICON, glo_var.ART, '')
    base_info.addDir2('[COLOR red]============================================[/COLOR]', 'http://', 'section', glo_var.ICON, glo_var.ART, '')
    base_info.addDir2(' ', 'http://', 'section', glo_var.ICON, glo_var.ART, '')
    link = base_info.OPEN_URL(glo_var.MUSIC_FILE).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?ersion="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,image,fanart,version,description in match:
        base_info.addDir2(name + ' v' + version, url, 'apkinstall', image, fanart, description)
        xbmc.executebuiltin('Container.SetViewMode(50)')

####################################################################################    

###################################################################################
#Security Menu
def Security_Menu():
    base_info.addDir2('[COLOR dodgerblue]VPN and Security APK Menu[/COLOR]', 'http://', 'section', glo_var.ICON, glo_var.ART, '')
    base_info.addDir2('[COLOR red]============================================[/COLOR]', 'http://', 'section', glo_var.ICON, glo_var.ART, '')
    base_info.addDir2(' ', 'http://', 'section', glo_var.ICON, glo_var.ART, '')
    link = base_info.OPEN_URL(glo_var.SECURITY_FILE).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?ersion="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,image,fanart,version,description in match:
        base_info.addDir2(name + ' v' + version, url, 'apkinstall', image, fanart, description)
        xbmc.executebuiltin('Container.SetViewMode(50)')
###################################################################################

###################################################################################
#Sports Menu
def Sports_Menu():  
    base_info.addDir2('[COLOR dodgerblue]Sports TV APK Menu[/COLOR]', 'http://', 'section', glo_var.ICON, glo_var.ART, '')
    base_info.addDir2('[COLOR red]============================================[/COLOR]', 'http://', 'section', glo_var.ICON, glo_var.ART, '')
    base_info.addDir2(' ', 'http://', 'section', glo_var.ICON, glo_var.ART, '')
    link = base_info.OPEN_URL(glo_var.SPORTS_FILE).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?ersion="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,image,fanart,version,description in match:
        base_info.addDir2(name + ' v' + version, url, 'apkinstall', image, fanart, description)
        xbmc.executebuiltin('Container.SetViewMode(50)')

####################################################################################    

###################################################################################
#Tools Menu
def Tools_Menu():
    base_info.addDir2('[COLOR dodgerblue]System Tools APK Menu[/COLOR]', 'http://', 'section', glo_var.ICON, glo_var.ART, '')
    base_info.addDir2('[COLOR red]============================================[/COLOR]', 'http://', 'section', glo_var.ICON, glo_var.ART, '')
    base_info.addDir2(' ', 'http://', 'section', glo_var.ICON, glo_var.ART, '')
    link = base_info.OPEN_URL(glo_var.TOOLS_FILE).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?ersion="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,image,fanart,version,description in match:
        base_info.addDir2(name + ' v' + version, url, 'apkinstall', image, fanart, description)
        xbmc.executebuiltin('Container.SetViewMode(50)')
###################################################################################

####################################################################################
#Define Paramaters
def get_params():
    param=[]
    paramstring=sys.argv[2]
    if len(paramstring)>=2:
        params=sys.argv[2]
        cleanedparams=params.replace('?','')
        if (params[len(params)-1]=='/'):
            params=params[0:len(params)-2]
        pairsofparams=cleanedparams.split('&')
        param={}
        for i in range(len(pairsofparams)):
            splitparams={}
            splitparams=pairsofparams[i].split('=')
            if (len(splitparams))==2:
                param[splitparams[0]]=splitparams[1]
        return param

params=get_params()
url         = None
name        = None
version     = None
mode        = None
iconimage   = None
fanart      = None
description = None
try:     mode=urllib.unquote_plus(params["mode"])
except:  pass
try:     name=urllib.unquote_plus(params["name"])
except:  pass
try:     name=urllib.unquote_plus(params["version"])
except:  pass
try:     url=urllib.unquote_plus(params["url"])
except:  pass
try:     iconimage=urllib.unquote_plus(params["iconimage"])
except:  pass
try:     fanart=urllib.unquote_plus(params["fanart"])
except:  pass
try:     description=urllib.unquote_plus(params["description"])
except:  pass

#######################################################################

#######################################################################
# Below we are creating the different modes
if mode==None               : MainMenu()
elif mode=='emu_menu'       : Emulator_Menu()
elif mode=='kodi_menu'      : Kodi_Menu()
elif mode=='livetv_menu'    : LiveTV_Menu()
elif mode=='news'           : base_info.Update_News()
elif mode=='vod_menu'       : VOD_Menu()
elif mode=='music_menu'     : Music_Menu()
elif mode=='security_menu'  : Security_Menu()
elif mode=='sports_menu'    : Sports_Menu()
elif mode=='tools_menu'     : Tools_Menu()
elif mode=='apkinstall'     : base_info.apkInstaller(name, url)
#######################################################################

#######################################################################
#End of Directory
xbmcplugin.endOfDirectory(int(sys.argv[1]))
#######################################################################