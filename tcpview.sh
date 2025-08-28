#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <tcpdetailed.txt file>"
    exit 1
fi

file="$1"

# 1. 호스트 정보 추출
host_line=$(grep "Host:" "$file" | head -n 1)
ip=$(echo "$host_line" | awk '{print $2}')
fqdn=$(echo "$host_line" | awk -F '[()]' '{print $2}')

echo "📡 Host: $ip ($fqdn)"
echo "🔓 Open TCP Ports:"

# 2. 포트/서비스/버전 정리
grep -o '[0-9]*/open/tcp.*' "$file" \
| sed 's/, /\n/g' \
| awk -F '/' '{
    service = ($5 == "" ? "unknown" : $5);
    version = ($7 == "" ? "" : " (" $7 ")");
    printf "- Port: %-6s → %-15s%s\n", $1, service, version;
}'

