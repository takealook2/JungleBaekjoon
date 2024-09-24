import sys
sys.setrecursionlimit(10**9)

nums = []
while True:
    try:
        nums.append(int(sys.stdin.readline()))  # 전위 순회 입력값을 받음
    except:
        break  # 입력이 끝나면 반복을 종료함

def postorder(start, end):
    if start > end:
        return  # start > end인 경우에는 탐색할 노드가 없으므로 리턴
    
    # 오른쪽 서브트리의 시작점을 찾는 코드
    right_start = end + 1  # 기본값: 오른쪽 서브트리가 없을 경우
    
    for i in range(start+1, end+1):  # 루트 노드보다 큰 값이 나오는 첫 번째 위치를 찾음
        if nums[start] < nums[i]:
            right_start = i  # 처음으로 루트보다 큰 값을 찾으면 그게 오른쪽 서브트리의 시작
            break

    # 왼쪽 서브트리 처리 (start+1 ~ right_start-1 범위)
    postorder(start+1, right_start-1)

    # 오른쪽 서브트리 처리 (right_start ~ end 범위)
    postorder(right_start, end)

    # 후위 순회이므로 마지막에 루트 노드를 출력
    print(nums[start])

postorder(0, len(nums)-1)  # 트리 전체에 대해 후위 순회 수행