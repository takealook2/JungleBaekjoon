N = int(input())

if (N >= 1 and N <= 9) :
    for i in range(1, 10):
        print(N,"*", i,"=",N*i)
else :
    print("Error")
