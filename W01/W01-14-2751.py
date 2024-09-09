num = int(input())  # 첫 번째 입력: 숫자의 개수

array = []

# N 개의 배열 안에 N 번 수를 받음
for i in range(num):
    array.append(int(input()))  # 각 숫자를 입력받아 리스트에 추가

# 중복된 값 제거 후 정렬
array_unique = sorted(set(array))

# 정렬된 배열 출력
for i in array_unique:
    print(i)
