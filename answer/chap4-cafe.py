'''
1. レギュラー(1 分)
2. カプチーノ(2 分)
3. エスプレッソ(2 分)
4. ラテ(3 分)
5. アイリッシュ(3 分)
来店したお客様は,自分の名前(XX)と注文の種類(YY)と数(ZZ)を入力
します.種類と数によって待ち時間を計算(WW)します.もしも,カフェ
にないものが入力されたときは,「残念ながらそれは扱っていません.」と
いうメッセージを出します.入力に問題がなければ,以下のメッセージを
出します.

 YY,個数は ZZ ですね.
WW 分,お待ちください.
'''

xx=input("Python カフェにようこそ!名前をいれてください")
print (xx+" 様,ご注文ありがとうございます")
yy=input("注文内容はいかがでしょうか？　レギュラー カプチーノ　エスプレッソ　ラテ　アイリッシュ　どれにしましょうか？")
zz=input("個数はいくらでしょうか？")
print ("注文の種類は"+yy+" 個数は"+zz+" ですね")
wtime=0

if (yy[0:1]=='レギュラー'):
	wtime=1
elif (yy[0:1]=='カプチーノ' or yy[0:1]=='エスプレッソ'):
	wtime=2
elif (yy=='ラテ' or yy=='アイリッシュ'):	
	wtime=3
else:
	print ('残念ながらそれは扱っていません')
waitw=wtime*int(zz)
print (str(waitw)+'分,お待ちください')

