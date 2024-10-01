import sys

import sys

def fibo(n, fibo_list):
    # n이 0일 경우도 처리
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # n 크기에 맞게 리스트 초기화
    fibo_list[0] = 0
    fibo_list[1] = 1

    for i in range(2, n + 1):
        fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]
    return fibo_list[n]

def main():
    n = int(sys.stdin.readline().strip())
    
    # 리스트 크기를 n + 1로 초기화
    fibo_list = [0] * (n + 1)
    
    # 피보나치 값 계산
    result = fibo(n, fibo_list)
    
    # 결과 출력
    print(result)

if __name__ == "__main__":
    main()
