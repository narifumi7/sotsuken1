import requests
import pandas as pd
from bs4 import BeautifulSoup

html=requests.get("https://ja.wikibooks.org/wiki/線型代数学").text
soup=BeautifulSoup(html,"html.parser")

for script in soup(["script", "style"]):
    script.decompose()
    
text=soup.get_text()

lines= [line.strip() for line in text.splitlines()]
l2 = [x for x in lines if x]
print(l2)