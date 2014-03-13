import urllib2
from bs4 import BeautifulSoup
from pylab import *
import csv

response = urllib2.urlopen('http://sports.yahoo.com/nba/players')
html = response.read()
html_team_list = BeautifulSoup(html)
all_a = html_team_list.find_all('a')

team_links = {}
for a in all_a:
    try:
        parts = []
        parts = a['href'].split('/')
        if(parts[-1] == 'roster'):
            team_links[a.string] = a['href']
    except:
        continue

def set_players(teamname, part_url):
    whole_list = []
    teamfile = open('./files/player_list/' + teamname + '.csv', 'wb')
    res = urllib2.urlopen('http://sports.yahoo.com' + part_url)
    html = BeautifulSoup(res.read())
    all_tr = html.find_all('tr')
    arow = []
    for tr in all_tr:
        for td in tr:
            try:
                if(td['class'][0] == 'number'):
                    if(len(arow) > 6):
                        whole_list.append(list(arow))    
                    arow[:] = []
                    arow.append(td.string)
                elif(td['class'][0] == 'player'):
                    arow.append(td.string)
                elif(td['class'][0] == 'position'):
                    arow.append(td.string)
                elif(td['class'][0] == 'bats'):
                    arow.append(td.string)
                elif(td['class'][0] == 'throws'):
                    arow.append(td.string)
                elif(td['class'][0] == 'height'):
                    arow.append(td.string)
                elif(td['class'][0] == 'weight'):
                    arow.append(td.string)
                elif(td['class'][0] == 'age'):
                    arow.append(td.string)
                elif(td['class'][0] == 'experience'):
                    arow.append(td.string)
                elif(td['class'][0] == 'birthplace'):
                    arow.append(td.string)
                elif(td['class'][0] == 'college'):
                    arow.append(td.string)
                elif(td['class'][0] == 'salary'):
                    arow.append(td.string)
            except:
                continue
    csv.writer(teamfile).writerows(whole_list)
    teamfile.close()

for k,v in team_links.items():
    set_players(k, v)
