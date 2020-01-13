import twtd_invoker # twtd_invoker を読み込む

from gensim.models import word2vec
import MeCab
import sys
import re
import random
from collections import Counter

##########ここから翻訳するやつ##########
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
#l = ["好き","嫌いです。しかし、大好きです。"]
#print(Translate(l))
##########ここまで翻訳するやつ##########


##########ここから誤回答の候補を出すやつ##########

def WrongWord(Question):
	WrongWord_list = []#誤解等のリストの用意

	#以下、単語じゃなかった場合などに対処するため、分かち書きの処理
	parse = MeCab.Tagger().parse(Question)
	lines = parse.split('\n')
	items = (re.split('[\t,]', line) for line in lines)

	for item in items:
		word = item[0]
		break

	#以下、word2vecを使い、類似した単語を探す処理
	model = word2vec.Word2Vec.load("./wiki.model")
	results = model.wv.most_similar(positive=[word])

	for result in results:
		result_cut = result[0]
		WrongWord_list.append(result_cut)
		
	return WrongWord_list


#s = input()#テスト
#print(WrongWord(s))#テスト
##########ここまで呉回答出すやつ	##########


##########ここから問題と類似する単語渡された単語からを見つけて返すやつ##########
#正常に作動した場合は類義語を三つ、エラーが出た場合は渡されたNoneと単語からランダムで三つ出力される。
def WrongWord2(Question,AllWord):
	try:
		WrongWord_list = []#誤解等のリストの用意
		Word_list = []#分かちがきした単語のリストの用意
		Word_list2 = {}#辞書型で結果を保存するための用意
	
		#以下、単語じゃなかった場合などに対処するため、分かち書きの処理
		#問題の単語の処理
		for i in Question:
			parse = MeCab.Tagger().parse(i)
			lines = parse.split('\n')
			items = (re.split('[\t,]', line) for line in lines)
		
        	#分かちがきしたものをリストに保存する
			for item in items:
				word = item[0]
				Word_list.append(word)
				break

		#誤回答の候補の処理
		for i in AllWord:
			parse = MeCab.Tagger().parse(i)
			lines = parse.split('\n')
			items = (re.split('[\t,]', line) for line in lines)
		
        	#分かちがきしたものをリストに保存する
			for item in items:
				word = item[0]
				Word_list.append(word)
				break

		#リストから出題された問題の単語を取り出す		
		original = Word_list.pop(0)
	
		#以下、word2vecを使い、類似した単語を探す処理
		model = word2vec.Word2Vec.load("./wiki.model")
	
		#出題された単語と渡された各候補の類似度を計算して辞書型として保存する
		for i in Word_list:
			similarity = model.wv.similarity(original,i)
			Word_list2[i] = similarity
		
		#print(Word_list2)#確認用
		#降順にソートしてリストに保存,類似度上位３つをリストで出力する
		num = 0
	
		for k, v in sorted(Word_list2.items(), key = lambda x:-x[1]):
			WrongWord_list.append(k)
			num += 1
			if num == 3:
				break
		
		return WrongWord_list
	except:
		print(random.sample(AllWord, 3))



