#関数型プログラム

#このプログラムでは副作用が起こる
a = 0

def increment(): #インクリメントは増加するという意味
    global a #グローバル変数にaという関数を追加する。
    a += 1
    print(a)

increment()