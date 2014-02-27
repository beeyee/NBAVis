# Created by Chaowei Gao
# 2014.2.26
# Used to extract the information from a text live himl

from bs4 import BeautifulSoup

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
			play_by_play = elem[1];	
		except KeyError:
			continue
		
# get the play part		
for child in play_by_play:
    try:
		if(child['class'] == ['bd']):
			plays = child
		except:
			continue
		
