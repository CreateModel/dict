'''
服务端功能
１．登录，注册
    用户列表(user)
2.逻辑处理
    查询

通讯协议：　LOG
         SIG
         SEA
         HIS
'''
import sys
from socket import *
from multiprocessing import Process
import pymysql
import signal
ADDR=('127.0.0.1',8866)
def handle(confd):
    while True:
        request=confd.recv(1024).decode()
        if not request:
            confd.close()
        print('OK')

def main():
    s=socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(3)
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    while True:
        print('Listen the port 8866')
        try:
            confd,addr=s.accept()
            print('Connect from',addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit('退出服务端')
        except Exception as e:
            s.close()
            print(e)
            continue
        p=Process(target=handle,args=(confd,))
        p.start()

if __name__ == '__main__':
    main()



