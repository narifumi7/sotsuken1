import requests, bs4

#url = 'https://ja.wikipedia.org/wiki/' + str(input())
url = 'https://ja.wikibooks.org/wiki/新課程高等学校数学III'



res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, "html.parser")

#s = soup.find('div', id="toc")
#a = s.find('li', class_="toclevel-1 tocsection-1")
#print(a)
#for i in s:
#    print(i.getText().split()[0])
