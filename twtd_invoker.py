from langrid.clients import BindingNode, TranslationWithTemporalDictionaryClient
from settings import lg_config
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

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


#韓国語
#print(twtd_client.translate('ja', 'ko', '好き', tArray, 'en'))
#英語
#print(twtd_client.translate('ja', 'en', '好き', tArray, 'en'))
#ベトナム語
#print(twtd_client.translate('ja', 'vi', '好き', tArray, 'en'))
#中国語
#print(twtd_client.translate('ja', 'zh', '好き', tArray, 'en'))
#スペイン語
#print(twtd_client.translate('ja', 'es', '好き', tArray, 'en'))
#インドネシア語
#print(twtd_client.translate('ja', 'id', '好き', tArray, 'en'))


