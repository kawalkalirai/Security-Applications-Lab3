from scapy.all import *

print("Capturing 50 packets...")

# How much of each protocol
n_tcp = 0
n_udp = 0
n_other = 0

def log_packet(p):
    global n_tcp, n_udp, n_other
    
    # IP, PORTS, PROTOCOLS
    if IP in p:
        src = p[IP].src
        dst = p[IP].dst
        
        if TCP in p:
            n_tcp += 1
            sport = p[TCP].sport
            dport = p[TCP].dport
            print(f"TCP  | {src}:{sport} -> {dst}:{dport}")

        elif UDP in p:
            n_udp += 1
            sport = p[UDP].sport
            dport = p[UDP].dport
            print(f"UDP  | {src}:{sport} -> {dst}:{dport}")
            
        else:
            n_other += 1
            print(f"IP   | {src} -> {dst}")

# Captures 50 packets
sniff(filter="ip", prn=log_packet, count=50)

#OUTPUT SUMMARY
print("Capture Complete")
print(f"TCP: {n_tcp}")
print(f"UDP: {n_udp}")
print(f"Other: {n_other}")
