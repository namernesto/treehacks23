### Scraping links of each stanford profile
import json
import requests
import string
from bs4 import BeautifulSoup

links = []
for i in range(1, 75):
    url = 'https://profiles.stanford.edu/browse/stanford?p=' + str(i) + '&affiliations=capFaculty&ps=100'
    result = requests.get(url)
    src = result.content
    soup = BeautifulSoup(src, 'html.parser')
    link_class = soup.find_all("div", {"class": "customrow no-margin"})
    for link in [t.find("a") for t in link_class]:
        href = link.get("href")
        if href:
            links.append(href)
with open("/scraping/output-files/profiles-links.json", "w") as outfile:
    json.dump(links, outfile)