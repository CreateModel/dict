'''
电子词典客户端功能
１．一级界面：登录，注册，退出
２．二级界面：查单词 ，历史记录，注销

'''
import sys
import os
from socket import *
import time
ADDR = ('127.0.0.1', 8866)
def view2(c,name):
    while True:
        print('1.查单词\n2.历史记录\n3.注销\n')
        order = input('请选择：')
        if order == '3':
            view(c)
        elif order=='2':
            while True:
                word=input('查询单词：\n##退出查询')
                if word=='##':
                    break
                msg='SEA '+ word
                c.send(msg.encode())
                data=c.recv()
                print(data.decode())
        elif order=='3':
            msg='HIS '+name
            c.send(msg.encode(),ADDR)
            data=c.recv()
def view(c):
    while True:
        print("1.登录\n2.注册\n3.退出")
        order=input('请选择：')
        if order=='3':
            sys.exit('感谢您的使用！')
        elif order=='1':
            name=input('用户名：')
            passwd=input('密码：')
            msg='LOG '+name+' '+passwd
            c.sendto(msg.encode(),ADDR)
            result=c.recv()
            if result=='allright':
                   view2(c,name)
            elif result=='nouser':
                print('用户不存在，请注册')
                continue
            elif result=='worrypasswd':
                print('密码错误！')
                continue
        elif order=='2':
            name = input('请输入用户名：')
            passwd = input('请输入密码：')
            if not name and passwd:
                continue
            msg = 'SIG ' + name + ' ' + passwd
            c.sendto(msg.encode(), ADDR)
            result = c.recv()
            if result == b'ok':
                print('注册成功！登录中．．．')
                time.sleep(1)
                view2(c,name)
            elif result == b'haduser':
                print('用户名已存在')
                continue



def main():
    c=socket()
    c.connect(ADDR)
    view(c)
    c.close()

if __name__ == '__main__':
    main()