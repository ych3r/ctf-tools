from scapy.all import *
import ipaddress

ports = [25, 80, 53, 443, 445, 8080, 8443]


def SynScan(host: str) -> None:
    ans, unans = sr(
        IP(dst=host) /
        TCP(sport=33333, dport=ports, flags="S"), timeout=2, verbose=0)
    print(f"Open ports at {host}:")
    for (s, r) in ans:
        if s[TCP].dport == r[TCP].sport and r[TCP].flags == "SA":
            print(s[TCP].dport)


host = input("Enter IP Address: ")
try:
    ipaddress.ip_address(host)
except:
    print("Invalid address")
    exit(-1)

SynScan(host)