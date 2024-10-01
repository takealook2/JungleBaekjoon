import sys
input = sys.stdin.readline

def main():
    # 이전 게 낫냐 지금 게 낫냐
    # 지금 게 나으면 갱신한다
    n, k = map(int, input().strip().split())
    w = []
    p = []
    dp = [[0]*(k+1) for _ in range(n+1)]

    for _ in range(n):
        weight, profit = map(int, input().strip().split())
        w.append(weight)
        p.append(profit)

    for i in range(1, n+1):
        for j in range(1, k+1):
            if w[i-1]<=j:
                dp[i][j]=max(dp[i-1][j], dp[i-1][j-w[i-1]]+p[i-1])
            else:
                dp[i][j]=dp[i-1][j]
    
    print(dp[n][k])

if __name__ == "__main__":
    main()