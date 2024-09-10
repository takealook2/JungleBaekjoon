# 문자열 S
# 각 문자를 R번 반복 후 새로운 문자열 P

# 문자열 S는 공백으로 구분되어 주어짐
R = 0
S = []

# R번 반복하고 반복할 문자열 S를 입력 받음
testcase = int(input())

for i in range(testcase):
    R, S = map(str, input().split())
    R = int(R)
    for i in range(len(S)):
        print(S[i]*R, end="")
    print()