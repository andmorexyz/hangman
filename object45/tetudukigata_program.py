#手続型プログラミング

x = 2
y = 4
z = 8
xyz = x + y * z
print(xyz)

pop = []  #洋楽ポップソングを入れるリスト
jpop = [] #jポップを入れるリスト

def collect_songs(): #関数()←デフォルトの値
    song = "曲名を入力してください:"
    ask = "pかjのどちらかを選んでください。qで終われます。:"

    while True:
        genre = input(ask)
        if genre == "q": #もしaskで入力されたのが"q"と一緒なら
            print("ポップソング",pop)
            print("Jポップ",jpop)
            break #終了

        if genre == "p":
            p = input(song)
            pop.append(p) #popリストにp=入力された曲を追加する

        elif genre == "j": #elifまたは
            j = input(song)
            jpop.append(j)

        else: #それ以外なら
            print("不正な値です。")
            print("popsongs: ",pop) #コメントとpopリストを表示する。
            print("jpop songs: ",jpop)
    
collect_songs()


