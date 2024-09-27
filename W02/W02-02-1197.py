import sys
sys.setrecursionlimit(10**6)

def find(x):
    global parent
    if parent[x] == x:
        return x
    else:
        return find(parent[x])
    
def union(x, y):
    pX, pY = find(x), find(y)
    if pX > pY:
        parent[pX] = pY
    else:
        parent[pY] = pX

V, E = map(int, sys.stdin.readline().split())
arr, parent = [], [i for i in range(V)] # 파이썬 리스트 컴프리헨션

for _ in range(E):
    v1, v2, dist = map(int, sys.stdin.readline().split())
    arr.append((dist, v1-1, v2-1))
arr.sort()

mst = 0
for a in arr:
    if find(a[1]) == find(a[2]):
        continue
    union(a[1], a[2])
    mst += a[0]

print(mst)
