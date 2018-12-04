import ftplib
import os
import socket

HOST = "ftp.acc.umu.se"
DIR = 'Public/EFLIB/'
FILE = 'README'

try:
    f = ftplib.FTP()
    f.set_debuglevel(2)
    f.connect(HOST)
except Exception as e:
    print(e)
    exit()
print("***Connected to host {0}".format(HOST))



try:
    f.login()
except Exception as e:
    print(e)
    exit()
print("***Logged in as 'anonymous'")


try:
    f.cwd(DIR)
except Exception as e:
    print(e)
    exit()
print("*** Changed dir to {0}".format(DIR))

try:
    # 从FTP服务器上下载文件
    # 第一个参数是ftp命令
    # 第二个参数是回调函数
    # 此函数的意思是，执行RETR命令，下载文件到本地后，运行回调函数
    f.retrbinary('RETR {0}'.format(FILE), open(FILE, 'wb').write)
except Exception as e:
    print(e)
    exit()

f.quit()