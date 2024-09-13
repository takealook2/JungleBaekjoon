# input score
# 0 <= score <= 150
# score 중복되는 값 제거 .set()
# score.sort() 후 인덱스 4~8의 합

n = 8
score = []
scoreSort = []
resultScore = 0
scoreIdx = []

for i in range(n):
    score.append((int(input())))
    if score[i] < 0 or score[i] > 150:
        exit()

scoreSort = sorted(score)

for j in range(3, 8, 1):
    resultScore += scoreSort[j]
    for k in range(n):
        if scoreSort[j]==score[k]:
            scoreIdx.append(k+1)


scoreIdx = sorted(scoreIdx)

print(resultScore)
print(*scoreIdx, end='')