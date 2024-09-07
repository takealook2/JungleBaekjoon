# 수의 개수 N 개(100 이하)
# 입력할 수 있는 수는 1000 이하의 자연수

# 수의 개수는 곧 원소의 개수

import math

# 수의 개수 입력받기
num = int(input())
if not (0 < num <= 100):
    exit()

# 숫자 리스트 입력받기
data = input()
a = list(map(int, data.split()))

# 입력된 수가 1000 이하의 자연수인지 확인
for i in range(num):
    if a[i] < 0 or a[i] > 1000:
        exit()

# 소수 여부를 판단하는 에라토스테네스의 체 (1000 이하의 소수만 체크)
max_num = 1000
array = [True] * (max_num + 1)
array[0], array[1] = False, False  # 0과 1은 소수가 아님

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(max_num)) + 1):
    if array[i]:  # i가 소수인 경우
        for j in range(i * i, max_num + 1, i):
            array[j] = False  # i의 배수는 소수가 아님

# 입력된 수들 중 소수의 개수 세기
decNum = 0
for i in range(num):
    if array[a[i]]:  # a[i]가 소수인지 확인
        decNum += 1

print(decNum)