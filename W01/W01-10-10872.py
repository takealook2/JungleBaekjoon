def fact(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    return num*(fact(num-1))

num = int(input())

if 0 <= num <= 12:
    print(fact(num))
