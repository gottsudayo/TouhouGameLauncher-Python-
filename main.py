from tkinter import *
from tkinter import Tk
from tkinter import Listbox
from tkinter import ttk
from tkinter import messagebox
import sys
from pathlib import Path
import getpass
import subprocess

kensaku = Tk()
kensaku.title("東方原作ランチャー ver1.0.0")
kensaku.geometry("300x100")
kensakuchu = ttk.Label(kensaku,text="ディレクトリ検索中",font=(30))
kensakuchu.pack()

def get_game():
    n = gamelist.curselection()
    global selected_game
    selected_game = gamelist.get(n)

user = getpass.getuser()
folder = Path("C:\\Users\\" + user)

games = {"th06.exe":["東方紅魔郷","とうほうこうまきょう","2002"],
         "th07.exe":["東方妖々夢","とうほうようようむ","2003"],
         "th075.exe":["東方萃夢想","とうほうすいむそう","2004"],
         "th08.exe":["東方永夜抄","とうほうえいやしょう","2004"],
         "th09.exe":["東方花映塚","とうほうかえいづか","2005"],
         "th095.exe":["東方文花帖","とうほうぶんかちょう","2005"],
         "th10.exe":["東方風神録","とうほうふうじんろく","2007"],
         "th105.exe":["東方緋想天","とうほうひそうてん","2008"],
         "th11.exe":["東方地霊殿","とうほうちれいでん","2008"],
         "th12.exe":["東方星蓮船","とうほうせいれんせん","2009"],
         "th123.exe":["東方非想天則","とうほうひそうてんそく","2009"],
         "th125.exe":["ダブルスポイラー～東方文花帖","だぶるすぽいらー～とうほうぶんかちょう","2010"],
         "th128.exe":["妖精大戦争～東方三月精","ようせいだいせんそう～とうほうさんげつせい","2010"],
         "th13.exe":["東方神霊廟","とうほうしんれいびょう","2011"],
         "th135.exe":["東方心綺楼","とうほうしんきろう","2013"],
         "th14.exe":["東方輝針城","とうほうきしんじょう","2013"],
         "th143.exe":["弾幕アマノジャク","だんまくあまのじゃく","2014"],
         "th145.exe":["東方深秘録","とうほうしんぴろく","2015"],
         "th15.exe":["東方紺珠伝","とうほうかんじゅでん","2015"],
         "th155.exe":["東方憑依華","とうほうひょういばな","2017"],
         "th16.exe":["東方天空章","とうほうてんくうしょう","2017"],
         "th165.exe":["秘封ナイトメアダイアリー","ひふうないとめあだいありー","2018"],
         "th17.exe":["東方鬼形獣","とうほうきけいじゅう","2019"],
         "th175.exe":["東方剛欲異聞","とうほうごうよくいぶん","2021"],
         "th18.exe":["東方虹龍洞","とうほうこうりゅうどう","2021"],
         "th185.exe":["バレットフィリア達の闇市場","ばれっとふぃりあたちのやみいちば","2022"],
         "th19.exe":["東方獣王園","とうほうじゅうおうえん","2023"]}
Ingames = []
game_name = ["th06.exe","th07.exe","th075.exe","th08.exe","th09.exe","th095.exe","th10.exe","th105.exe","th11.exe","th12.exe","th123.exe","th125.exe","th128.exe","th13.exe","th135.exe","th14.exe","th143.exe","th145.exe","th15.exe","th155.exe","th16.exe","th165.exe","th17.exe","th18.exe","th185.exe","th19.exe"]
check_game = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in folder.glob("**/th[0-9][0-9].exe"):
    Ingames.append(str(i))
    kensaku.update()
    
print(Ingames)

for jogai in Ingames:
    if "AppData" in jogai:
        Ingames.pop(Ingames.index(jogai))
        
print(Ingames)

kensakuchu = ttk.Label(text="インデックス作成中",font=30)
kensaku.update()
kensaku.update_idletasks()
for j in range(len(Ingames)):
    for i in range(len(game_name)):
        if game_name[i] in Ingames[j]:
            check_game[i] = 1

print(check_game)

launcher = Tk()
launcher.title("東方原作ランチャー ver1.0.0")
launcher.geometry("500x500")
launcherLabel = ttk.Label(launcher,text="ゲームを選択してください。",font=30)


gamelist = Listbox(launcher,width=490,font=20,height=15)
item_game_list = []

for k in range(len(check_game)):
    if check_game[k] == 1:
        item_game_list.append(game_name[k])

launch_list = []
for item in item_game_list:
    gamelist.insert(END,games[item])
    launch_list.append(item)

gamelist.bind("<<ListboxSelect>>",get_game)

def launch_game():
    

#game_exe = ttk.Button(launcher,text="ゲームを起動",font=24,command=)

kensaku.destroy()
launcherLabel.pack()
gamelist.pack()

launcher.mainloop()
