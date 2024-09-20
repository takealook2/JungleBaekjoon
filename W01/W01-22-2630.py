# 입력받기
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

# 결과를 저장할 변수
white = 0  # 흰색 색종이 개수
blue = 0   # 파란색 색종이 개수

# 해당 영역이 모두 같은 색인지 확인하는 함수
def check(x, y, size):
    global white, blue
    color = paper[x][y]  # 첫 번째 색을 기준으로 삼음
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:  # 다른 색이 나오면 4분할 진행
                half = size // 2
                check(x, y, half)  
                check(x, y + half, half) 
                check(x + half, y, half)
                check(x + half, y + half, half)
                return

    # 모두 같은 색이라면
    if color == 0:
        white += 1
    else:
        blue += 1

# 분할정복 시작
check(0, 0, N)

# 결과 출력
print(white)
print(blue)
