# -*- coding: UTF-8 -*-
#######################################################################
 # ----------------------------------------------------------------------------
 # "THE BEER-WARE LICENSE" (Revision 42):
 # @tantrumdev wrote this file.  As long as you retain this notice you
 # can do whatever you want with this stuff. If we meet some day, and you think
 # this stuff is worth it, you can buy me a beer in return. - Muad'Dib
 # ----------------------------------------------------------------------------
#######################################################################

# Addon Name: Placenta
# Addon id: plugin.video.placenta
# Addon Provider: MuadDib

import re,urllib,urlparse
import resolveurl as urlresolver

from resources.lib.modules import cleantitle
from resources.lib.modules import client

class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['coolmoviezone.info']
        self.base_link = 'http://coolmoviezone.info'
        self.search_link = '/index.php?s=%s'

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = urlparse.urljoin(self.base_link, self.search_link)
            url = url  % (title.replace(':', ' ').replace(' ', '+'))

            search_results = client.request(url)
            match = re.compile('<h1><a href="(.+?)" rel="bookmark">(.+?)</a></h1>',re.DOTALL).findall(search_results)
            for item_url,item_title in match:
                if cleantitle.get(title) in cleantitle.get(item_title):
                    if year in str(item_title):
                        return item_url
            return
        except:
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []
            if url == None: return sources
            html = client.request(url)
            Links = re.compile('<td align="center"><strong><a href="(.+?)"',re.DOTALL).findall(html)
            for link in Links:
                if 'openload' in link:
                    try:
                        get_res = client.request(link)
                        rez = re.compile('target="_blank">(.+?)</a></td>',re.DOTALL).findall(get_res)[0]
                        if 'High-Definition' in rez:
                            quality = 'HD'
                        elif '720p' in rez:
                            quality='720p'
                        else:
                            quality='DVD'
                    except: quality='DVD'
                    sources.append({'source': 'Openload', 'quality': quality, 'language': 'en', 'url': link, 'direct': False, 'debridonly': False})
                elif 'streamango' in link:
                    try:
                        get_res = client.request(link)
                        rez = re.compile('target="_blank">(.+?)</a></td>',re.DOTALL).findall(get_res)[0]
                        if 'High-Definition' in rez:
                            quality = 'HD'
                        elif '720' in rez:
                            quality='720p'
                        else:
                            quality='DVD'
                    except: quality='DVD'
                    sources.append({'source': 'Streamango', 'quality': quality, 'language': 'en', 'url': link, 'direct': False, 'debridonly': False})
                else:
                    if urlresolver.HostedMediaFile(link):
                        host = link.split('//')[1].replace('www.','')
                        host = host.split('/')[0].split('.')[0].title()
                        sources.append({'source': host, 'quality': 'DVD', 'language': 'en', 'url': link, 'direct': False, 'debridonly': False})
            return sources
        except:
            return sources

    def resolve(self, url):
        return url