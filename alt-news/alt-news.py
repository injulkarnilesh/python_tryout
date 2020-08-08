import requests
import xml.etree.ElementTree as ET

page = 1

while True:
    url = 'https://www.altnews.in/feed/'

    print('Getting page {}'.format(page))

    pararms = dict(paged=page)
    r = requests.get(url=url, params=pararms)
    xml = r.text

    root = ET.fromstring(xml)
    titles = root.findall('./channel/item/title')
    count = len(titles)
    
    if count == 0:
        break

    file = open('alt.txt', 'a')
    for title in titles:
        txt = title.text.lower()
        file.write(txt + '\n')

    file.close()

    page += 1
