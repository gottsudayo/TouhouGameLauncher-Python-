#まずはライブラリのインポートから
from tkinter import *
from tkinter import Tk
from tkinter import Listbox
from tkinter import ttk
from tkinter import messagebox
from pathlib import Path
import getpass
import subprocess
import json
import os
import codecs

#ディレクトリ検索用のウィンドウを生成する。表示処理はこれより50行下
kensaku = Tk()
kensaku.title("東方原作ランチャー ver.1.1.0")
kensaku.geometry("300x100")
kensakuchu = ttk.Label(kensaku,text="ディレクトリ検索中",font=(30))
kensakuchu.pack()

def selected_index():
    selected_game2 = gamelist.curselection()
    global selected_game
    selected_game = selected_game2[0]

user = getpass.getuser()
folder = Path("C:\\Users\\" + user)

file_names = {}
p = Path('data.json')
if os.path.isfile(p.resolve()):
    with open('data.json',mode="r",encoding="utf-8") as f:
        file_names = json.load(f)
else:
    messagebox.showerror("エラー","data.jsonファイルが同じフォルダの中に見つかりません。\n必ず、同じフォルダに配置してください。\nこれより、アプリケーションを終了致します。")
    exit()

#「ゲーム実行ファイル名：東方のゲーム名等」でまとめてあるリスト
#新しいゲームが出たらここを変更する
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
Incustom = []
game_name = ["th06.exe","th07.exe","th075.exe","th08.exe","th09.exe","th095.exe","th10.exe","th105.exe","th11.exe","th12.exe","th123.exe","th125.exe","th128.exe","th13.exe","th135.exe","th14.exe","th143.exe","th145.exe","th15.exe","th155.exe","th16.exe","th165.exe","th17.exe","th18.exe","th185.exe","th19.exe"]
check_game = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in folder.glob("**/th[0-9][0-9].exe"):
    Ingames.append(str(i))
    kensaku.update()
    
print(Ingames)

#AppDataになんか生成される人もいるので除外。なんかバグあり。
jogai = 0
for jogai in Ingames:
    if "AppData" in jogai:
        Ingames.pop(Ingames.index(jogai))
        
print(Ingames)

#custom.exe起動用にリストを作っておく
#新しいゲームが出たらここを変更する
for i in Ingames:
    if "th06.exe" in i:
        Incustom.append([i.replace("th06.exe", "custom.exe"), "th06.exe"])
    if "th07.exe" in i:
        Incustom.append([i.replace("th07.exe", "custom.exe"), "th07.exe"])
    if "th075.exe" in i:
        Incustom.append([i.replace("th075.exe", "custom.exe"),"th075.exe"])
    if "th08.exe" in i:
        Incustom.append([i.replace("th08.exe", "custom.exe"),"th08.exe"])
    if "th09.exe" in i:
        Incustom.append([i.replace("th09.exe", "custom.exe"),"th09.exe"])
    if "th095.exe" in i:
        Incustom.append([i.replace("th095.exe", "custom.exe"),"th095.exe"])
    if "th10.exe" in i:
        Incustom.append([i.replace("th10.exe", "custom.exe"),"th10.exe"])
    if "th105.exe" in i:
        Incustom.append([i.replace("th105.exe", "custom.exe"),"th105.exe"])
    if "th11.exe" in i:
        Incustom.append([i.replace("th11.exe", "custom.exe"),"th11.exe"])
    if "th12.exe" in i:
        Incustom.append([i.replace("th12.exe", "custom.exe"),"th12.exe"])
    if "th123.exe" in i:
        Incustom.append([i.replace("th123.exe", "custom.exe"),"th123.exe"])
    if "th125.exe" in i:
        Incustom.append([i.replace("th125.exe", "custom.exe"),"th125.exe"])
    if "th128.exe" in i:
        Incustom.append([i.replace("th128.exe", "custom.exe"),"th128.exe"])
    if "th13.exe" in i:
        Incustom.append([i.replace("th13.exe", "custom.exe"),"th13.exe"])
    if "th135.exe" in i:
        Incustom.append([i.replace("th135.exe", "custom.exe"),"th135.exe"])
    if "th14.exe" in i:
        Incustom.append([i.replace("th14.exe", "custom.exe"),"th14.exe"])
    if "th143.exe" in i:
        Incustom.append([i.replace("th143.exe", "custom.exe"),"th143.exe"])
    if "th145.exe" in i:
        Incustom.append([i.replace("th145.exe", "custom.exe"),"th145.exe"])
    if "th15.exe" in i:
        Incustom.append([i.replace("th15.exe", "custom.exe"),"th15.exe"])
    if "th155.exe" in i:
        Incustom.append([i.replace("th155.exe", "custom.exe"),"th155.exe"])
    if "th16.exe" in i:
        Incustom.append([i.replace("th16.exe", "custom.exe"),"th16.exe"])
    if "th165.exe" in i:
        Incustom.append([i.replace("th165.exe", "custom.exe"),"th165.exe"])
    if "th17.exe" in i:
        Incustom.append([i.replace("th17.exe", "custom.exe"),"th17.exe"])
    if "th175.exe" in i:
        Incustom.append([i.replace("th175.exe", "custom.exe"),"th175.exe"])
    if "th18.exe" in i:
        Incustom.append([i.replace("th18.exe", "custom.exe"),"th18.exe"])
    if "th19.exe" in i:
        Incustom.append([i.replace("th19.exe", "custom.exe"),"th19.exe"])

#表示は一瞬だが、インデックス作成時のウィンドウ
kensakuchu = ttk.Label(text="インデックス作成中",font=30)
kensaku.update()
kensaku.update_idletasks()
for j in range(len(Ingames)):
    for i in range(len(game_name)):
        if game_name[i] in Ingames[j]:
            check_game[i] = 1

print(check_game)

#いよいよメインウィンドウを生成
launcher = Tk()
launcher.title("東方原作ランチャー ver.1.1.0")
launcher.geometry("500x410")
launcherLabel = ttk.Label(launcher,text="ゲームを選択してください。",font=30)

#存在するゲームの候補を出すListBox
gamelist = Listbox(launcher,width=490,font=20,height=15)

#PCに存在するゲーム名（実行可能ファイル名）の抽出
item_game_list = []
for k in range(len(check_game)):
    if check_game[k] == 1:
        item_game_list.append(game_name[k])

#Listbox（GUI）に先ほど検索したものを列挙する
launch_list = []
for item in item_game_list:
    gamelist.insert(END,games[item])
    launch_list.append(item)

global result_search_index
result_search_index_games = []
result_search_index_custom = []

#選択されたゲームのファイルの候補を出す
#Ingames：見つかったゲームのディレクトリ
for ll in range(len(launch_list)):
    result_search_index_games.append([])
    for ig in range(len(Ingames)):
        if launch_list[ll] in Ingames[ig]:
            result_search_index_games[ll].append(Ingames[ig])

#選択されたcustom.exeの候補を出す
for ll in range(len(launch_list)):
    for ig in range(len(Ingames)):
        if launch_list[ll] in Ingames[ig]:
            result_search_index_custom.append(Incustom[ig])
            
print(result_search_index_games)
print(result_search_index_custom)

def data_update():
    for i in file_names.values():
        i = i.replace("\\", "\\\\")
    json_data = codecs.open("data.json","w","utf-8")
    json.dump(file_names, json_data, indent=2, ensure_ascii=False)
    json_data.close()
    messagebox.showinfo("メッセージ","データの保存が完了しました。")
    subprocess.Popen([fr"{os.getcwd()}\\restart.bat"])
    exit()

def launch_game():
    #thXX.exeを起動するための処理
    try:
        selected_index()
        if len(result_search_index_games) >= 2:
            launch_game2 = Tk()
            launch_game2.geometry("550x200")
            launch_game2.title("東方原作ランチャー ver.1.1.0")
            
            open_list = []
            open_list_h = []
            
            def open_game():
                try:
                    global selected_game4
                    selected_game4 = launch_game2_list.curselection()
                    open_games = open_list[selected_game4[0]]
                    result = result_search_index_games[selected_game][open_games]
                    print(result)
                    result2 = result
                    #新しいゲームが出たらここを変更する
                    if ("\\th06.exe" in result) == True:
                        result = result.replace('\\th06.exe', '')
                    if ("\\th07.exe" in result) == True:
                        result = result.replace('\\th07.exe', '')
                    if ("\\th075.exe" in result) == True:
                        result = result.replace('\\th075.exe', '')
                    if ("\\th08.exe" in result) == True:
                        result = result.replace('\\th08.exe', '')
                    if ("\\th09.exe" in result) == True:
                        result = result.replace('\\th09.exe', '')
                    if ("\\th095.exe" in result) == True:
                        result = result.replace('\\th095.exe', '')
                    if ("\\th10.exe" in result) == True:
                        result = result.replace('\\th10.exe', '')
                    if ("\\th105.exe" in result) == True:
                        result = result.replace('\\th105.exe', '')
                    if ("\\th11.exe" in result) == True:
                        result = result.replace('\\th11.exe', '')
                    if ("\\th12.exe" in result) == True:
                        result = result.replace('\\th12.exe', '')
                    if ("\\th123.exe" in result) == True:
                        result = result.replace('\\th123.exe', '')
                    if ("\\th125.exe" in result) == True:
                        result = result.replace('\\th125.exe', '')
                    if ("\\th128.exe" in result) == True:
                        result = result.replace('\\th128.exe', '')
                    if ("\\th13.exe" in result) == True:
                        result = result.replace('\\th13.exe', '')
                    if ("\\th135.exe" in result) == True:
                        result = result.replace('\\th135.exe', '')
                    if ("\\th14.exe" in result) == True:
                        result = result.replace('\\th14.exe', '')
                    if ("\\th143.exe" in result) == True:
                        result = result.replace('\\th143.exe', '')
                    if ("\\th145.exe" in result) == True:
                        result = result.replace('\\th145.exe', '')
                    if ("\\th15.exe" in result) == True:
                        result = result.replace('\\th15.exe', '')
                    if ("\\th155.exe" in result) == True:
                        result = result.replace('\\th155.exe', '')
                    if ("\\th16.exe" in result) == True:
                        result = result.replace('\\th16.exe', '')
                    if ("\\th165.exe" in result) == True:
                        result = result.replace('\\th165.exe', '')
                    if ("\\th17.exe" in result) == True:
                        result = result.replace('\\th17.exe', '')
                    if ("\\th175.exe" in result) == True:
                        result = result.replace('\\th175.exe', '')
                    if ("\\th18.exe" in result) == True:
                        result = result.replace('\\th18.exe', '')
                    if ("\\th19.exe" in result) == True:
                        result = result.replace('\\th19.exe', '')
                    print(result2)
                    print(result)
                    launcher.destroy()
                    launch_game2.destroy()
                    subprocess.run(result2,shell=True,cwd=result)
                    exit()
                except TypeError as e:
                    messagebox.showerror("エラー",f"ゲームが選択されておりません。\nTypeError : {e}")
            
            def open_game_cancel():
                launch_game2.destroy()
            
            def rename():
                try:
                    global selected_game4
                    selected_game4 = launch_game2_list.curselection()
                    open_games = open_list[selected_game4[0]]
                    result = result_search_index_games[selected_game][open_games]
                    rename_window = Tk()
                    rename_window.geometry("500x100")
                    rename_window.title("東方原作ランチャー ver.1.1.0")
                    rename_label = Label(rename_window,text="以下のディレクトリの表示名を入力してください。",font=30)
                    rename_label2 = Label(rename_window,text=result)
                    rename_entry = Entry(rename_window,width=490)
                    if result_search_index_games[selected_game][open_games] in file_names:
                        rename_entry.insert(END,file_names[result_search_index_games[selected_game][open_games]])
                    
                    def rename_s():
                        rename_e = rename_entry.get()
                        if len(rename_e) > 0:
                            file_names[result] = rename_e
                            data_update()
                            renames = False
                            rename_window.destroy()
                        elif "\\" in rename_e:
                            messagebox.showerror("エラー","使えない文字が含まれています。\n使えない文字：\\")
                        elif len(rename_e) == 0:
                            messagebox.showerror("エラー","変更する名前を入力してください。")
                    
                    def rename_r():
                        #global selected_game4
                        #selected_game4 = launch_game2_list.curselection()
                        #open_games = open_list[selected_game4[0]]
                        #result = result_search_index_games[selected_game][open_games]
                        hyouji = open_list_h[open_games]
                        question = messagebox.askquestion("表示名リセット",f"表示名「{hyouji}」を本当にリセットしますか？")
                        if question == 'yes':
                            file_names.pop(result_search_index_games[selected_game][open_games])
                            data_update()
                    
                    def rename_c():
                        renames = False
                        rename_window.destroy()
                    
                    rename_setting = Button(rename_window,text="変更を適用",font=30,command=rename_s)
                    rename_reset = Button(rename_window,text="表示名をリセット",font=30,command=rename_r)
                    rename_cancel = Button(rename_window,text="キャンセル",font=30,command=rename_c)
                    
                    rename_label.pack()
                    rename_label2.pack()
                    rename_entry.pack()
                    rename_setting.pack(side=LEFT)
                    rename_reset.pack(side=LEFT)
                    rename_cancel.pack(side=RIGHT)
                    rename_window.update()
                    launch_game2.update()
                except IndexError as e:
                    messagebox.showerror("エラー",f"ゲームが選択されておりません。\nIndexError : {e}")
            
            launch_game2_label = ttk.Label(launch_game2,text="該当する項目が複数見つかりました。\nどのディレクトリのゲームを起動するか選択してください。",font=30)
            launch_game2_list = Listbox(launch_game2,width=490,font=20,height=5)
            for i in range(len(result_search_index_games[selected_game])):
                if result_search_index_games[selected_game][i] in file_names:
                    launch_game2_list.insert(END,file_names[result_search_index_games[selected_game][i]])
                    open_list_h.append(file_names[result_search_index_games[selected_game][i]])
                else:
                    launch_game2_list.insert(END,result_search_index_games[selected_game][i])
                    open_list_h.append(result_search_index_games[selected_game][i])
                open_list.append(i)
            launch_game2_open = Button(text="ゲーム開始",font=30,command=open_game)
            launch_game2_rename = Button(text="表示名を編集",font=30,command=rename)
            launch_game2_cancel = Button(text="キャンセル",font=30,command=open_game_cancel)
            launch_game2_label.pack()
            launch_game2_list.pack()
            launch_game2_open.pack(side=LEFT)
            launch_game2_rename.pack(side=LEFT)
            launch_game2_cancel.pack(side=RIGHT)
            launch_game2.update()
        elif len(result_search_index_games) == 1:
            result = result_search_index_games[0][0]
            result2 = result
            print(result2)
            print(result)
            print("\\th07.exe" in result)
            if ("\\th06.exe" in result) == True:
                result = result.replace('\\th06.exe', '')
            if ("\\th07.exe" in result) == True:
                result = result.replace('\\th07.exe', '')
            if ("\\th075.exe" in result) == True:
                result = result.replace('\\th075.exe', '')
            if ("\\th08.exe" in result) == True:
                result = result.replace('\\th08.exe', '')
            if ("\\th09.exe" in result) == True:
                result = result.replace('\\th09.exe', '')
            if ("\\th095.exe" in result) == True:
                result = result.replace('\\th095.exe', '')
            if ("\\th10.exe" in result) == True:
                result = result.replace('\\th10.exe', '')
            if ("\\th105.exe" in result) == True:
                result = result.replace('\\th105.exe', '')
            if ("\\th11.exe" in result) == True:
                result = result.replace('\\th11.exe', '')
            if ("\\th12.exe" in result) == True:
                result = result.replace('\\th12.exe', '')
            if ("\\th123.exe" in result) == True:
                result = result.replace('\\th123.exe', '')
            if ("\\th125.exe" in result) == True:
                result = result.replace('\\th125.exe', '')
            if ("\\th128.exe" in result) == True:
                result = result.replace('\\th128.exe', '')
            if ("\\th13.exe" in result) == True:
                result = result.replace('\\th13.exe', '')
            if ("\\th135.exe" in result) == True:
                result = result.replace('\\th135.exe', '')
            if ("\\th14.exe" in result) == True:
                result = result.replace('\\th14.exe', '')
            if ("\\th143.exe" in result) == True:
                result = result.replace('\\th143.exe', '')
            if ("\\th145.exe" in result) == True:
                result = result.replace('\\th145.exe', '')
            if ("\\th15.exe" in result) == True:
                result = result.replace('\\th15.exe', '')
            if ("\\th155.exe" in result) == True:
                result = result.replace('\\th155.exe', '')
            if ("\\th16.exe" in result) == True:
                result = result.replace('\\th16.exe', '')
            if ("\\th165.exe" in result) == True:
                result = result.replace('\\th165.exe', '')
            if ("\\th17.exe" in result) == True:
                result = result.replace('\\th17.exe', '')
            if ("\\th175.exe" in result) == True:
                result = result.replace('\\th175.exe', '')
            if ("\\th18.exe" in result) == True:
                result = result.replace('\\th18.exe', '')
            if ("\\th19.exe" in result) == True:
                result = result.replace('\\th19.exe', '')
            print(result2)
            print(result)
            launcher.destroy()
            subprocess.run(result2,shell=True,cwd=result)
            exit()
        elif len(result_search_index_games) == 0:
            messagebox.showerror("エラー",("指定したゲームが「C:\\Users\\" + user + "」内から見つかりませんでした。"))
    except TypeError as e:
        messagebox.showerror("エラー",f"ゲームが選択されておりません。\nTypeError : {e}")

game_exe = Button(launcher,text="ゲームを起動",command=launch_game,font=20)

kensaku.destroy()
launcherLabel.pack()
gamelist.pack()
game_exe.pack()

launcher.mainloop()
