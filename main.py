import scanIP
import scanPort
import ipaddress


def main():
    ip = input("Enter the IP range to scan: ")
    port = int(input("Enter the port to scan: "))
    try :
        ipaddress.ip_network(ip, strict=False)
    except ValueError:
        print("Invalid IP range")
        return
    
    devices = scanIP(ip)
    available = []
    for device in devices:
        if scanPort(device["ip"], port):
            available.append(device)
    if available:
        print("IP\t\t\tMAC Address")
        print("----------------------------------------------------")
        for device in available:
            print(device["ip"] + "\t\t" + device["mac"])
    else:
        print("No devices found")

if __name__ == "__main__":
    main()