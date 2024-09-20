import sys
sys.setrecursionlimit(10**9)

nums = []
while True:
    try:
        nums.append(int(sys.stdin.readline()))
    except:
        break

def postorder(start, end):
    if start > end:
        return # start > end 인 경우에는 탐색할 노드가 없음?
    
    # 오른쪽 서브트리의 시작점을 찾는 코드
    mid = end + 1 # 오른쪽 서브트리가 없을 때를 기본값으로 설정
    for i in range(start+1, end+1): # root 노드보다 큰 값이 나오는 위치를 찾음
        if nums[start] < nums[i]:
            mid = i # 오른쪽 서브트리의 시작점이 됨
            break

    postorder(start+1, mid-1)
    postorder(mid, end)
    print(nums[start])

postorder(0, len(nums)-1)