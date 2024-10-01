import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
coin = []

for _ in range(n):
    coin.append(int(input().strip()))

coin.sort(reverse=True)
count = 0

for c in coin:
    if k == 0:
        break
    if c <= k:
        count += k // c  # 해당 동전으로 필요한 개수 계산
        k %= c  # 남은 금액을 갱신

print(count)
