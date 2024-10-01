import sys

input = sys.stdin.readline

num = input().strip()

if "-" in num:
    num = num.split("-")
    if "+" in num[0]:
        result = sum(map(int, num[0].split("+")))
    else: 
        result = int(num[0])

    for n in num[1:]:
        result -= sum(map(int, n.split("+")))
else:
    num = num.split("+")
    result = int(num[0])
    for n in num[1:]:
        result+=int(n)

print(result)