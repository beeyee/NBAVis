# Created by Chaowei Gao
# 2014.2.26
# Used to extract the information from a text live himl

from bs4 import BeautifulSoup
from pylab import *
import csv

# open the html file with BeautifulSoup.
soup = BeautifulSoup(open('./files/text_live_file/mavs-76ers-20140221.html'))
html = soup.html

# find all the div tags.
divs = html.find_all('div')

# in all of the div tags, find the play by play part.
for elem in divs:
    try:
		if(elem['id'] == 'mediasportsplaybyplay'):
		# print elem
			play_by_play = elem;	
	except KeyError:
		continue
		
# get the play part		
for child in play_by_play:
    try:
		if(child['class'] == ['bd']):
			plays = child
	except:
		continue
		
for child in plays:
	try:
		if(child.name == 'dl'):
			real_play = child
	except:
		continue
				

results = open('./results.csv', 'w')
wholelist = list()
arow = list();
	for child in real_play:
		try:
			if(child['class'][0] == 'play'):
				for playchild in child:
					try:
						if(playchild.name == 'span'):
							for spanchild in playchild:
								arow.append(spanchild.string)
							elif(playchild['class'][0] == 'team-logo'):
								arow.append(playchild['title'])
					except:
						continue
			elif(child['class'][0] == 'period'):
				tmpperiod = child.string
			elif(child['class'][0] == 'clock'):          
				csv.writer(results).writerow(arow)         
				arow[:] = []
				arow.append(tmpperiod)
				arow.append(child.string)
		except:
			continue
results.close()






		

			

