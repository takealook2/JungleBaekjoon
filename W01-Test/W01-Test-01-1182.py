# 정수의 개수 N과 정수 S 입력
N, S = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

# 부분수열의 합을 찾는 재귀 함수
def find_subsequences(idx, current_sum):
    global count
    # 배열의 끝에 도달한 경우
    if idx == N:
        # 현재까지의 합이 S와 같다면 카운트 증가
        if current_sum == S:
            count += 1
        return
    
    # 현재 인덱스를 포함하지 않는 경우
    find_subsequences(idx + 1, current_sum)
    
    # 현재 인덱스를 포함하는 경우
    find_subsequences(idx + 1, current_sum + arr[idx])

# 첫 번째 호출 (idx 0에서 시작)
find_subsequences(0, 0)

# 합이 0인 경우 공집합이 포함되므로 공집합을 제외
if S == 0:
    count -= 1

# 결과 출력 
print(count)