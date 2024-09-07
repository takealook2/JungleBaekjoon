import math

def find_prime_pair(even):
    if even % 2 != 0:
        return None

    # 소수 판별
    array = [True] * (even + 1)
    array[0] = False
    array[1] = False

    # 에라토스테네스의 체 : 소수 판별
    for i in range(2, int(math.sqrt(even)) + 1):
        if array[i]:
            for j in range(i * i, even + 1, i):
                array[j] = False

    best_pair = None
    min_diff = float('inf')

    # 두 소수의 차이가 가장 작은 경우를 찾음
    for i in range(2, even // 2 + 1):
        if array[i] and array[even - i]:
            diff = abs(i - (even - i))
            if diff < min_diff:
                min_diff = diff
                best_pair = (i, even - i)

    return best_pair

# 여러 입력 처리
while True:
    try:
        even = int(input())
        pair = find_prime_pair(even)
        if pair:
            print(pair[0], pair[1])
        else:
            None
    except:
        break  # 입력이 더 이상 없으면 종료
