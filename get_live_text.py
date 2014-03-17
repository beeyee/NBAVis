import urllib2
from bs4 import BeautifulSoup
from pylab import *
import csv

# def get_text_live_html()


prefix = 'http://www.cbssports.com/nba/scoreboard/2014'
for month in xrange(13):
    for day in xrange(32):
        if(0<month and month<10):
            if(0<day and day<10):
                response = urllib2.urlopen(prefix+'0'+str(month)+'0'+str(day))
            elif(10<=day):
                response = urllib2.urlopen(prefix+'0'+str(month)+str(day))
        elif(10<=month):
            if(0<day and day<10):
                response = urllib2.urlopen(prefix+str(month)+'0'+str(day))
            elif(10<=day):
                response = urllib2.urlopen(prefix+str(month)+str(day))
        html = response.read()
        soup = BeautifulSoup(html)
        html = soup.html
        a_list = html.find_all('a')
        for a in a_list:
            try:
                if(a['class'][0] == 'gameTracker'):
                    live_link = 'http://www.cbssports.com' + a['href']
                    string_tokens = live_link.split('/')
                    if(string_tokens[5] == 'live'):
                        playbyplay_link = live_link.replace('live','playbyplay')
                        playbyplay_response = urllib2.urlopen(playbyplay_link)
                        playbyplay_html = playbyplay_response.read()
                        print string_tokens[-1]
                        playbyplay_file = open('./files/text_live_file/'+string_tokens[-1]+'.html','w')
                        playbyplay_file.write(playbyplay_html)
                        playbyplay_file.close()
            except:
                continue

'''
response = urllib2.urlopen('http://sports.yahoo.com/nba/players')
html = response.read()
html_team_list = BeautifulSoup(html)
all_a = html_team_list.find_all('a')
'''
