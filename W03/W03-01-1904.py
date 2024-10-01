import sys
input = sys.stdin.readline

divisor = 15746

prv = 1
curr = 1

n = int(input())
for i in range(2, n+1):
    prv, curr = curr, (prv + curr)%divisor
print(curr)