import socket
from time import sleep
import os

HOST = ""
PORT = 80
BUFFER = 1024*3
        

def generate_subnet():
    actual_ip = ""
    local_ip = socket.gethostbyname(socket.gethostname()).split(".")
    first_3_of_ip = local_ip[0:3]
    for i in first_3_of_ip:
         actual_ip += i + "."
    for last_4 in range(1,255):
        with open("ip.txt", "a") as ips:
            ips.write(str(actual_ip))
            ips.write(str(last_4))
            ips.write("\n")
    ips.close()
    main(255)


def main(seconds_to_try):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    seconds = 0
    
    for i in range(0, seconds_to_try):
        with open("ip.txt", "r") as file:
            for ip in file:
                global HOST
                HOST += ip
                address = (HOST,PORT)
                try:
                    sock.connect(address)   
                    if address[0] == "10.78.65.25":
                        sock.connect(address)
                    msg = sock.recv(BUFFER).decode()
                    print(msg)
                    with open("results.txt", "a") as results:
                        results.write(msg)
                    exit(1)
                except:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("connecting to host {}".format(f"{HOST}"))
                    seconds += 1
                    HOST = ""
                    sleep(0.01)

                    if seconds >= seconds_to_try:
                        os.system("cls")
                        print("[!] couldnt find host to connect to")
                        file.close()
                        exit(1)

            
choice = input("[manual/auto]: ")   

if choice.lower() == "manual":
    new_host = input("type host: ")
    HOST += new_host
    address = (HOST,PORT)
    own_num = 0
    seconds_to_try = int(input("type connection attempts: "))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            sock.connect(address)      
            msg = sock.recv(BUFFER).decode()
            print(f"[+] information recived!")
            print(msg) 
            exit(1)
        except:
            print(f"connection attempt: {own_num}...")
            own_num += 1
            sleep(1)
        
            if own_num >= seconds_to_try: 
                break
            else:
                pass
elif choice.lower() == "auto":
    if __name__ == "__main__":
        generate_subnet()

