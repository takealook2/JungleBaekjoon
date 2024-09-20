import sys
 
# 전위 탐색
def preorder(root, tree):
    if root != '.':
        print(root, end='') # 루트
        preorder(tree[root][0], tree) # 왼쪽 자식  
        preorder(tree[root][1], tree) # 오른쪽 자식
 
# 중위 탐색
def inorder(root, tree):
    if root != '.':
        inorder(tree[root][0], tree) # 왼쪽 자식
        print(root, end='') # 루트
        inorder(tree[root][1], tree) # 오른쪽 자식
 
# 후위 탐색
def postorder(root, tree):
    if root != '.':
        postorder(tree[root][0], tree) # 왼쪽 자식
        postorder(tree[root][1], tree) # 오른쪽 자식
        print(root, end='') # 루트
 
def main():
    N = int(sys.stdin.readline().strip())
    tree = {}
    
    for _ in range(N):
        root, left, right = sys.stdin.readline().strip().split()
        tree[root] = [left, right]

    preorder('A', tree)
    print()
    inorder('A', tree)
    print()
    postorder('A', tree)

if __name__ == "__main__":
    main()