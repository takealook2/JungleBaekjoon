import sys
input = sys.stdin.readline

def all_coin(n, coin, cost):
    dp = [0]*(cost+1)
    dp[0] = 1

    for c in coin:
        for i in range(c, cost+1):
            dp[i]+=dp[i-c]

    print(dp[cost])

def main():

    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())
        coin = list(map(int, input().strip().split()))
        cost = int(input().strip())
        all_coin(n, coin, cost)

if __name__ == "__main__":
    main()