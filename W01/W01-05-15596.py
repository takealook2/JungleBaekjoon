# 합을 구해야 하는 정수 n 개가 저장되어 있는 리스트 a
# 1<=n<=3000000
# 0<=a[i]<=1000000

# def solve(a: list) -> int
# 정수의 개수는 n 개인데 정수의 범위는 0에서 1000000

# 난수야?

import random

n = random.randint(1, 3000000)
a = [None]*n

for i in range(0, n) :
    a[i] = random.randint(0,1000000)

def solve(a:list)->int:
    return sum(a)

print(solve(a))