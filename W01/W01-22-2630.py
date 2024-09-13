































# 전체 종이의 한 변의 길이 N (2, 4, 8, 16, 32, 64, 128)
# 윗줄부터 차례로 둘째 줄부터 마지막 줄까지
# 하얀색은 0 파란색은 1 각 숫자 사이에는 빈칸(split())

N = int(input())

# # 만약 N이 2**1부터 2**7의 값이 아니라면 pass
# # 이거 분할탐색 넣으면 코드가 너무 헤비한가? 근데 떠오르는 방법이 이거밖에 없다
# # ** 연산자로 뭔가 할 수 있을 거 같은데 기억이 안 난다

# # 분할탐색으로 N 값이 저 배열 안에 없다면 pass 시키기
arr = [2, 4, 8, 16, 32, 64, 128]

def binarySearch(arr, key, low, high):
    mid = (low+high)//2
    if high < low:
        return 0
    if arr[mid]<key:
        return binarySearch(arr, key, mid+1, high)
    elif arr[mid]>key:
        return binarySearch(arr, key, low, mid-1)
    else:
        return 1

binarySearch(arr, N, 0, len(arr)-1)

# 그리고 이제 윗줄부터 마지막 줄까지 하얀색은 0 파란색은 1로 입력 받기
# 총 N 번 입력받습니다
paper = []
for i in range(N):
    paper.append(list(map(int, input().split())))

# 모두 같은 색으로 칠해져 있지 않으면 가로와 세로로 중간 부분을 잘라 N/2*N/2
# 같은 색으로 칠해져 있을 때까지 반복한다 자르는 걸

# 아니 나누는 게 왜 이해가 안 가지? 진짜 미치겠네
# 행과 열로 생각해야 하는 건 알겠다



















# # 전역 변수 선언
# white_count = 0
# blue_count = 0

# # 종이가 같은 색인지 확인하는 함수
# def isSameColor(paper, x, y, n):
#     baseColor = paper[x][y]
#     for i in range(x, x + n):
#         for j in range(y, y + n):
#             if paper[i][j] != baseColor:
#                 return False
#     return True

# # 종이를 4등분하면서 색종이의 개수를 세는 함수
# def divideAndCheck(paper, x, y, n):
#     global white_count, blue_count

#     # 만약 이 영역이 모두 같은 색이라면
#     if isSameColor(paper, x, y, n):
#         if paper[x][y] == 0:  # 하얀색
#             white_count += 1
#         else:  # 파란색
#             blue_count += 1
#     else:
#         # 영역을 4등분
#         half = n // 2
#         divideAndCheck(paper, x, y, half)  # 왼쪽 위
#         divideAndCheck(paper, x, y + half, half)  # 오른쪽 위
#         divideAndCheck(paper, x + half, y, half)  # 왼쪽 아래
#         divideAndCheck(paper, x + half, y + half, half)  # 오른쪽 아래

# # 메인 실행부
# N = int(input())  # 종이의 크기 입력
# paper = [list(map(int, input().split())) for _ in range(N)]  # 종이 입력 받기

# # 종이 전체 영역에 대해 분할 시작
# divideAndCheck(paper, 0, 0, N)

# # 결과 출력
# print(white_count)  # 하얀색 색종이 개수 출력
# print(blue_count)  # 파란색 색종이 개수 출력
