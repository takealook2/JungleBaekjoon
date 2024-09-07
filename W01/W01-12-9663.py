
queenNum = int(input())

# 체스판 생성하기

chess = [-1]*queenNum

# 체스판 생성(이제 체스판의 row, col)
# 퀸이 chess[0,0]에 들어가고
    # row, col, diagonal 조건이 참
        # 조건이 참일 때 퀸이 해당 위치에 들어서고(있으면 True 없으면 False)
        # row+1을 시킨 후 다음 퀸을 place 시킨다
    # 참이 아니라면 col+1
    # result 값을 +1 증가한다
# print(result)

# 결과적으로 i, j 즉 chess[i][j]를 가지고 참인지 아닌지를 판별

# row 조건은 chess[1][2] chess[1][3]이 있을 때 "1"이 겹치면 row가 겹치는 걸로
# 근데 여러 개의 조건이 겹치는 건 어떻게 해야하는 건지 모르겠다


for i in range(queenNum):
    for j in range(queenNum):
        if 



print(chess)

