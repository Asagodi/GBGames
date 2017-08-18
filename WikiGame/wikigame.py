import scrapy
import urllib2
import bs4
from bs4 import BeautifulSoup

wikiurl = "https://en.wikipedia.org/wiki/The_Glass_Bead_Game?oldformat=true"
page = urllib2.urlopen(wikiurl)
soup = BeautifulSoup(page)


