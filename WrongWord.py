from gensim.models import word2vec
import MeCab
import sys
import re
from collections import Counter

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
	print(WrongWord_list)		


