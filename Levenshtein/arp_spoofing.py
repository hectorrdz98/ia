import scapy.all as scapy

def get_mac(ip):
    # Create arp packet object. pdst - destination host ip address
    arp_request = scapy.ARP(pdst=ip)
    print('arp_request: {}'.format(arp_request))
    # Create ether packet object. dst - broadcast mac address. 
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    print('broadcast: {}'.format(broadcast))
    # Combine two packets in two one
    arp_request_broadcast = broadcast/arp_request
    print('arp_request_broadcast: {}'.format(arp_request_broadcast))
    # Get list with answered hosts
    ans, unans = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
    print(ans)
    # ans.summary(lambda (s,r): r.sprintf("%Ether.src% %ARP.psrc%") )
    # print('answered_list: {}'.format(answered_list))
    # Return host mac address

ip = '192.168.43.99'
print('IP: {}'.format(ip))
get_mac(ip)