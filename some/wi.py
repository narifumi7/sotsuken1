import re
import requests
from bs4 import BeautifulSoup
#BeautifulSoupの設定
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"}
url="https://syosetu.com/syuppan/view/bookid/3387/"
response = requests.get(url=url, headers=headers)
html = response.content
soup = BeautifulSoup(html, "lxml")
#ここで「書籍情報」内のテキストを全取得
all_text=soup.find(class_="book_contentinfo").text
#ここで取得したテキストを1行ずつ分割してリストに収納
all_text_list=all_text.split("\n")
#リストを1行ずづ読み込んで部分一致する行だけ抽出
for text in all_text_list:
    if "出版社" in text:
        print(text)