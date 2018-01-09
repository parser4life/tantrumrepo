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
#Import Modules Section
import xbmc,xbmcplugin,xbmcaddon,xbmcgui,sys,os,re,urllib,urllib2,xbmcvfs
#######################################################################

#######################################################################
# Adds a top level style menu item, built from menu files
def addMenuFolder(name, url, mode, iconimage, fanart, description=''):
        u=sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo(type="Video", infoLabels={"Title": name, "Plot": description})
        liz.setProperty('fanart_image', fanart)
        ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
#######################################################################

#######################################################################
# Adds a clickable menu item for direct play
def addMenuItem(name, url, mode, iconimage, fanart, description=''):
        u=sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo(type="Video", infoLabels={"Title": name, "Plot": description})
        liz.setProperty('fanart_image', fanart)
        ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
#######################################################################

#######################################################################
# Adds a section/info line placeholder item to the menu
def addSectionItem(name, iconimage, fanart):
        u=sys.argv[0]+"?url=sectionItem&mode=100&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
#######################################################################

#######################################################################
# Adds a Search Term to the menu from a menu file
def addYTSearchItem(name, search_id, iconimage, fanart):
    work_url = "plugin://plugin.video.youtube/kodion/search/query/?q="+search_id+"/"
    ok=True
    liz=xbmcgui.ListItem(name)
    liz.setInfo( type="Video", infoLabels={ "Title": name })
    liz.setArt({ 'thumb': iconimage, 'fanart': fanart })
    liz.setPath(work_url)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=work_url,listitem=liz,isFolder=True)
    return ok
#######################################################################

#######################################################################
# Adds a Channel to the menu from a menu file
def addYTChannelItem(name, channel_id, iconimage, fanart):
    work_url = "plugin://plugin.video.youtube/channel/"+channel_id+"/"
    ok=True
    liz=xbmcgui.ListItem(name)
    liz.setInfo( type="Video", infoLabels={ "Title": name })
    liz.setArt({ 'thumb': iconimage, 'fanart': fanart })
    liz.setPath(work_url)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=work_url,listitem=liz,isFolder=True)
    return ok
#######################################################################

#######################################################################
# Adds a Playlist to the menu from a menu file
def addYTPlaylistItem(name, playlist_id, iconimage, fanart):
    work_url = "plugin://plugin.video.youtube/playlist/"+playlist_id+"/"
    ok=True
    liz=xbmcgui.ListItem(name)
    liz.setInfo( type="Video", infoLabels={ "Title": name })
    liz.setArt({ 'thumb': iconimage, 'fanart': fanart })
    liz.setPath(work_url)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=work_url,listitem=liz,isFolder=True)
    return ok
#######################################################################

#######################################################################
# Adds a video to the menu, populated by selecting a Playlist from a Menu
def addYTVideoItem(name, video_id, iconimage, fanart):
    work_url = "plugin://plugin.video.youtube/play/?video_id="+video_id
    ok=True
    liz=xbmcgui.ListItem(name)
    liz.setInfo( type="Video", infoLabels={ "Title": name })
    liz.setArt({ 'thumb': iconimage, 'fanart': fanart })
    liz.setPath(work_url)
    liz.setProperty('IsPlayable', 'true')
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=work_url,listitem=liz,isFolder=False)
    return ok
#######################################################################

#######################################################################
# Adds a folder to the directory for containing stream items - Part of original code
def addStreamFolder(title, url, iconImg="DefaultVideo.png", home="", away="", mode=""):
    sys_url = sys.argv[0] + '?url=' + urllib.quote_plus(url) + '&home=' + urllib.quote_plus(str(home)) +'&away=' + urllib.quote_plus(str(away)) +'&mode=' + urllib.quote_plus(str(mode))
    item = xbmcgui.ListItem(title, iconImage=iconImg, thumbnailImage=iconImg)
    item.setInfo(type='Video', infoLabels={'Title': title})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys_url, listitem=item, isFolder=True)
#######################################################################

#######################################################################
# Adds a folder to the directory for containing Reddit items - Part of original code
def addRedditFolder(title, url, next_url, iconImg="DefaultVideo.png", popup=None, mode=""):
    sys_url = sys.argv[0] + '?url=' + urllib.quote_plus(url)+'&next_url=' + urllib.quote_plus(next_url) +'&mode=' + urllib.quote_plus(str(mode))
    item = xbmcgui.ListItem(title, iconImage=iconImg, thumbnailImage=iconImg)
    item.setInfo(type='Video', infoLabels={'Title': title})
    if popup:
        item.addContextMenuItems(popup, True)
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys_url, listitem=item, isFolder=True)
#######################################################################

#######################################################################
# Adds a Playable Link to the directory - Part of original code
def addLink(title, orig_title, url, iconImg="DefaultVideo.png", mode=""):
    sys_url = sys.argv[0] + '?url=' + urllib.quote_plus(url) + '&mode=' + urllib.quote_plus(str(mode))+ '&orig=' + urllib.quote_plus(str(orig_title))
    item = xbmcgui.ListItem(title, iconImage=iconImg, thumbnailImage=iconImg)
    item.setLabel(title)
    item.setInfo(type='Video', infoLabels={'Title': title})
    item.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys_url, listitem=item)
#######################################################################

#######################################################################
# Adds a Direct Playable Link to the directory - Part of original code
def addDirectLink(title, infoLabels, url, iconImg="DefaultVideo.png"):
    item = xbmcgui.ListItem(title, iconImage=iconImg, thumbnailImage=iconImg)
    item.setInfo(type='Video', infoLabels=infoLabels)
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=item)
#######################################################################

#######################################################################
# Old addDir from default.py. Added here for while code is ported over to new methods.
def oldAddDir(title, url, iconImg="DefaultVideo.png", home="", away="", mode=""):
    sys_url = sys.argv[0] + '?url=' + urllib.quote_plus(url) + '&home=' + urllib.quote_plus(str(home)) +'&away=' + urllib.quote_plus(str(away)) +'&mode=' + urllib.quote_plus(str(mode))
    item = xbmcgui.ListItem(title, iconImage=iconImg, thumbnailImage=iconImg)
    item.setInfo(type='Video', infoLabels={'Title': title})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys_url, listitem=item, isFolder=True)
#######################################################################