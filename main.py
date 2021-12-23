############################
##           GuP          ##
##                        ##
## version: 1.0b1         ##
## author: whmsft         ##
## contributors: none     ##
############################

import tkinter as tk
from tkinter import ttk
import time
import random

def messagebox(message):
    global messagebox_frame
    messagebox_frame = tk.Frame(gameframe, bg = '#000', width = 330, height = 200,highlightbackground="#fff", highlightthickness=2)
    messagebox_message = tk.Label(messagebox_frame, text=message, font = 'Segoe\ UI 15', background = '#000', foreground = '#fff')
    messagebox_message.place(x=5, y=5)
    messagebox_okbtn = tk.Button(messagebox_frame, text= "Yes", font = 'Segoe\ UI 15', background = '#404040', foreground = '#fff', command = lambda:exec('messagebox_frame.place_forget()'), borderwidth=0, activebackground = '#555', activeforeground = '#fff')
    messagebox_okbtn.place(x=5, y=140, width = 315, height = 50)
    messagebox_frame.place(relx=0.5, rely=0.5, anchor = 'center')

def jumpIn(frameobj, t=-360):
    frameobj.place(x=t, y=0)
    if t > 0:
        return
    root.after(1, jumpIn, frameobj, t+1)

def jumpOut(frameobj, t=0):
    frameobj.place(x=t,y=0)
    if t > 360:
        return
    root.after(1, jumpOut, frameobj, t+1)

def addtoper(num, bk=False):
    global guesspercent
    num = str(num)
    if not bk:
        guesspercent += num
        guesspercentage['text'] = guesspercent+'%'
    else:
        guesspercent = guesspercent[:-1]
        guesspercentage['text'] = guesspercent+'%'

def difference(num1, num2):
    if num1 == num2:
        return 0
    elif num1 > num2:
        return num1-num2
    elif num2 > num1:
        return num2-num1

def confirm():
    global score, guesspercent
    if difference(pbar['value'], int(guesspercent)) == 0:
        score = score + 10
        tkscore['text'] = 'Score: '+ str(score)
        pbar['value'] = random.randint(0,100)
        guesspercent = '0'
        guesspercentage['text'] = '0%'
    elif difference(pbar['value'], int(guesspercent)) <= 10:
        score = score + 5
        tkscore['text'] = 'Score: '+ str(score)
        pbar['value'] = random.randint(0,100)
        guesspercent = '0'
        guesspercentage['text'] = '0%'
    else:
        score = score - 10
        tkscore['text'] = 'Score: '+ str(score)
        pbar['value'] = random.randint(0,100)
        guesspercent = '0'
        guesspercentage['text'] = '0%'

def startclicked():
    tick_mark = '✅'
    backspace = '⌫'
    another_tick = '✔'
    global guesspercent, guesspercentage, pbar, gameframe, score, tkscore
    score = 0
    gameframe = tk.Frame(root, background='#000', width=360, height=640)
    guesspercent = ''
    tkscore = tk.Label(gameframe, text = 'Score: '+str(score), background = '#000', foreground = '#fff', font = 'Segoe\ UI 20')
    tkscore.place(relx=0.5, rely=0.1, anchor = 'center')
    backbtn = tk.Button(gameframe, text = '<', font = 'Consolas 25', relief = 'flat', borderwidth=0, foreground= '#ffffff', background = '#000000', activeforeground = '#fff', activebackground='#000', command = lambda:jumpOut(gameframe))
    backbtn.place(relx = 0, rely=0)
    pbar = ttk.Progressbar(gameframe, style="bar.Horizontal.TProgressbar", orient="horizontal", length=300, mode="determinate", maximum=100, value=random.randint(0,100))
    pbar.place(relx=0.5, rely=0.3, anchor = 'center', height=50)
    guesspercentage = tk.Label(gameframe, font = 'Segoe\ UI 20', foreground = 'white', background = '#000')
    guesspercentage['text'] = '0%'
    guesspercentage.place(relx=0.5, rely=0.5, anchor = 'center')
    num1 = tk.Button(gameframe, text = 1, font = 'Segoe\ UI 20', relief = 'flat', background = '#404040', foreground = '#fff', borderwidth = 0, activeforeground= '#fff', activebackground = '#505050', command = lambda i=1:addtoper(i))
    num1.place(height = 50, width = 110, x = 10, y = 640-225)
    num2 = tk.Button(gameframe, text = 2, font = 'Segoe\ UI 20', relief = 'flat', background = '#404040', foreground = '#fff', borderwidth = 0, activeforeground= '#fff', activebackground = '#505050', command = lambda i=2:addtoper(i))
    num2.place(height = 50, width = 110, x = 125, y = 640-225)
    num3 = tk.Button(gameframe, text = 3, font = 'Segoe\ UI 20', relief = 'flat', background = '#404040', foreground = '#fff', borderwidth = 0, activeforeground= '#fff', activebackground = '#505050', command = lambda i=3:addtoper(i))
    num3.place(height = 50, width = 110, x = 240, y = 640-225)
    num4 = tk.Button(gameframe, text = 4, font = 'Segoe\ UI 20', relief = 'flat', background = '#404040', foreground = '#fff', borderwidth = 0, activeforeground= '#fff', activebackground = '#505050', command = lambda i=4:addtoper(i))
    num4.place(height = 50, width = 110, x = 10, y = 640-170)
    num5 = tk.Button(gameframe, text = 5, font = 'Segoe\ UI 20', relief = 'flat', background = '#404040', foreground = '#fff', borderwidth = 0, activeforeground= '#fff', activebackground = '#505050', command = lambda i=5:addtoper(i))
    num5.place(height = 50, width = 110, x = 125, y = 640-170)
    num6 = tk.Button(gameframe, text = 6, font = 'Segoe\ UI 20', relief = 'flat', background = '#404040', foreground = '#fff', borderwidth = 0, activeforeground= '#fff', activebackground = '#505050', command = lambda i=6:addtoper(i))
    num6.place(height = 50, width = 110, x = 240, y = 640-170)
    num7 = tk.Button(gameframe, text = 7, font = 'Segoe\ UI 20', relief = 'flat', background = '#404040', foreground = '#fff', borderwidth = 0, activeforeground= '#fff', activebackground = '#505050', command = lambda i=7:addtoper(i))
    num7.place(height = 50, width = 110, x = 10, y = 640-115)
    num8 = tk.Button(gameframe, text = 8, font = 'Segoe\ UI 20', relief = 'flat', background = '#404040', foreground = '#fff', borderwidth = 0, activeforeground= '#fff', activebackground = '#505050', command = lambda i=8:addtoper(i))
    num8.place(height = 50, width = 110, x = 125, y = 640-115)
    num9 = tk.Button(gameframe, text = 9, font = 'Segoe\ UI 20', relief = 'flat', background = '#404040', foreground = '#fff', borderwidth = 0, activeforeground= '#fff', activebackground = '#505050', command = lambda i=9:addtoper(i))
    num9.place(height = 50, width = 110, x = 240, y = 640-115)
    num0 = tk.Button(gameframe, text = 0, font = 'Segoe\ UI 20', relief = 'flat', background = '#404040', foreground = '#fff', borderwidth = 0, activeforeground= '#fff', activebackground = '#505050', command = lambda i=0:addtoper(i))
    num0.place(height = 50, width = 110, x = 125, y = 640-60)
    symback = tk.Button(gameframe, text = '⌫', font = 'Segoe\ UI 20', relief = 'flat', background = '#404040', foreground = '#fff', borderwidth = 0, activeforeground= '#fff', activebackground = '#505050', command = lambda i=True:addtoper(0,bk=True))
    symback.place(height = 50, width = 110, x = 240, y = 640-60)
    symconf = tk.Button(gameframe, text = '✔', font = 'Segoe\ UI 20', relief = 'flat', background = '#404040', foreground = '#fff', borderwidth = 0, activeforeground= '#fff', activebackground = '#505050', command = lambda:confirm())
    symconf.place(height = 50, width = 110, x = 10, y = 640-60)
    jumpIn(gameframe)

root = tk.Tk()
windowWidth = 360
windowHeight = 640
screenWidth  = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
xCordinate = int((screenWidth/2) - (windowWidth/2))
yCordinate = int((screenHeight/2) - (windowHeight/2))
root.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, xCordinate, yCordinate))
root.config(bg='#000000')

TROUGH_COLOR = '#202020'
BAR_COLOR = '#0084ff'
Style = ttk.Style(root)
Style.theme_use('clam')
Style.configure("blue.Horizontal.TProgressbar", foreground='blue', background='blue')
Style.configure("bar.Horizontal.TProgressbar", troughcolor=TROUGH_COLOR, bordercolor=TROUGH_COLOR, background=BAR_COLOR, lightcolor=BAR_COLOR, darkcolor=BAR_COLOR)

mainmenu = tk.Frame(root, background='#000', width=360, height=640)
#mainmenu.pack(fill = 'both', expand = True)
startbtn = tk.Button(mainmenu, text = 'Start', font = 'Segoe\ UI 50', relief='flat', borderwidth=0, foreground= '#ffffff', background = '#000000', activeforeground = '#fff', activebackground='#000', command = startclicked)
startbtn.place(relx=0.5, rely=0.5, anchor='center')

jumpIn(mainmenu)
root.mainloop()
