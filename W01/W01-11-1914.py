num = int(input())

if 1 <= num <= 100:
    if num > 20:
        total_moves = (2 ** num) - 1
        print(total_moves)  # 총 이동 횟수 먼저 출력
    else :
        total_moves = (2 ** num) - 1
        print(total_moves)  # 총 이동 횟수 먼저 출력
        def hanoi(n, a, b, c):
            if n == 1:
                print(a, c)
            else:
                hanoi(n-1, a, c, b)  # a에서 b로 옮기는 중간에 c를 거친다
                print(a, c)  # 가장 큰 원판을 목적지로 옮긴다
                hanoi(n-1, b, a, c)  # 중간에 옮겨진 원판들을 다시 목적지로 옮긴다

        # 하노이 탑 실행
        hanoi(num, "1", "2", "3")