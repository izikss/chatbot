from urllib.request import urlopen as uop
from bs4 import BeautifulSoup as bs

j=0
k=1
f = open("blackberry.txt","w+", encoding='UTF-8')
while k <= 1:
    url = 'https://assistance.orange.sn/questions/browse?page=1&search=param%C3%A8tres+Internet+pour+BlackBerry&utf8=%E2%9C%93'

    uclient = uop(url)

    page_html = uclient.read()
    uclient.close()

    page_soup = bs(page_html, "html.parser")

    links = page_soup.find_all("a", {"class": "content_permalink"})



    for i in links:
        href = str(j+1) + "- " + i.get_text() + '\n' + '\n'
        f.write(href)
        j+=1
    k+=1
f.close()
