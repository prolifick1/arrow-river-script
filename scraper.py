import requests
import bs4
from bs4 import BeautifulSoup
import re
import wget
import os

URL = 'https://www.arrowriver.ca/desana.html'
mp3url = 'https://arrowriver.ca/dhammatalks/'
pattern = 'talks\d+\/\d+_\w+'

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0"}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

mp3s = []

def getTitles():
  for tr in soup.find_all('tr'):
    if(tr.find('td', class_='talk') != None and tr.find('td', class_='date') != None and tr.find('input') != None): 
      try:
        mp3s.append({
          'title' : tr.find('td', class_='talk').getText().strip(),
          'date' : tr.find('td', class_='date').getText().strip(),
          'url' : getUrl(tr)
          })
      except:pass
  return mp3s

def getUrl(tr):
  x = tr.find('input')['onclick']
  if(re.match('javascript:streamPage', x)):
    return(mp3url + re.findall('talks15\/\d+_\w+', x)[0] + '.mp3')


getTitles()

for mp3 in mp3s:
  wget.download(mp3.get('url'), mp3.get('title') + ' ' + mp3.get('date')+ '.mp3')