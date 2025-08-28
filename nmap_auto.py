import os
import subprocess
from pathlib import Path

def extract_open_ports(nmap_grep_file):
    open_ports = set()
    with open(nmap_grep_file, 'r') as f:
        for line in f:
            if "/open" in line:
                parts = line.split()
                for part in parts:
                    if "/open" in part:
                        port = part.split("/")[0]
                        open_ports.add(port)
    return ",".join(sorted(open_ports))

def get_ip_suffix(ip):
    return ip.strip().split(".")[-1]

def scan_ip(ip):
    suffix = get_ip_suffix(ip)

    # TCP SCAN
    open_tcp = f"scanport/{suffix}_open_tcp.txt"
    tcp_detailed = f"scanport/{suffix}_tcpdetailed.txt"
    print(f"[*] Scanning TCP ports on {ip}...")
    subprocess.run([
        "nmap", "-p-", "--min-rate", "3000", "-sS", "-Pn", "-T4", "-v",
        "-oG", open_tcp, ip
    ])
    ports = extract_open_ports(open_tcp)
    if ports:
        print(f"[*] Detected open TCP ports: {ports}")
        subprocess.run([
            "nmap", "-p", ports, "-Pn", "--min-rate", "2000",
            "-sV", "-sC", "-A", "-T4", "-oG", tcp_detailed, "-v", ip
        ])

    # UDP SCAN
    open_udp = f"scanport/{suffix}_open_udp.txt"
    udp_detailed = f"scanport/{suffix}_udpdetailed.txt"
    print(f"[*] Scanning UDP ports on {ip}...")
    subprocess.run([
        "nmap", "-sU", "-T4", "--min-rate", "3000", "-v",
        "-oG", open_udp, ip
    ])
    udp_ports = extract_open_ports(open_udp)
    if udp_ports:
        print(f"[*] Detected open UDP ports: {udp_ports}")
        subprocess.run([
            "nmap", "-sU", "-Pn", "-sV", "-sC", "-T4", "-v",
            "-p", udp_ports, "-oG", udp_detailed, ip
        ])

def main():
    print("[*] Welcome to Multi-IP Nmap Port Scanner")
    print("Enter target IPs one per line. Enter a blank line to finish:")

    ip_list = []
    while True:
        ip = input("IP: ").strip()
        if ip == "":
            break
        ip_list.append(ip)

    print("[*] All IPs received. Starting scans...\n")
    Path("scanport").mkdir(exist_ok=True)

    for ip in ip_list:
        scan_ip(ip)

    print("[*] Scan complete. Results saved in ./scanport/")

if __name__ == "__main__":
    main()
