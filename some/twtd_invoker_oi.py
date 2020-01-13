from langrid.clients import BindingNode, TranslationWithTemporalDictionaryClient
from settings import lg_config
#sslをインポートし、５行目の文を書くと認証エラーが出ない
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#以下翻訳メソッド
def trans_test(arg1,arg2):
	#全体のリスト、言語別のリストを用意
	return_word = []
	vessel_jp = []
	vessel_zh = []
	vessel_ko = []
	vessel_vi = []
	vessel_es = []
	vessel_id = []
	vessel_en = []
	
	twtd_client = TranslationWithTemporalDictionaryClient('http://langrid.org/service_manager/wsdl/kyoto1.langrid:TranslationCombinedWithBilingualDictionaryWithLongestMatchSearch',
                                                      	lg_config['userid'], lg_config['password'])

	#Translationの作成
	# 辞書型を利用した場合
	t={'headWord':'SOURCE', 'targetWords':['TRANSLATION']}

	tArray = [t]

	#バインディング
	#BindingNode版
	twtd_client.getTreeBindings().append(BindingNode('MorphologicalAnalysisPL', 'Mecab'))
	twtd_client.getTreeBindings().append(BindingNode('BilingualDictionaryWithLongestMatchSearchPL', 'KyotoTourismDictionaryDb'))
	twtd_client.getTreeBindings().append(BindingNode('TranslationPL', 'GoogleTranslateNMT'))
	#バインディングがネストした場合
	#twtd_client.getTreeBindings().append(BindingNode('TranslationPL', 'TwoHopTranslationEn').addChildren(BindingNode('FirstTranslationPL','KyotoUJServer')).addChildren(BindingNode('SecondTranslationPL','KyotoUJServer')))

	#直接JSONでバインディング情報を設定する場合
	#twtd_client.setJsonBindings('[{"children":[],"invocationName":"MorphologicalAnalysisPL", "serviceId":"Mecab"}, {"children":[],"invocationName":"TranslationPL", "serviceId":"GoogleTranslateNMT"}]')

	#翻訳サービス呼び出し
	#各言語で翻訳し、リストに入れていく
	#日本語
	vessel_jp.append(arg1)
	vessel_jp.append(arg2)
	return_word.append(vessel_jp)
	
	#中国語
	zh1 = (twtd_client.translate('ja', 'zh', arg1, tArray, 'en'))
	zh2 = (twtd_client.translate('ja', 'zh', arg2, tArray, 'en'))
	vessel_zh.append(zh1)
	vessel_zh.append(zh2)
	return_word.append(vessel_zh)
	
	#韓国語
	ko1 = (twtd_client.translate('ja', 'ko', arg1, tArray, 'en'))
	ko2 = (twtd_client.translate('ja', 'ko', arg2, tArray, 'en'))
	vessel_ko.append(ko1)
	vessel_ko.append(ko2)
	return_word.append(vessel_ko)
	
	#ベトナム語
	vi1 = (twtd_client.translate('ja', 'vi', arg1, tArray, 'en'))
	vi2 = (twtd_client.translate('ja', 'vi', arg2, tArray, 'en'))
	vessel_vi.append(vi1)
	vessel_vi.append(vi2)
	return_word.append(vessel_vi)

	#スペイン語
	es1 = (twtd_client.translate('ja', 'es', arg1, tArray, 'en'))
	es2 = (twtd_client.translate('ja', 'es', arg2, tArray, 'en'))
	vessel_es.append(es1)
	vessel_es.append(es2)
	return_word.append(vessel_es)
	
	#インドネシア語
	id1 = (twtd_client.translate('ja', 'id', arg1, tArray, 'en'))
	id2 = (twtd_client.translate('ja', 'id', arg2, tArray, 'en'))
	vessel_id.append(id1)
	vessel_id.append(id2)
	return_word.append(vessel_id)
	
	#英語
	en1 = (twtd_client.translate('ja', 'en', arg1, tArray, 'en'))
	en2 = (twtd_client.translate('ja', 'en', arg2, tArray, 'en'))
	vessel_en.append(en1)
	vessel_en.append(en2)
	return_word.append(vessel_en)
	
	#テスト出力
	print(return_word)


