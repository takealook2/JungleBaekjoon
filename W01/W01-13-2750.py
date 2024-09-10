from typing import MutableSequence

# 퀵소트 구현 함수
def quickSort(array: MutableSequence, left: int, right: int) -> None:
    pl = left
    pr = right
    x = array[(left + right) // 2]  # 피봇 설정

    while pl <= pr:
        while array[pl] < x:
            pl += 1
        while array[pr] > x:
            pr -= 1

        if pl <= pr:
            array[pl], array[pr] = array[pr], array[pl]
            pl += 1
            pr -= 1

    if left < pr:
        quickSort(array, left, pr)
    if pl < right:
        quickSort(array, pl, right)

# 초기 함수 설정
def quick_sort(array: MutableSequence) -> None:
    quickSort(array, 0, len(array) - 1)

# N 개의 수를 받음, 이때 N 은 1<=N<=1000
num = int(input())

# N 개의 배열을 생성
if 1 <= num <= 1000:
    array = []
    
    # N 개의 배열 안에 N 번 수를 받음
    for i in range(num):
        array.append(int(input()))

    # 중복된 값 제거
    array_unique = list(set(array))

    # 절대값 1000 이하인지 확인하고 정렬
    if all(abs(x) <= 1000 for x in array_unique):
        quick_sort(array_unique)

    # 정렬된 배열 출력
    for i in array_unique:
        print(i)