import bs4
import urllib.request as urllib2
import re
import datetime

seedset = ["http://toscrape.com/", "http://mentalfloss.com/article/53792/17-ancient-abandoned-websites-still-work",
           "http://scratchpads.eu/explore/sites-list"]

totallinks = []

for url in seedset:
    html_page = urllib2.urlopen(url)
    soup = bs4.BeautifulSoup(html_page, features = "lxml")
    links = []

    for link in soup.findAll('a', attrs = {'href': re.compile("^http://")}):
        links.append(link.get('href'))
    totallinks += links

urlfile = open("index.txt", "w+")

i = 0
for link in totallinks:
    ts = datetime.datetime.now()
    ts.strftime("%m/%d/%Y")
    line = str(i) + ".html " + str(ts) + " " + link + "\n"
    urlfile.write(line)
    i+=1

