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
arr_unique.sort(key=lambda x: len(x))


for item in arr_unique:
    print(item)