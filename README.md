# nmap_auto

OSCP 시험 준비 과정에서, 여러 IP 대역을 한 번에 스캔하고 싶어 만든 자동화 도구입니다.  
전체 포트를 빠르게 스캐닝하고, 열린 포트에 대해서만 서비스 식별을 수행합니다.  
시험 환경에서 사용하려면 도구가 미리 업로드되어 있어야 한다고 하여, 해당 코드를 GitHub에 업로드합니다.


## 사용법
- 실행하면 IP를 한 줄씩 입력받습니다.
- `scanport/` 폴더가 없으면 자동 생성되며, IP 마지막 옥텟을 기준으로 결과가 저장됩니다.

```
┌──(root㉿kali)-[/home/kali/Desktop]
└─# python3 nmap_auto.py                        
[*] Welcome to Multi-IP Nmap Port Scanner
Enter target IPs one per line. Enter a blank line to finish:
IP: 10.129.161.121
IP: 10.10.14.17
IP: [끝났으면 그냥 엔터]

```

## 결과 확인
- 조사한 ip 맨 끝자리로 파일이 저장됩니다. (scanport 디렉터리 내부에)
```
┌──(root㉿kali)-[/home/kali/Desktop]
└─# ./tcpview.sh scanport/121_tcpdetailed.txt                                                
📡 Host: 10.129.242.121 ()
🔓 Open TCP Ports:
- Port: 53     → domain          (Simple DNS Plus)
- Port: 80     → http            (Microsoft IIS httpd 10.0)
- Port: 88     → kerberos-sec    (server time: 2025-08-16 12:26:34Z))
- Port: 135    → msrpc           (Microsoft Windows RPC)
- Port: 139    → netbios-ssn     (Microsoft Windows netbios-ssn)
- Port: 389    → ldap            (Domain: authority.htb)
- Port: Site: Default-First-Site-Name) → unknown        
- Port: 445    → microsoft-ds?  
- Port: 464    → kpasswd5?      
- Port: 593    → ncacn_http      (Microsoft Windows RPC over HTTP 1.0)
- Port: 636    → ssl|ldap        (Domain: authority.htb)
- Port: Site: Default-First-Site-Name) → unknown        
- Port: 3268   → ldap            (Domain: authority.htb)
- Port: Site: Default-First-Site-Name) → unknown        
- Port: 3269   → ssl|ldap        (Domain: authority.htb)
- Port: Site: Default-First-Site-Name) → unknown        
- Port: 5985   → http            (Microsoft HTTPAPI httpd 2.0 (SSDP|UPnP))
- Port: 8443   → ssl|http        (Apache Tomcat (language: en))
- Port: 9389   → mc-nmf          (.NET Message Framing)
- Port: 47001  → http            (Microsoft HTTPAPI httpd 2.0 (SSDP|UPnP))

```
## 옵시디언에 정리한 모습
<img width="670" height="508" alt="image" src="https://github.com/user-attachments/assets/e2f15f65-b3b8-48a7-80a8-25e027459e27" />



## 개인적인 사용방법
nmap 결과는 모두 출력되기 때문에 꼼꼼하게 살펴봅니다.
출력 결과물을 분석하고 특이 사항은 위 결과물 옆에 적어두는 편입니다. 
깔끔하게 정리도 하고 열려 있는 포트는 항상 인지하고 있으려고 합니다. 

++
이 도구는 개인 교육용으로 제작되었습니다.
