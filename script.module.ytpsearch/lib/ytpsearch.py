import xbmc         
import xbmcaddon    
import xbmcplugin  
import json, math, urllib, urllib2, re, xbmcgui, datetime, os, sys
from youtube_plugin import *

YOUTUBE_API_KEY = "AIzaSyA4ktCh7tLBk467AYgPMykgdtMZ8HL68hE"
RESULTS_PER_PAGE = '40' # 1-50 as per Google's rules.

#######################################################################
# Builds the item for Kodi's Video information
def add_video_result(name,video_id,mode,iconimage,info,video_info,audio_info):
    work_url = "plugin://plugin.video.youtube/play/?video_id="+video_id
    ok=True
    liz=xbmcgui.ListItem(name)
    liz.setInfo( type="Video", infoLabels=info)
    liz.addStreamInfo('video', video_info)
    liz.addStreamInfo('audio', audio_info)
    liz.setArt({ 'thumb': iconimage })
    liz.setPath(work_url)
    liz.setProperty('IsPlayable', 'true')
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=work_url,listitem=liz,isFolder=False)
    return ok
#######################################################################

#######################################################################
# Adds a section/info line placeholder item to the menu
def add_dir_placeholder(name, iconimage, fanart):
    u=sys.argv[0]+"?url=sectionItem&mode=100&name="+urllib.quote_plus(name)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setProperty('fanart_image', fanart)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok
#######################################################################

#######################################################################
# Sets up the sorting for the results
def add_sort_methods():
    sort_methods = [xbmcplugin.SORT_METHOD_LABEL,xbmcplugin.SORT_METHOD_UNSORTED,xbmcplugin.SORT_METHOD_DATE,xbmcplugin.SORT_METHOD_DURATION,xbmcplugin.SORT_METHOD_EPISODE]
    for method in sort_methods:
        xbmcplugin.addSortMethod(int(sys.argv[1]), sortMethod=method)
    return
#######################################################################

#######################################################################
# Performs a recursive search of the playlists passed to it
def perform_search(search_term, playlists):
    base_plugin_url = 'plugin://plugin.video.youtube/play/?video_id='
    base_search_url = 'https://www.googleapis.com/youtube/v3/playlistItems?'

    first_url = base_search_url+'key={}&order=date&maxResults={}'.format(YOUTUBE_API_KEY, RESULTS_PER_PAGE)

    total_results = 0
    video_links = []
    cycle = 0
    url = first_url + '&playlistId='+playlists[cycle]+'&part=id,snippet,contentDetails'
    # Begin cycling through the list of videos, in each playlist - If a lot of videos, this could take a while
    while True:
        inp = urllib.urlopen(url)
        resp = json.load(inp)
        video_count = len(resp["items"])
        video_worked = 1;
        for video in resp['items']:
            title_temp = video["snippet"]["title"].lower()
            if title_temp.find(search_term.lower()) == -1:
                # first try/except checks for end of playlist items
                try:
                    # First, see if this is the last video in returned results
                    if video_worked == video_count:
                        next_page_token = resp['nextPageToken']
                        url = first_url + '&playlistId={}&part=id,snippet,contentDetails&pageToken={}'.format(playlists[cycle], next_page_token)
                        continue
                    # Not the last video, so just continue to next cycle as normal
                    video_worked = video_worked + 1
                    continue
                except:
                    # Something broke, most likely last video of last page, so go on to the next try/except to get next video and token
                    pass

                # This try/except checks for next Playlist in the cycle. If no more Playlists, break out
                try:
                    next_page_token = ''
                    cycle = cycle + 1
                    url = first_url + '&playlistId={}&part=id,snippet,contentDetails'.format(playlists[cycle])
                    continue
                except:
                    break

            title = video["snippet"]["title"]
            plot = video["snippet"]["description"]
            aired = video["snippet"]["publishedAt"]
            thumb = video["snippet"]["thumbnails"]["high"]["url"]
            videoid = video["snippet"]['resourceId']['videoId']
            try:
                duration_string = video["contentDetails"]["duration"]
                duration = return_duration_as_seconds(duration_string)
            except: duration = '0'
            try: 
                aired = re.compile('(.+?)-(.+?)-(.+?)T').findall(aired)[0]
                date = aired[2] + '.' + aired[1] + '.' + aired[0]
                aired = aired[0]+'-'+aired[1]+'-'+aired[2]
            except: 
                aired = ''
                date = ''
            try:
                if episode_playlists:
                    if url in episode_playlists:
                        episode = re.compile('(\d+)').findall(title)[0]
                    else: episode = ''
                else: episode = ''
            except: episode = ''
        
            infolabels = {'plot':plot.encode('utf-8'),'aired':aired,'date':date,'tvshowtitle':'','title':title.encode('utf-8'),'originaltitle':title.encode('utf-8'),'status':'','duration':duration,'episode':episode,'playcount':0}
            
            # Compile video and audio details
            video_info = { 'codec': 'avc1', 'aspect' : 1.78 }
            audio_info = { 'codec': 'aac', 'language' : 'en' }
            try:
                if video["contentDetails"]["definition"].lower() == 'hd':
                    video_info['width'] = 1280
                    video_info['height'] = 720
                    audio_info['channels'] = 2
                else:
                    video_info['width'] = 854
                    video_info['height'] = 480
                    audio_info['channels'] = 1
                try:
                    if xbmcaddon.Addon(id='plugin.video.youtube').getSetting('kodion.video.quality.ask') == 'false' and xbmcaddon.Addon(id='plugin.video.youtube').getSetting('kodion.video.quality') != '3' and xbmcaddon.Addon(id='plugin.video.youtube').getSetting('kodion.video.quality') != '4':
                        video_info['width'] = 854
                        video_info['height'] = 480
                        audio_info['channels'] = 1
                except: pass    
            except:
                video_info['width'] = 854
                video_info['height'] = 480
                audio_info['channels'] = 1      
            
            # Build and add video to collection
            add_video_result(title.encode('utf-8'),videoid,5,thumb,infolabels,video_info,audio_info)
            total_results = total_results + 1
            video_worked = video_worked + 1

        # first try/except checks for end of playlist items
        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&playlistId={}&part=id,snippet,contentDetails&pageToken={}'.format(playlists[cycle], next_page_token)
            continue
        except:
            pass
        
        # This try/except checks for next Playlist in the cycle. If no more Playlists, break out
        try:
            next_page_token = ''
            cycle = cycle + 1
            url = first_url + '&playlistId={}&part=id,snippet,contentDetails'.format(playlists[cycle])
        except:
            break

    # All videos in all lists are done, now finish this up and display the results
    if total_results > 0:
        add_sort_methods()
    xbmcplugin.setContent(int(sys.argv[1]), 'episodes')
    return
#######################################################################