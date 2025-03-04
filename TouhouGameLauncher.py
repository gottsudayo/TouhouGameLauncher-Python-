"""管理人用メモ
1.東方の新しい原作が出たら「#新しいゲームが出たらここを変更する」を検索にかけてそれぞれ追加する
2.バグはさっさと潰す
"""
#まずはライブラリのインポートから
from tkinter import *
from tkinter import Tk
from tkinter import Listbox
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from pathlib import Path
import getpass
import subprocess
import json
import os
import codecs
import sys
from time import sleep
import webbrowser
import base64
import numpy
from PIL import Image, ImageTk

#続いていろいろな関数の定義
global dire
global setting
dire = []
setting = []
def exit_py():
    app = False
    sys.exit()

messages = {"Japanese":[
    "ディレクトリ検索中",
    "東方原作ランチャー ver.2.0.2",
    "ゲームを選択してください。",
    "ゲームを起動",
    "custom.exeを起動",
    "リストを更新",
    "メッセージ",
    "データの保存が完了しました。",
    "エラー",
    "ゲームが選択されておりません。\nTypeError : ",
    "以下のパスの表示名を入力してください。",
    "使えない文字が含まれています。\n使えない文字：\\",
    "変更する名前を入力してください。",
    "表示名リセット",
    "次の表示名を本当にリセットしますか？\n",
    "",
    "変更を適用",
    "表示名をリセット",
    "キャンセル",
    "該当する項目が複数見つかりました。\nどの階層のゲームを起動するか選択してください。",
    "ゲーム開始",
    "表示名を編集",
    "指定したゲームが以下ディレクトリから見つかりませんでした。\n",
    "custom.exeが見つかりませんでした。同じ階層に入れてください。\n正しい位置：",
    "該当する項目が複数見つかりました。\nどの階層のゲームのcustom.exeを起動するか選択してください。",
    "custom.exeを開く",
    "指定したcustom.exeが以下ディレクトリから見つかりませんでした。\n",
    "設定",
    "参照ディレクトリ設定",
    "検索するフォルダを選択",
    "ディレクトリが選択されておりません。\nIndexError : ",
    "追加",
    "削除",
    "閉じる",
    "設定の保存が完了しました。",
    "参照ディレクトリ設定",
    "設定を保存",
    "東方原作ランチャー",
    "ゲームを起動",
    "custom.exeを起動",
    "リストを更新",
    "終了",
    "このアプリについて",
    "ソースコード",
    "公式Wiki",
    "お問い合わせ",
    "ヘルプ",
    "ファイル"
    ],
            "English":[
                "Searching Directory...",
                "Touhou Game Launcher ver2.0.2",
                "Please select a game.",
                "Launch game",
                "Launch custom.exe",
                "Reload",
                "Message",
                "Completed saving data.",
                "Error",
                "You didn't select a game.\nTypeError : ",
                "Please enter this display name.",
                "Invalid text is in this.\nInvalid text:\\",
                "Please enter this display name.",
                "Reset display name",
                "Will you reset display name?",
                "",
                "Apply changes",
                "Reset display name",
                "Cancel",
                "Some results were found.\nWhich one will you launch?",
                "Start",
                "Change display name",
                "This game was not found in them.\n",
                "This custom.exe was not found.\nIs this custom.exe went in same directory?\nRight place:",
                "Some results were found.\nWhich one will you launch?",
                "Open custom.exe",
                "This custom.exe was not found in them.\n",
                "Settings",
                "Where to find game settings",
                "Select folder",
                "You didn't select directory.\nIndexError : ",
                "Append",
                "Delete",
                "Close",
                "Settings was saved.",
                "Where to find game settings",
                "Save settings",
                "Touhou Game Launcher",
                "Launch game",
                "Launch custom.exe",
                "Reload list",
                "Exit",
                "What is this application",
                "Sorce code",
                "Official wiki",
                "Contact us",
                "Help",
                "File",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
        "Korean":
    [
        "파일을 검색고 있어요.",
        "토우호우 프로젝트의 론쳐 ver2.0.2",
        "게임을 선택한.",
        "게임 시작",
        "custom.exe 시작",
        "리스트을 업데이트",
        "메시지",
        "데이터를 저장했습니다.",
        "오류",
        "게임가 안 선택됨.\nTypeError : ",
        "이 피일의 표시 이름을 입력하세요.",
        "이 문자를 사용할 수 없습니다.\n \\",
        "이 게임은 여기에서 찾을 수 없습니다.",
        "이 custom.exe는 찾을 수 없습니다.\n이 custom.exe는 같은 디렉토리에 있었나요? 올바른 위치:",
        "몇 가지 결과가 발견되었습니다. 어떤 것을 실행하시겠습니까?",
        "custom.exe 열기",
        "이 custom.exe는 여기에서 찾을 수 없습니다.",
        "설정",
        "게임을 찾을 수 있는 위치",
        "폴더 선택",
        "디렉토리를 선택하지 않았습니다.",
        "추가",
        "삭제",
        "닫기",
        "설정이 저장되었습니다.",
        "게임 설정을 찾을 수 있는 위치",
        "설정 저장",
        "토우호우 프로젝트의 론쳐",
        "게임 시작",
        "custom.exe 시작",
        "목록 다시 로드",
        "종료",
        "이 애플리케이션은 무엇입니까",
        "소스 코드",
        "공식 위키",
        "문의처",
        "도움말",
        "파일"
    ]}

def change_Japanese():
    global language
    language = "Japanese"
    setting[1] = "Japanese"
    data_json_update("Complete change language\nApplication will be restarted.")
def change_English():
    global language
    language = "English"
    setting[1] = "English"
    data_json_update("Complete change language\nApplication will be restarted.")

def change_Korean():
    global language
    language = "Korean"
    setting[1] = "Korean"
    data_json_update("Complete change language\nApplication will be restarted.")

def open_sorce():
    webbrowser.open("https://github.com/gottsudayo/TouhouGameLauncher-Python-")

def open_wiki():
    webbrowser.open("https://github.com/gottsudayo/TouhouGameLauncher-Python-/wiki")

def open_otoiawase():
    webbrowser.open("https://github.com/gottsudayo/TouhouGameLauncher-Python-/wiki/%E3%81%8A%E5%95%8F%E3%81%84%E5%90%88%E3%82%8F%E3%81%9B")

def launcher_widget():
    global launcher
    launcher = Tk()
    launcher.title(messages[language][1])
    launcher.geometry("500x410")
    launcher.iconbitmap(default="icon.ico")
    launcherLabel = ttk.Label(launcher,text=messages[language][2],font=30)
    
    #存在するゲームの候補を出すListBox
    gamelist_var = StringVar(launcher,value=game_list)
    gamelist = Listbox(launcher,width=490,font=20,height=15,listvariable=gamelist_var)
    gamelist_var.set(game_list)
    
    game_exe = Button(launcher,text=messages[language][38],command=launch_game,font=20)
    custom_exe = Button(launcher,text=messages[language][39],command=launch_custom,font=20)
    list_update = Button(launcher,text=messages[language][40],command=reload,font=20)
    menubar = Menu(launcher)
    launcher.config(menu=menubar)
    
    menu_file = Menu(menubar,tearoff=0)
    menu_file.add_command(label=messages[language][27],command=settings)
    menu_file.add_separator()
    menu_file.add_command(label=messages[language][41],command=exit_py)
    menubar.add_cascade(label=messages[language][47],menu=menu_file)
    
    menu_language = Menu(menubar,tearoff=0)
    menu_language.add_command(label="日本語",command=change_Japanese)
    menu_language.add_command(label="English",command=change_English)
    menu_language.add_command(label="한국어",command=change_Korean)
    menubar.add_cascade(label="languages",menu=menu_language)
    
    menu_help = Menu(menubar,tearoff=0)
    menu_help.add_command(label=messages[language][42],command=app_info)
    menu_help.add_separator()
    menu_help.add_command(label=messages[language][43],command=open_sorce)
    menu_help.add_command(label=messages[language][44],command=open_wiki)
    menu_help.add_command(label=messages[language][45],command=open_otoiawase)
    menubar.add_cascade(label=messages[language][46],menu=menu_help)
    
    launcherLabel.pack()
    gamelist.pack()
    game_exe.pack(side=LEFT)
    custom_exe.pack(side=LEFT)
    list_update.pack(side=LEFT)
    
    launcher.update()
    launcher.lift()
    
    launcher.mainloop()

#data.jsonの読み込み
data = []
p = Path('data.json')
if os.path.isfile(p.resolve()):
    try:
        with open('data.json',mode="r",encoding="utf-8") as f:
            data = json.load(f)
        global file_names
        file_names = data[0]
        dire = data[1]
        setting = data[2]
    except TypeError as e:
        messagebox.showerror("エラー",f"data.jsonファイルの読み込みに失敗しました。\nランチャーの再ダウンロードをするか、data.jsonの中身を元に戻してください。\nTypeError : {e}")
        exit_py()
else:
    messagebox.showerror("エラー","data.jsonファイルが同じフォルダの中に見つかりません。\n必ず、同じフォルダに配置してください。\nこれより、アプリケーションを終了致します。")
    exit_py()

def data_json_update(message):
    data = [{},[],[]]
    data[0] = file_names
    data[1] = dire
    data[2] = setting
    with open("data.json","w") as f:
        json.dump(data,f)
    if message == "":
        messagebox.showinfo(messages[language][6],messages[language][7])
    elif message != None:
        messagebox.showinfo(messages[language][6],message)
    reload()

#direのディレクトリが存在していればスルー、1つでも存在していないものがあれば自動的にリロードするため、dataのdireを初期化。
for i in dire:
    if os.path.exists(i) == False:
        print(os.path.exists(i))
        print("ディレクトリ：" + i + "、非存在")
        print("リストを初期化")
        dire = []
        data[1] = dire
        with open("data.json","w") as f:
            json.dump(data,f)
        break
    else:
        print(os.path.exists(i))
        print("ディレクトリ：" + i + "、存在確認")

user = getpass.getuser()

if len(setting[0]) == 0:
    setting[0].append("C:\\Users\\" + user)
    data[2] = setting
    with open("data.json","w") as f:
        json.dump(data, f)

#dataからsettingのlanguageを検出
global language
if len(data[2]) == 2:
    if data[2][1] != "":
        language = data[2][1]
    else:
        os_lang = os.environ['LANG']
        if "ja" in os_lang:
            language = "Japanese"
        elif "ko" in os_lang:
            language = "Korean"
        else:
            language = "English"
    
    setting.append(language)
    data[2] = setting
    with open("data.json","w") as f:
        json.dump(data,f)
else:
    os_lang = os.environ['LANG']
    if "ja" in os_lang:
        language = "Japanese"
    elif "ko" in os_lang:
        language = "Korean"
    else:
        language = "English"
    
    setting.append(language)
    data[2] = setting
    with open("data.json","w") as f:
        json.dump(data,f)

def selected_index():
    selected_game2 = gamelist.curselection()
    global selected_game
    selected_game = selected_game2[0]
    
global app
app = True

#検索をするためのとても重要な関数
def file_load():
    #様々な変数のグローバル化
    global Ingames
    global kensaku
    global data
    
    #data.jsonの読み込み
    data = []
    p = Path('data.json')
    if os.path.isfile(p.resolve()):
        try:
            with open('data.json',mode="r",encoding="utf-8") as f:
                data = json.load(f)
            dire = []
            setting = []
            file_names = data[0]
            dire = data[1]
            setting = data[2]
            language = setting[1]
        except TypeError as e:
            messagebox.showerror("エラー",f"data.jsonファイルの読み込みに失敗しました。\nランチャーの再ダウンロードをするか、data.jsonの中身を元に戻してください。\nTypeError : {e}")
            exit_py()
    else:
        messagebox.showerror("エラー","data.jsonファイルが同じフォルダの中に見つかりません。\n必ず、同じフォルダに配置してください。\nこれより、アプリケーションを終了致します。")
        exit_py()
    
    #ディレクトリ検索用のウィンドウを生成する。
    kensaku = Tk()
    kensaku.title(messages[language][1])
    kensaku.geometry("300x100")
    kensaku.iconbitmap(default="icon.ico")
    kensakuchu = ttk.Label(kensaku,text=messages[language][0],font=30)
    kensakuchu.pack()
    kensaku.update()
    kensaku.lift()
    Ingames = []
    kensaku.update()
    
    for j in setting[0]:
        folder = Path(j)
        print("ディレクトリ「" + str(folder) + "」を探索中")
        for i in folder.glob("**/th[0-9][0-9].exe"):
            Ingames.append(str(i))
        

def load():
    #様々な変数のグローバル化2
    global game_list
    global file_names
    global result_search_index
    global result_search_index_games
    global result_search_index_custom
    global Incustom
    global check_game
    global dire
    
    Incustom = []
    check_game = [0 for i in range(26)]
    #AppDataになんか生成される人もいるので除外。なんかバグあり。
    jogai = 0
    for jogai in Ingames:
        if "AppData" in jogai:
            Ingames.pop(Ingames.index(jogai))
    
    
    #custom.exe起動用にリストを作っておく
    #新しいゲームが出たらここを変更する
    for i in Ingames:
        if "th06.exe" in i:
            Incustom.append(i.replace("th06.exe", "custom.exe"))
        if "th07.exe" in i:
            Incustom.append(i.replace("th07.exe", "custom.exe"))
        if "th075.exe" in i:
            Incustom.append(i.replace("th075.exe", "custom.exe"))
        if "th08.exe" in i:
            Incustom.append(i.replace("th08.exe", "custom.exe"))
        if "th09.exe" in i:
            Incustom.append(i.replace("th09.exe", "custom.exe"))
        if "th095.exe" in i:
            Incustom.append(i.replace("th095.exe", "custom.exe"))
        if "th10.exe" in i:
            Incustom.append(i.replace("th10.exe", "custom.exe"))
        if "th105.exe" in i:
            Incustom.append(i.replace("th105.exe", "custom.exe"))
        if "th11.exe" in i:
            Incustom.append(i.replace("th11.exe", "custom.exe"))
        if "th12.exe" in i:
            Incustom.append(i.replace("th12.exe", "custom.exe"))
        if "th123.exe" in i:
            Incustom.append(i.replace("th123.exe", "custom.exe"))
        if "th125.exe" in i:
            Incustom.append(i.replace("th125.exe", "custom.exe"))
        if "th128.exe" in i:
            Incustom.append(i.replace("th128.exe", "custom.exe"))
        if "th13.exe" in i:
            Incustom.append(i.replace("th13.exe", "custom.exe"))
        if "th135.exe" in i:
            Incustom.append(i.replace("th135.exe", "custom.exe"))
        if "th14.exe" in i:
            Incustom.append(i.replace("th14.exe", "custom.exe"))
        if "th143.exe" in i:
            Incustom.append(i.replace("th143.exe", "custom.exe"))
        if "th145.exe" in i:
            Incustom.append(i.replace("th145.exe", "custom.exe"))
        if "th15.exe" in i:
            Incustom.append(i.replace("th15.exe", "custom.exe"))
        if "th155.exe" in i:
            Incustom.append(i.replace("th155.exe", "custom.exe"))
        if "th16.exe" in i:
            Incustom.append(i.replace("th16.exe", "custom.exe"))
        if "th165.exe" in i:
            Incustom.append(i.replace("th165.exe", "custom.exe"))
        if "th17.exe" in i:
            Incustom.append(i.replace("th17.exe", "custom.exe"))
        if "th175.exe" in i:
            Incustom.append(i.replace("th175.exe", "custom.exe"))
        if "th18.exe" in i:
            Incustom.append(i.replace("th18.exe", "custom.exe"))
        if "th19.exe" in i:
            Incustom.append(i.replace("th19.exe", "custom.exe"))
    
    for j in range(len(Ingames)):
        for i in range(len(game_name)):
            if game_name[i] in Ingames[j]:
                check_game[i] = 1
    
    #PCに存在するゲーム名（実行可能ファイル名）の抽出
    item_game_list = []
    for k in range(len(check_game)):
        if check_game[k] == 1:
            item_game_list.append(game_name[k])
    
    #Listbox（GUI）に先ほど検索したものを列挙する
    launch_list = []
    game_list = []
    for item in item_game_list:
        launch_list.append(item)
        game_list.append(games[language][item])
    
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
        result_search_index_custom.append([])
        for ig in range(len(Ingames)):
            if launch_list[ll] in Ingames[ig]:
                result_search_index_custom[ll].append(Incustom[ig])
    
    #direに要素を追加
    dire = []
    for i in Ingames:
        dire.append(i)
    data[1] = dire
    with open('data.json',"w") as f:
        json.dump(data,f)
    

def reload():
    #ウィンドウlauncherを閉じる
    launcher.destroy()
    #data.jsonの読み込み
    global data
    data = []
    p = Path('data.json')
    if os.path.isfile(p.resolve()):
        try:
            with open('data.json',mode="r",encoding="utf-8") as f:
                data = json.load(f)
            dire = []
            setting = []
            file_names = data[0]
            dire = data[1]
            setting = data[2]
            language = setting[1]
        except TypeError as e:
            messagebox.showerror("エラー",f"data.jsonファイルの読み込みに失敗しました。\nランチャーの再ダウンロードをするか、data.jsonの中身を元に戻してください。\nTypeError : {e}")
            exit_py()
    else:
        messagebox.showerror("エラー","data.jsonファイルが同じフォルダの中に見つかりません。\n必ず、同じフォルダに配置してください。\nこれより、アプリケーションを終了致します。")
        exit_py()
    
    #ディレクトリ検索
    file_load()
    #インデックス作成
    load()
    #オブジェクト配置
    kensaku.destroy()
    launcher_widget()


#「ゲーム実行ファイル名：東方のゲーム名等」でまとめてあるリスト
#新しいゲームが出たらここを変更する
games = {"Japanese":
    {"th06.exe":["東方紅魔郷　とうほうこうまきょう","2002"],
        "th07.exe":["東方妖々夢　とうほうようようむ","2003"],
        "th075.exe":["東方萃夢想　とうほうすいむそう","2004"],
        "th08.exe":["東方永夜抄　とうほうえいやしょう","2004"],
        "th09.exe":["東方花映塚　とうほうかえいづか","2005"],
        "th095.exe":["東方文花帖　とうほうぶんかちょう","2005"],
        "th10.exe":["東方風神録　とうほうふうじんろく","2007"],
        "th105.exe":["東方緋想天　とうほうひそうてん","2008"],
        "th11.exe":["東方地霊殿　とうほうちれいでん","2008"],
        "th12.exe":["東方星蓮船　とうほうせいれんせん","2009"],
        "th123.exe":["東方非想天則　とうほうひそうてんそく","2009"],
        "th125.exe":["ダブルスポイラー～東方文花帖　だぶるすぽいらー～とうほうぶんかちょう","2010"],
        "th128.exe":["妖精大戦争～東方三月精　ようせいだいせんそう～とうほうさんげつせい","2010"],
        "th13.exe":["東方神霊廟　とうほうしんれいびょう","2011"],
        "th135.exe":["東方心綺楼　とうほうしんきろう","2013"],
        "th14.exe":["東方輝針城　とうほうきしんじょう","2013"],
        "th143.exe":["弾幕アマノジャク　だんまくあまのじゃく","2014"],
        "th145.exe":["東方深秘録　とうほうしんぴろく","2015"],
        "th15.exe":["東方紺珠伝　とうほうかんじゅでん","2015"],
        "th155.exe":["東方憑依華　とうほうひょういばな","2017"],
        "th16.exe":["東方天空章　とうほうてんくうしょう","2017"],
        "th165.exe":["秘封ナイトメアダイアリー　ひふうないとめあだいありー","2018"],
        "th17.exe":["東方鬼形獣　とうほうきけいじゅう","2019"],
        "th175.exe":["東方剛欲異聞　とうほうごうよくいぶん","2021"],
        "th18.exe":["東方虹龍洞　とうほうこうりゅうどう","2021"],
        "th185.exe":["バレットフィリア達の闇市場　ばれっとふぃりあたちのやみいちば","2022"],
        "th19.exe":["東方獣王園　とうほうじゅうおうえん","2023"]
        },
        "English":
            {
                "th06.exe":["Touhou Koumakyo","2002"],
                "th07.exe":["Touhou Youyoumu","2003"],
                "th075.exe":["Touhou Suimusou","2004"],
                "th08.exe":["Touhou Eiyasho","2004"],
                "th09.exe":["Touhou Kaeizuka","2005"],
                "th095.exe":["Touhou Bunkacho","2005"],
                "th10.exe":["Touhou Fujinroku","2007"],
                "th105.exe":["Touhou Hisouten","2008"],
                "th11.exe":["Touhou Chireiden","2008"],
                "th12.exe":["Touhou Seirensen","2009"],
                "th123.exe":["Touhou Hisoutensoku","2009"],
                "th125.exe":["Double Spoiler ~ Touhou Bunkacho","2010"],
                "th128.exe":["Yousei Daisensou ~ Touhou Sangetsusei","2010"],
                "th13.exe":["Touhou Shinreibyo","2011"],
                "th135.exe":["Touhou Shinkiro","2013"],
                "th14.exe":["Touhou Kishinjo","2013"],
                "th143.exe":["Danmaku Amanojaku","2014"],
                "th145.exe":["Touhou Shinpiroku","2015"],
                "th15.exe":["Touhou Kanjuden","2015"],
                "th155.exe":["Touhou Hyoibana","2017"],
                "th16.exe":["Touhou Tenkusho","2017"],
                "th165.exe":["Hifu Nightmare Diary","2018"],
                "th17.exe":["Touhou Kikeiju","2019"],
                "th175.exe":["Touhou Goyokuibun","2021"],
                "th18.exe":["Touhou Kouryudo","2021"],
                "th185.exe":["Black Market of Bulletphilia","2022"],
                "th19.exe":["Touhou Juohen","2023"]
            },
            "Korean":
                {
                    "th06.exe":["동방 코마쿄","2002"],
                    "th07.exe":["동방 요요무","2003"],
                    "th075.exe":["동방 스이무소우","2004"],
                    "th08.exe":["동방 에이야쇼","2004"],
                    "th09.exe":["동방 카에이즈카","2005"],
                    "th095.exe":["동방 문화초","2005"],
                    "th10.exe":["동방 후지로쿠","2007"],
                    "th105.exe":["동방 히소텐","2008"],
                    "th11.exe":["동방 치레이덴","2008"],
                    "th12.exe":["동방 사이렌센","2009"],
                    "th123.exe":["동방 히소텐소쿠","2009"],
                    "th125.exe":["더블 스포일러 ~ 동방 문화초","2010"],
                    "th128.exe":["요우세이 다이센소우 ~ 동방 산게츠세이","2010"],
                    "th13.exe":["동방 신레이요","2011"],
                    "th135.exe":["동방 신키로","2013"],
                    "th14.exe":["동방 키신조","2013"],
                    "th143.exe":["단마쿠 아마노자쿠","2014"],
                    "th145.exe":["동방 신피로쿠","2015"],
                    "th15.exe":["동방 칸쥬덴","2015"],
                    "th155.exe":["동방효바나","2017"],
                    "th16.exe":["동방천공","2017"],
                    "th165.exe":["히푸 악몽 일기","2018"],
                    "th17.exe":["동방 키케이주","2019"],
                    "th175.exe":["동방 코요쿠이분","2021"],
                    "th18.exe":["동방 고류도","2021"],
                    "th185.exe":["불렛필리아 블랙 시장","2022"],
                    "th19.exe":["동방 주오헨","2023"]
                }
            }

#新しいゲームが出たらここを変更する
game_name = ["th06.exe","th07.exe","th075.exe","th08.exe","th09.exe","th095.exe","th10.exe","th105.exe","th11.exe","th12.exe","th123.exe","th125.exe","th128.exe","th13.exe","th135.exe","th14.exe","th143.exe","th145.exe","th15.exe","th155.exe","th16.exe","th165.exe","th17.exe","th18.exe","th185.exe","th19.exe"]

#ここで読み込み関数実行
if len(dire) == 0:
    file_load()
    load()
    kensaku.destroy()
else:
    global Ingames
    Ingames = []
    for i in dire:
        Ingames.append(i)
    load()

def launch_game():
    #thXX.exeを起動するための処理
    try:
        selected_index()
        if len(result_search_index_games[selected_game]) >= 2:
            #ファイル候補を出す
            global launch_game2
            launch_game2 = Tk()
            launch_game2.geometry("550x200")
            launch_game2.title(messages[language][1])
            launch_game2.iconbitmap(default="icon.ico")
            
            open_list = []
            open_list_h = []
            
            def open_game():
                try:
                    global selected_game4
                    selected_game4 = launch_game2_list.curselection()
                    open_games = open_list[selected_game4[0]]
                    result = result_search_index_games[selected_game][open_games]
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
                    launcher.destroy()
                    launch_game2.destroy()
                    print("アプリを開く：「" + result2 + "」、「" + result + "」の上で")
                    subprocess.run(result2,shell=True,cwd=result)
                    exit_py()
                except TypeError as e:
                    error = messages[language][9] + e
                    messagebox.showerror(messages[language][8],error)
            
            def open_game_cancel():
                launch_game2.destroy()
            
            def rename():
                try:
                    global selected_game4
                    global rename_window
                    selected_game4 = launch_game2_list.curselection()
                    open_games = open_list[selected_game4[0]]
                    result = result_search_index_games[selected_game][open_games]
                    rename_window = Tk()
                    rename_window.geometry("500x100")
                    rename_window.title(messages[language][1])
                    rename_window.iconbitmap(default="icon.ico")
                    rename_label = Label(rename_window,text=messages[language][10],font=30)
                    rename_label2 = Label(rename_window,text=result)
                    rename_entry = Entry(rename_window,width=490)
                    if result_search_index_games[selected_game][open_games] in file_names:
                        rename_entry.insert(END,file_names[result_search_index_games[selected_game][open_games]])
                    
                    def rename_s():
                        rename_e = rename_entry.get()
                        if len(rename_e) > 0:
                            file_names[result] = rename_e
                            data_json_update("")
                            renames = False
                            rename_window.destroy()
                        elif "\\" in rename_e:
                            messagebox.showerror(messages[language][8],messages[language][11])
                        elif len(rename_e) == 0:
                            messagebox.showerror(messages[language][8],messages[language][12])
                    
                    def rename_r():
                        hyouji = open_list_h[open_games]
                        msg = messages[language][14] + hyouji
                        question = messagebox.askquestion(messages[language][13],msg)
                        if question == 'yes':
                            file_names.pop(result_search_index_games[selected_game][open_games])
                            data_json_update("")
                    
                    def rename_c():
                        renames = False
                        rename_window.destroy()
                    
                    rename_setting = Button(rename_window,text=messages[language][16],font=30,command=rename_s)
                    rename_reset = Button(rename_window,text=messages[language][17],font=30,command=rename_r)
                    rename_cancel = Button(rename_window,text=messages[language][18],font=30,command=rename_c)
                    
                    rename_label.pack()
                    rename_label2.pack()
                    rename_entry.pack()
                    rename_setting.pack(side=LEFT)
                    rename_reset.pack(side=LEFT)
                    rename_cancel.pack(side=RIGHT)
                    rename_window.update()
                    launch_game2.update()
                except IndexError as e:
                    error = messages[language][9] + e
                    messagebox.showerror(messages[language][8],error)
            
            launch_game2_label = ttk.Label(launch_game2,text=messages[language][19],font=30)
            launch_game2_list = Listbox(launch_game2,width=490,font=20,height=5)
            for i in range(len(result_search_index_games[selected_game])):
                if result_search_index_games[selected_game][i] in file_names:
                    launch_game2_list.insert(END,file_names[result_search_index_games[selected_game][i]])
                    open_list_h.append(file_names[result_search_index_games[selected_game][i]])
                else:
                    launch_game2_list.insert(END,result_search_index_games[selected_game][i])
                    open_list_h.append(result_search_index_games[selected_game][i])
                open_list.append(i)
            launch_game2_open = Button(launch_game2,text=messages[language][20],font=30,command=open_game)
            launch_game2_rename = Button(launch_game2,text=messages[language][21],font=30,command=rename)
            launch_game2_cancel = Button(launch_game2,text=messages[language][18],font=30,command=open_game_cancel)
            launch_game2_label.pack()
            launch_game2_list.pack()
            launch_game2_open.pack(side=LEFT)
            launch_game2_rename.pack(side=LEFT)
            launch_game2_cancel.pack(side=RIGHT)
            launch_game2.update()
        elif len(result_search_index_games[selected_game]) == 1:
            print(result_search_index_games[selected_game][0])
            result = result_search_index_games[selected_game][0]
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
            launcher.destroy()
            print("アプリを開く：「" + result2 + "」、「" + result + "」の上で")
            subprocess.run(result2,shell=True,cwd=result)
            exit_py()
        elif len(result_search_index_games[selected_game]) == 0:
            error = messages[language][22]
            for i in setting[0]:
                error = error + i + ",\n"
            messagebox.showerror(messages[language][8],error)
    except TypeError as e:
        error = messages[language][9] + e
        messagebox.showerror(messages[language][8],error)

def launch_custom():
    try:
        selected_index()
        if len(result_search_index_custom[selected_game]) >= 2:
            #ファイル候補を出す
            global launch_custom2
            launch_custom2 = Tk()
            launch_custom2.geometry("550x200")
            launch_custom2.title(messages[language][1])
            launch_custom2.iconbitmap(default="icon.ico")
            open_list = []
            open_list_h = []
            
            def open_custom():
                try:
                    global selected_game4
                    selected_game4 = launch_custom2_list.curselection()
                    open_games = open_list[selected_game4[0]]
                    result = result_search_index_custom[selected_game][open_games]
                    result2 = result
                    result = result.replace("\\custom.exe","")
                    launch_custom2.destroy()
                    print("アプリを開く：「" + result2 + "」、「" + result + "」の上で")
                    if os.path.isfile(result2):
                        print("アプリを開く：「" + result2 + "」、「" + result + "」の上で")
                        subprocess.run(result2,shell=True,cwd=result)
                    else:
                        error = messages[language][23] + result
                        messagebox.showerror(messages[language][8],error)
                except IndexError as e:
                    error = messages[language][9] + e
                    messagebox.showerror(messages[language][8],error)
            
            def open_custom_cancel():
                launch_custom2.destroy()
            
            launch_custom2_label = ttk.Label(launch_custom2,text=messages[language][24],font=30)
            launch_custom2_list = Listbox(launch_custom2,width=490,font=20,height=5)
            for i in range(len(result_search_index_games[selected_game])):
                if result_search_index_games[selected_game][i] in file_names:
                    launch_custom2_list.insert(END,file_names[result_search_index_games[selected_game][i]])
                    open_list_h.append(file_names[result_search_index_games[selected_game][i]])
                else:
                    launch_custom2_list.insert(END,result_search_index_games[selected_game][i])
                    open_list_h.append(result_search_index_games[selected_game][i])
                open_list.append(i)
            launch_custom2_open = Button(launch_custom2,text=messages[language][25],font=30,command=open_custom)
            launch_custom2_cancel = Button(launch_custom2,text=messages[language][18],font=30,command=open_custom_cancel)
            launch_custom2_label.pack()
            launch_custom2_list.pack()
            launch_custom2_open.pack(side=LEFT)
            launch_custom2_cancel.pack(side=RIGHT)
            launch_custom2.mainloop()
        elif len(result_search_index_custom[selected_game]) == 1:
            result = result_search_index_custom[0][0]
            result2 = result
            result = result.replace("\\custom.exe","")
            if os.path.isfile(result2):
                print("アプリを開く：「" + result2 + "」、「" + result + "」の上で")
                subprocess.run(result2,shell=True,cwd=result)
            else:
                error = messages[language][23] + result
                messagebox.showerror(messages[language][8],error)
        elif len(result_search_index_custom[selected_game]) == 0:
            error = messages[language][26]
            for i in setting[0]:
                error = error + i + ",\n"
            messagebox.showerror(messages[language][8],error)
    except TypeError as e:
        error = messages[language][9] + e
        messagebox.showerror(messages[language][8],error)
        
def settings():
    setting_window = Tk()
    setting_window.geometry("400x400")
    setting_window.title(messages[language][27])
    setting_window.iconbitmap("icon.ico")
    
    def set0_w():
        set0_window = Tk()
        set0_window.geometry("400x400")
        set0_window.title(messages[language][28])
        set0_window.iconbitmap("icon.ico")
        
        global search_dire_k
        search_dire_k = []
        for i in setting[0]:
            search_dire_k.append(i)
        print(search_dire_k)
        dire_list_var = StringVar(set0_window,value=search_dire_k)
        dire_list = Listbox(set0_window,width=100,font=30,listvariable=dire_list_var)
        dire_list_var.set(search_dire_k)
        
        def folder_add():
            folder = filedialog.askdirectory(title=messages[language][29],initialdir="PC")
            if folder != "":
                search_dire_k.append(folder)
                dire_list_var.set(search_dire_k)
        def folder_delete():
            try:
                selected_folder = dire_list.get(dire_list.curselection())
                search_dire_k.remove(selected_folder)
                dire_list_var.set(search_dire_k)
            except IndexError as e:
                error = messages[language][30] + e
                messagebox.showerror(messages[language][8],error)
            except TypeError as e:
                error = messages[language][30] + e
                messagebox.showerror(messages[language][8],error)
        def close_set0():
            set0_window.destroy()
        
        set0_add = Button(set0_window,text=messages[language][31],font=30,command=folder_add)
        set0_delete = Button(set0_window,text=messages[language][32],font=30,command=folder_delete)
        set0_close = Button(set0_window,text=messages[language][33],font=30,command=close_set0)
        
        dire_list.pack()
        set0_add.pack(side=LEFT)
        set0_delete.pack(side=LEFT)
        set0_close.pack(side=RIGHT)
        
        set0_window.mainloop()
    
    def save_setting():
        setting[0] = search_dire_k
        setting_window.destroy()
        data_json_update(messages[language][34])
    
    def cancel_setting():
        setting_window.destroy()
    
    set0_button = Button(setting_window,text=messages[language][35],font=30,command=set0_w)
    setting_save = Button(setting_window,text=messages[language][36],font=30,command=save_setting)
    setting_cancel = Button(setting_window,text=messages[language][18],font=30,command=cancel_setting)
    
    set0_button.pack(side=LEFT)
    setting_cancel.pack(side=RIGHT,anchor=S)
    setting_save.pack(side=RIGHT,anchor=S)
    
    setting_window.mainloop()

def app_info():
    info_window = Tk()
    info_window.geometry("500x300")
    info_window.iconbitmap("icon.ico")
    info_window.title(messages[language][1])
    
    info_title = Label(info_window,text=messages[language][37],font=50)
    info_version = Label(info_window,text="ver1.3.0\nProgramed by Gottsudayo",font=20)
    
    def close_info():
        info_window.destroy()
        
    info_ok = Button(info_window,text="ok",font=30,command=close_info)
    
    info_title.pack()
    info_version.pack()
    info_ok.pack(side=BOTTOM)
    
    info_window.mainloop()

launcher_widget()
