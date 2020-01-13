from gensim.models import word2vec
import MeCab
import sys
import re
import random
from collections import Counter

#出題された単語を０番目、それ以降を候補としてリストで渡された場合を想定している

def WrongWord(Question,AllWord):
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


