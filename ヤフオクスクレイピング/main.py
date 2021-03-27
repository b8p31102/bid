#!/usr/bin/env python
# -*- coding: utf8 -*-

import tkinter as tk
import sys
import subprocess
import tkinter.ttk as ttk
#ボタンクリックイベント処理
def btn1():
    #YahooAuction_bid.py表実行
    subprocess.Popen(r'YahooAuction_Successful_bid.exe')
    #keyword = entry1_frame()
        

def btn2():
    #YahooAuction_secessful_bid.py表実行
    subprocess.Popen(r'YahooAuction_bid.exe')

def finish_menu():
    sys.exit()

def yahuoku():
    global frame_app
    
    frame.destroy()
    
    # メインフレームの作成と設置
    frame_app = ttk.Frame(root)
    frame_app.pack(fill = tk.BOTH, pady=20)

    # 各種ウィジェットの作成
    label1_frame_app = ttk.Label(frame_app, text="ヤフオク")
    entry1_frame_app = ttk.Entry(frame_app)
    button_change_frame_app = ttk.Button(frame_app, text="メルカリ", command=mercari )
    python_btn_frame_app = ttk.Button(frame_app, text='python実行', command=btn2)
    finish_menu_Button = ttk.Button(frame_app, text=u'2終了')
    finish_menu_Button["command"] = finish_menu

    
    # 各種ウィジェットの設置
    label1_frame_app.pack()
    entry1_frame_app.pack()
    button_change_frame_app.pack()
    python_btn_frame_app.pack()
    finish_menu_Button.pack()

def mercari():
    global frame
    
    
    frame_app.destroy()
    
    # メインフレームの作成と設置
    frame = ttk.Frame(root)
    frame.pack(fill = tk.BOTH, pady=20)

    # 各種ウィジェットの作成
    label1_frame = ttk.Label(frame, text="メルカリ")
    entry1_frame = ttk.Entry(frame)
    button_change = ttk.Button(frame, text="ヤフオク", command=yahuoku)
    python_btn = ttk.Button(frame, text='python実行', command=btn1)
    finish_menu_Button = ttk.Button(frame, text=u'1終了')
    finish_menu_Button["command"] = finish_menu
    
    # 各種ウィジェットの設置
    label1_frame.pack()
    entry1_frame.pack()
    button_change.pack()
    python_btn.pack()
    finish_menu_Button.pack()
    



    
      
    
if __name__ == "__main__":
    # rootメインウィンドウの設定
    root = tk.Tk()
    root.title("tkinter application")
    root.geometry("300x150")

    # メインフレームの作成と設置
    frame = ttk.Frame(root)
    frame.pack(fill = tk.BOTH, pady=20)



    # 各種ウィジェットの作成
    label1_frame = ttk.Label(frame, text="メインウィンドウ")
    entry1_frame = ttk.Entry(frame)
    button_change = ttk.Button(frame, text="ヤフオク", command=yahuoku)
    button_change_frame_app = ttk.Button(frame, text="メルカリ", command=mercari)
    
    finish_menu_Button = ttk.Button(frame, text=u'3終了')
    finish_menu_Button["command"] = finish_menu
    
    # 各種ウィジェットの設置
    label1_frame.pack()
    entry1_frame.pack()
    button_change.pack()
    button_change_frame_app.pack()
    
    finish_menu_Button.pack()
    
    root.mainloop()    
    
