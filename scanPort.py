import socket
from tqdm import tqdm

def scanPort(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((ip, port))
    if result == 0:
        return True
    return False
    
def main():
    ip = input("Enter the IP address: ")
    opened = []

    for i in tqdm(range(1, 65535)):
        if scanPort(ip, i):
            opened.append(i)

    print(f"Opened ports ({len(opened)}): ")
    for i in opened:
        print(i)

if __name__ == "__main__":
    main()