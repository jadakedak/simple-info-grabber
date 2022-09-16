import socket
from time import sleep

HOST = "192.168.68.104"
PORT = 80
BUFFER = 1024*3

def main(seconds_to_try):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    seconds = 0
    address = (HOST,PORT)
    
    for i in range(0, seconds_to_try):
        try:
            sock.connect(address)      
            msg = sock.recv(BUFFER).decode()
            print(f"[+] information recived!")
            print(msg) 
            break
        except:
            if seconds >= 2:
                print(f"Running for {seconds} seconds...")
            else:
                print(f"Running for {seconds} second...") 
            seconds += 1
            sleep(1)


            
            
    






if __name__ == "__main__":
    main(100)