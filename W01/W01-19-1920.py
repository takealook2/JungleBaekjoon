# 입력은 총 4 번

# 첫번째 입력: 자연수 N(리스트의 크기를 결정)
# 두번째 입력: N개의 정수(리스트 안에 들어갈 원소)
# 세번째 입력: M개의 수
# 네번째 입력: 리스트[M]에 들어갈 원소

N = int(input())
A = []
A = list(map(int, input().split()))

M = int(input())
key = []
key = list(map(int, input().split()))


# 입력받은 A 리스트를 정렬
A.sort()

# 이진탐색 함수 정의
def binarySearch(A, key, low, high):
    mid = (low+high)//2

    if high < low:
        return 0

    if A[mid] > key:
        return binarySearch(A, key, 0, mid-1)
    elif A[mid] < key:
        return binarySearch(A, key, mid+1, high)
    else:
        return 1
        


# 정렬된 A 리스트에서 key 리스트를 찾는 이진탐색 실행
for k in key:
    result = binarySearch(A, k, 0, N-1)
    print(result)