from urllib.request import urlopen as uop
from bs4 import BeautifulSoup as bs

j=0
k=1
f = open("phone_list.txt","w+", encoding='UTF-8')
while k <= 1:
    url = 'https://www.gsmarena.com/makers.php3'

    uclient = uop(url)

    page_html = uclient.read()
    uclient.close()

    page_soup = bs(page_html, "html.parser")

    links = page_soup.find_all("a")



    for i in links:
        href = str(j+1) + "- " + i.get_text() + '\n' + '\n'
        f.write(href)
        j+=1
    k+=1
f.close()
