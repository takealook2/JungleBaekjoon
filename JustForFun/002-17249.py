import sys
input=sys.stdin.readline

# =로 시작해서 @로 끝남
# 얼굴의 형태 (^0^)
# @만 찾으면 되는 거 같은데

taebo = input().strip()

print(taebo)

right_punch = []
left_punch = []
right = 0
left = 0

right_punch = taebo.split("(")
left_punch = taebo.split(")")

right_punch = right_punch[0].split("=")
left_punch = left_punch[1].split("=")

for r in range(len(right_punch)):
    if "@" in right_punch[r]:
        right+=1
    else:
        pass
for l in range(len(left_punch)):
    if "@" in left_punch[l]:
        left+=1
    else:
        pass

print(right, left)