import twtd_invoker # twtd_invoker を読み込む

Jlist = ['単語', '意味'] # 例

def Translate(Jlist): # 「単語」と「意味」を翻訳する関数（変数はlist型[str(word), str(mean)]）
    lanlist = ['zh-CN', 'ko', 'vi', 'es', 'id', 'en'] # 順に「中国語」, 「韓国語」, 「ベトナム語」, 「スペイン語」, 「インドネシア語」, 「英語」に翻訳
    anslist = [] # 翻訳結果をいれるリスト
    anslist.append(Jlist) # はじめに日本語の「単語」と「意味」のセットを入れておく
    word = Jlist[0] # 変数のリストの「単語」を word に代入
    mean = Jlist[1] # 変数のリストの「意味」を mean に代入

    for i in lanlist: # 言語を
        ans_w = twtd_invoker.twtd_client.translate('ja', i, word, twtd_invoker.tArray, 'en') # word を i に代入された言語に翻訳
        ans_m = twtd_invoker.twtd_client.translate('ja', i, mean, twtd_invoker.tArray, 'en') # mean を i に代入された言語に翻訳
        anslist.append([ans_w, ans_m]) # ans_w とans_m をリストでセットにし, anslist に追加

    return anslist # 翻訳後の結果を返す

# 確認用
print(Translate(Jlist))