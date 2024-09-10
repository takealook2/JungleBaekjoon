# 무작위 수를 입력받는데 일곱 개의 정수 합이 무조건 100이 될 수 있는 거임?

# 주어지는 키 0 < height < 100
# 중복되는 값은 없음
# 조합을 통해 7개의 height를 더했을 때 == 100
# 합이 100이 되는 height를 출력

# 파이썬에서 제공하는 combinations 함수 존재

from itertools import combinations

# 총 입력받을 수 있는 수(num)
num = 9

# height 리스트 초기화
height = []

# 9개의 height를 입력받아 리스트에 저장(0<height<100)
for i in range(num):
    height.append(int(input()))

height_comb = list(combinations(height, 7))
success_arr = []

def combSum(arr):
    for i in range(len(arr)):
        if sum(arr[i]) == 100:
            success_arr = list(arr[i])
            # 해당 정답 리스트 하나를 불러올 건데, 오름차순 정렬
            success_arr.sort()
            for j in success_arr:
                print(j)
            break



combSum(height_comb)