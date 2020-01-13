import requests, bs4

x = input("調べたい文字を入力してください -> ")

if x != "":

    list1 = [["中国語", "null"], ["韓国語", "null"], ["ベトナム語", "null"], ["スペイン語", "null"], ["インドネシア語", "null"], ["英語", "null"]]

    url = "https://ja.wikipedia.org/wiki/" + str(x)
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    mw = soup.find("div", id="p-lang")
    s = mw.find("div", class_="body")
    a = s.find_all("a")

    for i in range(len(a)-1):
        list2 = a[i].get("title").split(": ") # ["言語", "その言語での言い方"]

        for j in range(len(list1)):

            if list1[j][0] == list2[0]:
                list1[j][1] = list2[1]

    for i in list1:
        print(i)
            
else:
    print("なんでもいいから入力してくれ")
