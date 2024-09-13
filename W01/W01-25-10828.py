import sys

def push(X, stack):
    stack.append(X)

def pop(stack):
    # 정수를 스택에서 제거한다는 건 어떤 의미일까?
    # 그 스택의 값이 None이 된다는 의미? > 이건 아닌 거 같다 ㅋㅋ;
    # 파이썬 메서드가 있었다... pop()
    if not stack:
        print(-1)
    else:
        print(stack.pop())

def size(stack):
    print(len(stack))

def empty(stack):
    if not stack:
        print(1)
    else:
        print(0)

def top(stack):
    if not stack:
        print(-1)
    else:
        print(stack[-1])

def command_oper(command, command_arr, stack):
    if command == "push":
        X = int(command_arr[1])
        push(X, stack)
    elif command == "pop":
        pop(stack)
    elif command == "size":
        size(stack)
    elif command == "empty":
        empty(stack)
    elif command == "top":
        top(stack)

def main():
    N = int(sys.stdin.readline())
    stack = []
    for i in range(N):
        command_str = sys.stdin.readline().rstrip()
        command_arr = command_str.split()
        command = command_arr[0]

        command_oper(command, command_arr, stack)


if __name__ == "__main__":
    main()