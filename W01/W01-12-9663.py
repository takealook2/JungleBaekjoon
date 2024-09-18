# isPromising 함수를 통해 다음 퀸을 놓을 수 있을지 없는지를 탐색함
def isPromising(row, col, chess):
    # row 이전에 놓인 퀸들과 비교하여 같은 열에 있거나 대각선에 있는지 확인
    for i in range(row):
        if chess[i] == col or abs(chess[i] - col) == abs(i - row):
            return False  # 같은 열 또는 대각선에 있으면 False를 반환하여 퀸을 놓을 수 없음을 알림
    return True  # 퀸을 놓을 수 있으면 True 반환

# 퀸을 놓는 함수
def placeQueen(row, N, chess, solution_cnt, cols, left_diags, right_diags):
    # N개의 퀸을 모두 놓았을 때 가능한 경우의 수 증가
    if row == N:
        solution_cnt[0] += 1  # 가능한 경우의 수 카운트
    else:
        # 각 열에 퀸을 놓을 수 있는지 확인
        for col in range(N):
            # 해당 열 또는 대각선에 퀸이 이미 놓여있으면 스킵
            if cols[col] or left_diags[row - col + N - 1] or right_diags[row + col]:
                continue  # 조건이 충족되지 않으면 반복문의 다음 열로 넘어감

            # 퀸을 현재 (row, col)에 놓을 수 있으므로 해당 위치에 퀸 배치
            chess[row] = col
            # 열과 대각선의 상태를 True로 설정하여 퀸이 놓였음을 표시
            cols[col] = left_diags[row - col + N - 1] = right_diags[row + col] = True
            
            # 다음 행에 퀸을 놓기 위해 재귀 호출
            placeQueen(row + 1, N, chess, solution_cnt, cols, left_diags, right_diags)
            
            # 백트래킹: 퀸을 제거하고 상태를 복원 (다른 열에 퀸을 놓을 수 있도록)
            cols[col] = left_diags[row - col + N - 1] = right_diags[row + col] = False

# 메인 함수
def main():
    # 사용자로부터 체스판의 크기 N을 입력받음
    N = int(input())
    # 퀸이 놓인 각 행의 열 위치를 저장할 배열 초기화 (-1로 초기화하여 아직 퀸이 놓이지 않았음을 표시)
    chess = [-1] * N
    # 가능한 해결 방법의 수를 저장할 리스트 (값을 참조 및 수정할 수 있도록 리스트 형태로 선언)
    solution_cnt = [0]

    # 퀸이 놓인 열, 왼쪽 대각선, 오른쪽 대각선에 대한 충돌 체크를 위한 배열 초기화
    cols = [False] * N  # 각 열에 퀸이 놓였는지 여부
    left_diags = [False] * (2 * N - 1)  # 왼쪽 대각선 체크 (row - col)
    right_diags = [False] * (2 * N - 1)  # 오른쪽 대각선 체크 (row + col)

    # 퀸을 배치하는 함수 호출 (처음에는 0번째 행부터 시작)
    placeQueen(0, N, chess, solution_cnt, cols, left_diags, right_diags)
    
    # 모든 경우의 수를 출력
    print(solution_cnt[0])

# 프로그램이 시작되는 부분
if __name__ == '__main__':
    main()