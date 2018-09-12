from scapy.all import sniff

pcap = sniff(offline='capture.pcapng')

for packet in pcap :

    # ping to destination and success
    if packet['IP'].dst == '192.168.11.5' and packet['ICMP'].type == 8 :
        print(chr(len(packet.load)), end='')

print('\n')

