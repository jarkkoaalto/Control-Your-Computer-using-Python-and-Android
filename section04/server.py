from socket import * 
import os
import platform

host = "192.168.1.247"
port = 9999

s = socket(AF_INET, SOCK_STREAM)
s.bind((host,port))
s.listen(5)

while True:
    c,addr = s.accept()
    type = c.recv(1024).decode('utf-8')
    if(type == "shutdown"):
        if(platform.system() == "Windows"):
            os.system("shutdown /f")
        elif(platform.system() == "Linux"):
            os.system("shutdown")
    elif(type == "restart"):
        if(platform.system() == "Windows"):
            os.system("shutdown /r")
        elif(platform.system() == "Linux"):
             os.system("shutdown -r")
    elif(type == "music"):
        if(platform.system() == "Windows"):
            os.system("D:\\1.mp3")
        elif(platform.system() == "Linux"):
             os.system("~/1.mp3")
    print(c.recv(1024).decode('UTF-8'))
