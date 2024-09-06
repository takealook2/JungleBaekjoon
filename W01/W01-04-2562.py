a = [None]*9

for i in range(0, 9):
    while True:
        a[i]=int(input())
        if 0 <= a[i] <= 100:
            break
        else:
            print("Error")

max = a[0]
max_index = 1

# max 구하기
for i in range(1,9):
    if(a[i]>max):
        max=a[i]
        max_index=i + 1
print(max)
print(max_index)