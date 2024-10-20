import scapy.all as scapy
import ipaddress

def scanIP(ip:str):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast = broadcast/arp_req
    answered_list = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]

    conected_list = []

    for answer in answered_list:
        device = {"ip": answer[1].psrc, "mac": answer[1].hwsrc}
        conected_list.append(device)

    return conected_list


def main():
    ip = input("Enter the IP range to scan: ")
    try :
        ipaddress.ip_network(ip, strict=False)
    except ValueError:
        print("Invalid IP range")
        return
    
    devices = scanIP(ip)
    if devices:
        print("IP\t\t\tMAC Address")
        print("----------------------------------------------------")
        for device in devices:
            print(device["ip"] + "\t\t" + device["mac"])
    else:
        print("No devices found")

if __name__ == "__main__":
    #main()
    print(scanIP("192.168.1.1/24"))