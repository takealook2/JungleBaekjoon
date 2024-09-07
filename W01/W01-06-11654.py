ans = input()

if (ans.isalpha()):
    print(ord(ans))
elif (ans.isdigit()):
    ans_int = int(ans)
    if (0<=ans_int<10):
        print(ord(ans))