import sys
import threading
import tkinter
import tkinter.ttk
from tkinter import *
from src import two_shibie, four_hecheng, five_play, three_jieru, one_luyin, function

stop = 1
flag = 1


def get_pro_ask():
    string = "please say something:"
    return string


def get_pro_end():
    string = "the dialogue is finished"
    return string


def fun():
    global flag
    flag = 1
    while True:

        # print the message:please say something
        text1.delete(0.0, tkinter.END)
        text1.insert(tkinter.INSERT, get_pro_ask())
        text1.update()

        one_luyin.rec()
        ask = two_shibie.listen()
        response = three_jieru.robot(ask)
        four_hecheng.speak(response)

        text1.delete(0.0, tkinter.END)
        text1.insert(tkinter.INSERT, ask)
        text1.update()

        text2.delete(0.0, tkinter.END)
        text2.insert(tkinter.INSERT, response)
        text2.update()

        five_play.play()
        if "退出" in ask or stop == 1:
            flag = 0
            break
    if flag == 0:
        print("process finished!")
        myWindow.destroy()


def fun1():
    # print the message:please say something
    text1.delete(0.0, tkinter.END)
    text1.insert(tkinter.INSERT, get_pro_ask())
    text1.update()

    one_luyin.rec()
    ask = two_shibie.listen()

    text1.delete(0.0, tkinter.END)
    text1.insert(tkinter.INSERT, ask)
    text1.update()

    # response = three_jieru.robot(ask)
    # index = ask.find('搜索')
    # response = ask[index + 2:-1]  # 省略机器人回应这一步骤，直接人工分割ask语句

    if ("播放音乐" not in ask) and ("qq音乐" not in ask) and ("交互软件" not in ask) and ("聊天软件" not in ask) and ("搜索" not in ask) and ("计算器" not in ask) and ("睡眠" not in ask):
        text2.delete(0.0, tkinter.END)
        text2.insert(tkinter.INSERT, "无法执行该任务")
        text2.update()
        four_hecheng.speak("无法执行该任务")
        five_play.play()

    else:
        text2.delete(0.0, tkinter.END)
        text2.insert(tkinter.INSERT, "正在执行" + ask[:-1] + "任务")
        text2.update()

        four_hecheng.speak("正在执行" + ask[:-1] + "任务")
        five_play.play()

        function.fun_total(ask)
        four_hecheng.speak("已执行" + ask[:-1] + "任务")

        five_play.play()

        text2.delete(0.0, tkinter.END)
        text2.insert(tkinter.INSERT, "已执行" + ask[:-1] + "任务")
        text2.update()


def fun1_pro():
    T = threading.Thread(target=fun1)
    T.setDaemon(True)       # 守护线程 当程序中主线程及所有非守护线程执行结束时，未执行完毕的守护线程也会随之消亡
    T.start()


def f_start():
    global stop
    stop = 0
    T = threading.Thread(target=fun)
    T.setDaemon(True)
    T.start()


def f_quit():
    global stop
    stop = 1

    myWindow.destroy()
    sys.exit()


text = ""
text_1 = ""
myWindow = Tk()

myWindow.title("颖颖AI")
myWindow.configure(bg="BurlyWood")
# myWindow.configure(bg="powderblue")
width = 850
height = 510
screenwidth = myWindow.winfo_screenwidth()
screenheight = myWindow.winfo_screenheight()
alignstr = ("%dx%d+%d+%d" % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2))
myWindow.geometry(alignstr)
# myWindow.resizable(width=False, height=False)

label1 = tkinter.Label(myWindow, text="ask:", bg="BurlyWood", fg="black", font=("Arial", 12), relief="flat")  # 询问标签
label1.grid(row=0, column=0, sticky='w')

text1 = tkinter.Text(myWindow, bg="BurlyWood", fg="black", font=("Arial Unicode MS", 14), width=60, height=9,
                     bd=0)  # 询问框
text1.grid(row=1, column=0, sticky='w')

label2 = tkinter.Label(myWindow, text="response:", bg="BurlyWood", fg="black", font=("Arial", 12),
                       relief="flat")  # 回应标签
label2.grid(row=3, column=0, sticky='w')

text2 = tkinter.Text(myWindow, bg="BurlyWood", fg="black", font=("Arial Unicode MS", 14), width=60, height=9,
                     bd=0)  # 回应框
text2.grid(row=4, column=0, sticky='w')

# label function
# label3=tkinter.Label(myWindow,text='button',bg='BurlyWood',fg='black',font=("Arial", 16),
#                      relief='flat')     # button label
# label3.grid(row=0,column=5,padx=60,pady=0,sticky='w')

# button function
button1 = tkinter.Button(myWindow, bg="BurlyWood", activebackground="DeepPink", text="loop", command=f_start,
                         font=("Arial", 16), width=8,
                         height=2, relief="groove")  # button command1
button1.grid(row=1, column=5, padx=40, pady=0)

button3 = tkinter.Button(myWindow, bg="BurlyWood", activebackground="DeepPink", text="single", command=fun1_pro,
                         font=("Arial", 16), width=8,
                         height=2, relief="groove")  # button command3
button3.grid(row=3, column=5, padx=40, pady=0)

button2 = tkinter.Button(myWindow, bg="BurlyWood", activebackground="DeepPink", text="exit", command=f_quit,
                         font=("Arial", 16), width=8,
                         height=2, relief="groove")  # button command2
button2.grid(row=4, column=5, padx=40, pady=0)  # 0

myWindow.attributes('-alpha', 0.8)  # 设置透明度(0-1)
# myWindow.overrideredirect(True)     #设置无边框对话框


myWindow.mainloop()
