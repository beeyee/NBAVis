# Created by Chaowei Gao
# 2014.3.17
# Used to extract the information from a text live html
from bs4 import BeautifulSoup
from pylab import *
import csv

def extract_play_by_play(filename):
    soup = BeautifulSoup(filename)
    html = soup.html
    body = html.body
    for child in body:
    if(child.name == 'div' and child['id'] == 'mantle_skin'):
        for adiv in child:
            try:
                if(adiv['id'] == 'pageRow'):
                    tmp_divs = adiv.find_all('div')
                    for div in tmp_divs:
                        try:
                            if(div['class'][0] == 'column1'):
                                for childdiv in div:
                                    if(childdiv.name == 'table'):
                                        playbyplay = childdiv
                        except:
                            continue
            except:
                continue


    