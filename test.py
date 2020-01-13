from sotsuken import Translate,WrongWord,WrongWord2
#翻訳のテスト
l = ["百万遍では立て看が撤去されました。","嫌いです。しかし、大好きです。"]
print(Translate(l))
print("文字を入力してください")
#WrongWordのテスト
v = input()
print(WrongWord(v))
#WrongWord2のテスト
s=["微分"]
l = ["形態素解析","関数","数学","積分"]
print(WrongWord2(s,l))
