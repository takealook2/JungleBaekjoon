num = int(input())
same_num = []

if 1 <= num <= 20000:
    arr = [None]*num

for i in range(num):
    arr[i] = input()
    if len(arr[i]) > 50:
        None

arr_unique = list(set(arr))

arr_unique.sort()
# lambda 함수를 통해 (단어의 길이, 단어) 식으로 튜플을 형성함
# 튜플을 형성한 후 일단 단어의 길이를 가지고 정렬하고
# 단어의 길이를 정렬한 후에 단어를 가지고 오름차순 정렬을 함
arr_unique.sort(key=lambda x: len(x))


for item in arr_unique:
    print(item)