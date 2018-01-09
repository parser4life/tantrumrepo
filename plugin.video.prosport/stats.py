# -*- coding: utf-8 -*-

"""
Copyright (C) 2017 podgod

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>
"""


import xbmcgui, xbmcplugin, urllib, urllib2, sys, re

def NFLSelect():
		dialog = xbmcgui.Dialog()
		ret = dialog.select('Standings', ['Division', 'Conference','League','Playoff','Leaders'])
		if ret == 0:
			URL = 'http://www.espn.com/nfl/standings'
			dialog = xbmcgui.Dialog(URL)
			NFLStandings(URL)
		if ret == 1:
			URL = 'http://www.espn.com/nfl/standings/_/group/conference'
			dialog = xbmcgui.Dialog(URL)
			NFLStandings(URL)
		if ret == 2:
			URL = 'http://www.espn.com/nfl/standings/_/group/league'
			dialog = xbmcgui.Dialog()
			NFLStandings(URL)
		if ret == 3:
			URL = 'http://www.espn.com/nfl/standings/_/view/playoff'
			dialog = xbmcgui.Dialog()
			NFLStandings(URL)
		if ret == 4:
			URL = 'http://www.espn.com/nfl/statistics/player/_/stat/points/sort/points/year/2017/seasontype/2'
			dialog = xbmcgui.Dialog()
			NFLStats(URL)
		  
		  
def NFLStandings(URL):
        league = 'nfl'
        logo='http://a.espncdn.com/combiner/i?img=/i/teamlogos/leagues/500/'+league+'.png'
        heading = 'DIVISION         W      L      OTL   PCT     TEAM'
        addDir('[B]'+heading+'[/B]','',iconImg=logo, fanart=logo, mode="")
        HTML = OPEN_URL(URL)
        match = re.compile('align="left">American Football Conferenc </td><td>((.|\n)*)class="colhead',re.MULTILINE).findall(HTML)
        string = str(match)
        match2 = re.compile('<abbr title="(.+?)">(.+?)</abbr></span></a></td><td style="white-space:no-wrap;" class="">(.+?)</td><td style="white-space:no-wrap;" class="">(.+?)</td><td style="white-space:no-wrap;" class="">(.+?)</td><td style="white-space:no-wrap;" class="">(.+?)</td><td',re.MULTILINE).findall(HTML)
        for name3,name2,W,L,T,PCT in match2:
                teamLogo='http://a.espncdn.com/combiner/i?img=/i/teamlogos/'+league+'/500/'+name2+'.png'
                AFC_EAST = ['New England Patriots','Buffalo Bills','Miami Dolphins','New York Jets']
                AFC_NORTH = ['Pittsburgh Steelers','Cincinnati Bengals','Baltimore Ravens','Cleveland Browns']
                AFC_SOUTH = ['Houston Texans','Tennessee Titans','Indianapolis Colts','Jacksonville Jaguars']
                AFC_WEST =['Oakland Raiders','Denver Broncos','Kansas City Chiefs','San Diego Chargers']
                NFC_EAST = ['Dallas Cowboys','New York Giants','Philadelphia Eagles','Washington Redskins']
                NFC_NORTH = ['Minnesota Vikings','Green Bay Packers','Detroit Lions','Chicago Bears']
                NFC_SOUTH = ['Atlanta Falcons','Tampa Bay Buccaneers','New Orleans Saints','Carolina Panthers']
                NFC_WEST =['Seattle Seahawks','Arizona Cardinals','Los Angeles Rams','San Francisco 49ers']
                if name3 in AFC_EAST:
                        Div = 'AFC EAST    '
                elif name3 in AFC_NORTH:
                        Div = 'AFC NORTH'
                elif name3 in AFC_SOUTH:
                        Div = 'AFC SOUTH '
                elif name3 in AFC_WEST:
                        Div = 'AFC WEST   '
                elif name3 in NFC_EAST:
                        Div = 'NFC EAST    '
                elif name3 in NFC_NORTH:
                        Div = 'NFC NORTH'
                elif name3 in NFC_SOUTH:
                        Div = 'NFC SOUTH '
                elif name3 in NFC_WEST:
                        Div = 'NFC WEST   '
						
                name = Div.zfill(10).rjust(10).replace('0','')+'     '+W.zfill(2)+'  '+'   '+L.zfill(2)+'  '+'   '+T.zfill(2)+'   '+'[B][COLOR red]'+PCT.zfill(2)+'[/COLOR][/B]'+'    '+name3
                addDir(name, '', iconImg=teamLogo, fanart=logo, mode="")
				

def NFLStats(URL):
		URL = URL
		league = 'nfl'
		logo='http://a.espncdn.com/combiner/i?img=/i/teamlogos/leagues/500/'+league+'.png'
		heading = 'COM  ATT   PCT   YDS    TD    INT SACKS    TEAM   PLAYER'
		heading2 = '-------------------------------------------------------------------------------------'
		addDir('[B]'+heading+'[/B]','',iconImg=logo, fanart=logo, mode="")
		addDir('[B]'+heading2+'[/B]','',iconImg=logo, fanart=logo, mode="")
		URL = 'http://www.espn.com/'+league+'/statistics/player/_/stat/points'
		HTML = OPEN_URL(URL)
		match = re.compile('href="http:\/\/www.espn.com\/nfl\/player\/_\/id\/(.+?)\/.+?>(.+?)<\/a>.+?align="left">(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td><td  class="sortcell">(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td>',re.MULTILINE).findall(HTML)
		for ID,PLAYER,TEAM,COMP,ATT,PCT,YDS,YDSperA,LONG,TD,INT,SACK,RATE,YPG,PPA,SHG,SHA in match:
			headShot = 'http://a.espncdn.com/combiner/i?img=/i/headshots/nfl/players/full/'+ID+'.png'
			teamLogo='http://a.espncdn.com/combiner/i?img=/i/teamlogos/'+league+'/500/'+TEAM+'.png'
			name = COMP.zfill(3)+'    '+ATT.zfill(3)+'    '+PCT.zfill(2)+'    '+'[COLOR blue]'+YDS.zfill(5)+'[/COLOR]'+'    '+TD.zfill(2)+'      '+INT.zfill(2)+'      '+SACK.zfill(2)+'       '+TEAM.zfill(3).replace('0',' ')+'      '+'[B]'+PLAYER+'[/B]'
			addDir(name, '', iconImg=headShot, fanart=teamLogo, mode="")
				
				
def NHLSelect():
		dialog = xbmcgui.Dialog()
		ret = dialog.select('Stats & Standings', ['Division Standings', 'Conference Standings','Wild Card Standings','Scoring Leaders'])
		if ret == 0:
			URL = 'http://www.espn.com/nhl/standings/_/group/3'
			dialog = xbmcgui.Dialog(URL)
			NHLStandings(URL)
		if ret == 1:
			URL = 'http://www.espn.com/nhl/standings/_/group/2'
			dialog = xbmcgui.Dialog(URL)
			NHLStandings(URL)
		if ret == 2:
			URL = 'http://www.espn.com/nhl/standings/_/type/wildcard/group/1'
			dialog = xbmcgui.Dialog()
			NHLStandings(URL)
		if ret == 3:
			URL = 'http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2017/seasontype/2'
			dialog = xbmcgui.Dialog()
			NHLStats(URL)

def NHLStandings(URL):
        URL = URL
        league = 'nhl'
        logo='http://a.espncdn.com/combiner/i?img=/i/teamlogos/leagues/500/'+league+'.png'
        heading = 'CONF     DIVISION          GP    W       L     OTL   PTS    TEAM'
        heading2 = '-------------------------------------------------------------------------------------'
        addDir('[B]'+heading+'[/B]','',iconImg=logo, fanart=logo, mode="")
        addDir('[B]'+heading2+'[/B]','',iconImg=logo, fanart=logo, mode="")
        HTML = OPEN_URL(URL)
        match2 = re.compile('href="http:\/\/www.espn.com\/nhl\/team\/_\/name\/(.+?)\/(.+?)">(.+?)<\/a>\n<\/td>\n<td>(.+?)<\/td><td>(.+?)<\/td><td>(.+?)<\/td><td>(.+?)<\/td><td class="sortcell">(.+?)<\/td><td>',re.MULTILINE).findall(HTML)
        for name1,name2,name3,GP,W,L,OTL,PTS in match2:
                teamLogo='http://a.espncdn.com/combiner/i?img=/i/teamlogos/'+league+'/500/'+name1+'.png'
                atlantic = ['Montreal','Detroit','Ottawa','Tampa Bay','Boston','Buffalo','Florida','Toronto']
                metropolitan = ['Pittsburgh','NY Rangers','Washington','Philadelphia','New Jersey','Columbus','NY Islanders','Carolina']
                central = ['Minnesota','Chicago','St. Louis','Colorado','Dallas','Winnipeg','Nashville']
                pacific =['Edmonton','San Jose','Anaheim','Vancouver','Calgary','Los Angeles','Arizona']
                if name3 in atlantic:
                        Div = 'Atlantic               '
                        Conf = 'EAST'+'       '
                elif name3 in metropolitan:
                        Div = 'Metropolitan     '
                        Conf = 'EAST'+'       '
                elif name3 in central:
                        Div = 'Central               '
                        Conf = 'WEST'+'       '
                elif name3 in pacific:
                        Div = 'Pacific               '
                        Conf = 'WEST'+'       '
                name = Conf+Div+GP.zfill(2)+'  '+'   '+W.zfill(2)+'  '+'   '+L.zfill(2)+'  '+'   '+OTL.zfill(2)+'  '+'   '+'[B][COLOR red]'+PTS.zfill(2)+'[/COLOR][/B]'+'    '+name3
                league='nhl'
                addDir(name, '', iconImg=teamLogo, fanart=logo, mode="")
				

def NHLStats(URL):
		URL = URL
		league = 'nhl'
		logo='http://a.espncdn.com/combiner/i?img=/i/teamlogos/leagues/500/'+league+'.png'
		heading = 'GP   G      A  PTS  +/-   PIM   PTS/G    TEAM   PLAYER'
		heading2 = '-------------------------------------------------------------------------------------'
		addDir('[B]'+heading+'[/B]','',iconImg=logo, fanart=logo, mode="")
		addDir('[B]'+heading2+'[/B]','',iconImg=logo, fanart=logo, mode="")
		URL = 'http://www.espn.com/'+league+'/statistics/player/_/stat/points'
		HTML = OPEN_URL(URL)
		match = re.compile('href="http:\/\/www.espn.com\/nhl\/player\/_\/id\/(.+?)\/.+?>(.+?)<\/a>.+?align="left">(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td><td  class="sortcell">(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td>',re.MULTILINE).findall(HTML)
		for ID,PLAYER,TEAM,GP,G,A,PTS,PlusMinus,PIM,PTSPerGame,INT,PCT,GWG,PPG,PPA,SHG,SHA in match:
			headShot = 'http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/'+ID+'.png'
			teamLogo='http://a.espncdn.com/combiner/i?img=/i/teamlogos/'+league+'/500/'+TEAM+'.png'
			name = GP.zfill(2)+'    '+G.zfill(2)+'    '+A.zfill(2)+'    '+'[COLOR blue]'+PTS.zfill(2)+'[/COLOR]'+'    '+PlusMinus.zfill(2).replace('-',' -')+'    '+PIM.zfill(3)+'    '+PTSPerGame.zfill(3)+'       '+TEAM.zfill(4).replace('0',' ')+'      '+'[B]'+PLAYER+'[/B]'
			addDir(name, '', iconImg=headShot, fanart=teamLogo, mode="")
				

def NBASelect():
        NBA1='http://www.espn.com/nba/standings/_/group/division'
        NBA2='http://www.espn.com/nba/standings'
        NBA3='http://www.espn.com/nba/standings/_/group/league'
        NBA4='http://www.espn.com/nba/statistics/player/_/stat/points/sort/points/year/2017/seasontype/2'
        dialog = xbmcgui.Dialog()
        ret = dialog.select('Standings', ['Division', 'Conference','League','Scoring Leaders'])
        if ret == 0:
            URL = NBA1
            dialog = xbmcgui.Dialog(URL)
            NBAStandings(URL)
        if ret == 1:
            URL = NBA2
            dialog = xbmcgui.Dialog(URL)
            NBAStandings(URL)
        if ret == 2:
            URL = NBA3
            dialog = xbmcgui.Dialog()
            NBAStandings(URL)
        if ret == 3:
            URL = NBA4
            dialog = xbmcgui.Dialog()
            NBAStats(URL)
          
		  
def NBAStandings(URL):
        league = 'NBA'
        logo='http://a.espncdn.com/combiner/i?img=/i/teamlogos/leagues/500/'+league+'.png'
        heading = 'DIVISION           W      L        PCT   GB     TEAM'
        addDir('[B]'+heading+'[/B]','',iconImg=logo, fanart=logo, mode="")
        HTML = OPEN_URL(URL)
        match = re.compile('align="left">Eastern Conference </td><td>((.|\n)*)class="colhead',re.MULTILINE).findall(HTML)
        string = str(match)
        match2 = re.compile('<abbr title="(.+?)">(.+?)<\/abbr><\/span><\/a><\/td><td style="white-space:no-wrap;" class="">(.+?)<\/td><td style="white-space:no-wrap;" class="">(.+?)<\/td><td style="white-space:no-wrap;" class="">(.+?)<\/td><td style="white-space:no-wrap;" class="">(.+?)<\/td><td',re.MULTILINE).findall(HTML)
        for name3,name2,W,L,PCT,GB in match2:
                teamLogo='http://a.espncdn.com/combiner/i?img=/i/teamlogos/'+league+'/500/'+name2+'.png'
                ATLANTIC = ['Toronto Raptors','Boston Celtics','New York Knicks','Brooklyn Nets','Philadelphia 76ers']
                CENTRAL = ['Cleveland Cavaliers','Detroit Pistons','Chicago Bulls','Milwaukee Bucks','Indiana Pacers']
                SOUTHEAST = ['Charlotte Hornets','Atlanta Hawks','Orlando Magic','Miami Heat','Washington Wizards']
                NORTHWEST = ['Oklahoma City Thunder','Utah Jazz','Portland Trail Blazers','Denver Nuggets','Minnesota Timberwolves']
                PACIFIC = ['LA Clippers','Golden State Warriors','Los Angeles Lakers','Sacramento Kings','Phoenix Suns']
                SOUTHWEST = ['San Antonio Spurs','Houston Rockets','Memphis Grizzlies','Dallas Mavericks','New Orleans Pelicans']
                if name3 in ATLANTIC:
                        Div = 'ATLANTIC     '
                elif name3 in CENTRAL:
                        Div = 'CENTRAL       '
                elif name3 in SOUTHEAST:
                        Div = 'SOUTHEAST  '
                elif name3 in NORTHWEST:
                        Div = 'NORTHWEST '
                elif name3 in PACIFIC:
                        Div = 'PACIFIC          '
                elif name3 in SOUTHWEST:
                        Div = 'SOUTHWEST '
						
                name = Div.zfill(10).rjust(10).replace('0','')+'     '+W.zfill(2)+'  '+'   '+L.zfill(2)+'  '+'   '+PCT.zfill(4)+'   '+'[B][COLOR red]'+GB.rjust(3)+'[/COLOR][/B]'+'    '+name3
                addDir(name, '', iconImg=teamLogo, fanart=logo, mode="")

				
def NBAStats(URL):
		URL = URL
		league = 'nba'
		logo='http://a.espncdn.com/combiner/i?img=/i/teamlogos/leagues/500/'+league+'.png'
		heading = 'GP    MPG    PTS        FG%      3P%      TEAM      PLAYER'
		heading2 = '-------------------------------------------------------------------------------------'
		addDir('[B]'+heading+'[/B]','',iconImg=logo, fanart=logo, mode="")
		addDir('[B]'+heading2+'[/B]','',iconImg=logo, fanart=logo, mode="")
		URL = 'http://www.espn.com/'+league+'/statistics/player/_/stat/scoring-per-game/sort/avgPoints/year/2017/seasontype/2'
		HTML = OPEN_URL(URL)
		match = re.compile('href="http:\/\/www.espn.com\/nba\/player\/_\/id\/(.+?)\/.+?>(.+?)<\/a>.+?align="left">(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td><td.+?>(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td><td >(.+?)<\/td><td',re.MULTILINE).findall(HTML)
		for ID,PLAYER,TEAM,GP,MPG,PTS,FGMFGA,FG,PMPA,ThreePoint,FTMFTA in match:
			headShot = 'http://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/'+ID+'.png'
			teamLogo='http://a.espncdn.com/combiner/i?img=/i/teamlogos/'+league+'/500/'+TEAM+'.png'
			name = GP.zfill(2)+'      '+MPG.zfill(4)+'      '+'[COLOR blue]'+PTS.zfill(4)+'[/COLOR]'+'      '+FG.zfill(4).replace('-',' -')+'      '+ThreePoint.zfill(4)+'       '+TEAM.zfill(4).replace('0',' ')+'       '+'[B]'+PLAYER+'[/B]'
			addDir(name, '', iconImg=headShot, fanart=teamLogo, mode="")
				
				
def MLBSelect():
        MLB1='http://www.espn.com/mlb/standings/_/group/division'
        MLB2='http://www.espn.com/mlb/standings/_/group/league'
        MLB3='http://www.espn.com/mlb/standings/_/group/overall'
        MLB4='http://www.espn.com/mlb/standings/_/view/wild-card/group/overall'
        MLB5='http://www.espn.com/mlb/stats/batting/_/league/mlb'
        dialog = xbmcgui.Dialog()
        ret = dialog.select('Standings', ['Division', 'Conference','League','Wild Card','Leaders'])
        if ret == 0:
            URL = MLB1
            dialog = xbmcgui.Dialog(URL)
            MLBStandings(URL)
        if ret == 1:
            URL = MLB2
            dialog = xbmcgui.Dialog(URL)
            MLBStandings(URL)
        if ret == 2:
            URL = MLB3
            dialog = xbmcgui.Dialog()
            MLBStandings(URL)
        if ret == 3:
            URL = MLB4
            dialog = xbmcgui.Dialog()
            MLBStandings(URL)
        if ret == 4:
            URL = MLB5
            dialog = xbmcgui.Dialog()
            MLBStats(URL)
          
		  
def MLBStandings(URL):
        league = 'MLB'
        logo='http://a.espncdn.com/combiner/i?img=/i/teamlogos/leagues/500/'+league+'.png'
        heading = 'DIVISION           W      L        PCT   GB     TEAM'
        addDir('[B]'+heading+'[/B]','',iconImg=logo, fanart=logo, mode="")
        HTML = OPEN_URL(URL)
        match = re.compile('align="left">Eastern Conference </td><td>((.|\n)*)class="colhead',re.MULTILINE).findall(HTML)
        string = str(match)
        match2 = re.compile('<abbr title="(.+?)">(.+?)<\/abbr><\/span><\/a><\/td><td style="white-space:no-wrap;" class="">(.+?)<\/td><td style="white-space:no-wrap;" class="">(.+?)<\/td><td style="white-space:no-wrap;" class="">(.+?)<\/td><td style="white-space:no-wrap;" class="">(.+?)<\/td><td',re.MULTILINE).findall(HTML)
        for name3,name2,W,L,PCT,GB in match2:
                teamLogo='http://a.espncdn.com/combiner/i?img=/i/teamlogos/'+league+'/500/'+name2+'.png'
                AL_EAST = ['Boston Red Sox','Baltimore Orioles','Toronto Blue Jays','New York Yankees','Tampa Bay Rays']
                AL_CENTRAL = ['Cleveland Indians','Detroit Tigers','Kansas City Royals','Chicago White Sox','Minnesota Twins']
                AL_WEST = ['Texas Rangers','Seattle Mariners','Houston Astros','Los Angeles Angels','Oakland Athletics']
                NL_EAST = ['Washington Nationals','New York Mets','Miami Marlins','Philadelphia Phillies','Atlanta Braves']
                NL_CENTRAL = ['Chicago Cubs','St. Louis Cardinals','Pittsburgh Pirates','Milwaukee Brewers','Cincinnati Reds']
                NL_WEST = ['Los Angeles Dodgers','San Francisco Giants','Colorado Rockies','Arizona Diamondbacks','San Diego Padres']
                if name3 in AL_EAST:
                        Div = 'AL EAST          '
                elif name3 in AL_CENTRAL:
                        Div = 'AL CENTRAL  '
                elif name3 in AL_WEST:
                        Div = 'AL WEST          '
                elif name3 in NL_EAST:
                        Div = 'NL EAST          '
                elif name3 in NL_CENTRAL:
                        Div = 'NL CENTRAL  '
                elif name3 in NL_WEST:
                        Div = 'NL WEST          '
						
                name = Div.zfill(10).rjust(10).replace('0','')+'     '+W.zfill(2)+'  '+'   '+L.zfill(2)+'  '+'   '+PCT.rjust(4)+'   '+'[B][COLOR red]'+GB.rjust(4)+'[/COLOR][/B]'+'    '+name3
                addDir(name, '', iconImg=teamLogo, fanart=logo, mode="")

def MLBStats(URL):
		URL = URL
		league = 'mlb'
		logo='http://a.espncdn.com/combiner/i?img=/i/teamlogos/leagues/500/'+league+'.png'
		heading = 'AB     R        H        HR    RBI    AVG   SLG     TEAM     PLAYER'
		heading2 = '-------------------------------------------------------------------------------------'
		addDir('[B]'+heading+'[/B]','',iconImg=logo, fanart=logo, mode="")
		addDir('[B]'+heading2+'[/B]','',iconImg=logo, fanart=logo, mode="")
		HTML = OPEN_URL(URL)
		match = re.compile('http:\/\/www.espn.com\/mlb\/player\/_\/id\/(.+?)\/.+?>(.+?)<\/a>.+?align=".+?">(.+?)<\/td><td .*?align=".+?">(.+?)<\/td><td .*?align=".+?">(.+?)<\/td><td .*?align=".+?">(.+?)<\/td><td .*?align=".+?">(.+?)<\/td><td .*?align=".+?">(.+?)<\/td><td .*?align=".+?">(.+?)<\/td><td .*?align=".+?">(.+?)<\/td><td .*?align=".+?">(.+?)<\/td><td .*?align=".+?">(.+?)<\/td><td .*?align=".+?">(.+?)<\/td><td .*?align=".+?">(.+?)<\/td><td .*?align=".+?">(.+?)<\/td><td .*?align=".+?">(.+?)<\/td><td .*?align=".+?">(.+?)<\/td><td .*?align=".+?">(.+?)<\/td><td',re.MULTILINE).findall(HTML)
		for ID,PLAYER,TEAM,AB,R,H,B2,B3,HR,RBI,SB,CS,BB,SO,AVG,OBP,SLG,OPS in match:
			headShot = 'http://a.espncdn.com/combiner/i?img=/i/headshots/mlb/players/full/'+ID+'.png'
			teamLogo='http://a.espncdn.com/combiner/i?img=/i/teamlogos/'+league+'/500/'+TEAM+'.png'
			name = AB.zfill(3)+'    '+R.zfill(3)+'    '+H.zfill(3)+'    '+HR.zfill(2)+'    '+RBI.zfill(3).replace('-',' -')+'    '+'[COLOR blue]'+AVG.zfill(4)+'[/COLOR]'+'    '+SLG.zfill(4)+'       '+TEAM.zfill(4).replace('0',' ')+'      '+'[B]'+PLAYER+'[/B]'
			addDir(name, '', iconImg=headShot, fanart=teamLogo, mode="")
				
def OPEN_URL(url):
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36')
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		return link			

		
def addDir(title, url, iconImg="DefaultVideo.png", fanart="", mode=""):
		sys_url = sys.argv[0] + '?url=' + urllib.quote_plus(url) +'&mode=' + urllib.quote_plus(str(mode))
		item = xbmcgui.ListItem(title, iconImage=iconImg, thumbnailImage=iconImg)
		item.setProperty('fanart_image', fanart)
		item.setInfo(type='Video', infoLabels={'Title': title})
		xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys_url, listitem=item, isFolder=True)

