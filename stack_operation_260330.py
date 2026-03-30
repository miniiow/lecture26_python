# 손코딩 시험 범위(열심히 연습할 것!!!!)

stack = []
capacity = 5

def isFull():
    if len(stack) == capacity:
        return True
    else:
        return False

def push(data):
    if isFull():
        print("> Stack이 차 있어서 더 이상 추가할 수 없습니다.")
    else:
        stack.append(data)

def isEmpty():
    if len(stack) == 0:
        return True
    else:
        return False

def pop():
    if isEmpty():
        print('> Stack이 비어 있습니다.')
    else:
        return stack.pop()
    
def peek():
    if isEmpty():
        print('Stack이 비어 있습니다.')
    else:
        print('> 가져올 데이터 :', stack[len(stack)-1])


# ===========================================================
print(f'[[  정수형 스택 연산 실습 (용량 5)  ]]')
while True:
    print('==================================')
    print('  1.Push  2.Pop  3.Peek  0.Exit')
    print('==================================')
    menu = int(input('> 메뉴 선택 : '))
    if menu == 0:
        break
    elif menu == 1:
        data = int(input('> 데이터 입력 : '))
        push(data)
    elif menu == 2:
        data = pop()
        print('> 가져온 데이터 :', data)
    elif menu == 3:
        peek()

    print('> 현재 스택 상태 ', stack)

print('[[ 정수형 스택 연산 실습 종료]]')