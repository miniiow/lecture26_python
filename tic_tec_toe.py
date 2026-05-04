

# Random 모듈
# random.choice(시퀀스) : 리스트 등에서 무작위로 요소 하나를 선택함
# random.sample(시퀀스, k) : 중복 없이 k개의 요소를 무작위로 추출함

# 1. 자료구조
# 화면에 보여줄 보드
board_screen = ' 0 | 1 | 2 \n 3 | 4 | 5 \n 6 | 7 | 8'

board = [" "] * 9 # 게임의 진행 상태
board_blank = set(range(9))     # 빈 set 자료형태  0~8까지 생성
# 이겼을 때의 상태
win_status = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
              (0, 3, 6), (1, 4, 7), (2, 5, 8),
              (0, 4, 8), (2, 4, 6)]
human = 'O'
computer = 'X'

# 2. 필요한 함수 정의
def showBoard():
    print(board_screen)

def updateGame(who, number):
    global board, board_screen
    board[number] = who
    board_screen = board_screen.replace(str(number), who)
    # User가 선택한 숫자 갱신
    # .remove()사용하게되면 컴퓨터 턴에 에러발생하기 때문에 discard()사용함
    board_blank.discard(number)
   # print(who, number)


# random표준 라이브러리 사용: random은 빌트인 라이브러리이기때문에 따로 설치할 필요 없음
import random
def getComputerNumber():
    # for i in range(len(board)):
    #     if board[i] == " ":
    #         return i
    if board_blank:
        # return board_blank.pop()    # 빈 칸 있으면 아무거나 하나 넘김
        # board_blank는 set이라 시퀀스가 아님 >> choice를 사용하기 위해 list로 형변환
        return random.choice(list(board_blank))
    return -1

def isWin(turn):
    for status in win_status:
        if board[status[0]] == board[status[1]] == board[status[2]] == turn:
            return True
    return False


# 3. 메인 로직
# 3-1. 필요한 자료구조 초기화
print('============ Tic-Tac-Toe =============')
# 3-2. 보드를 보여줌
showBoard()
while True:
    # 3-3. human 차례
    # human 입력 받아서 처리
    human_input = int(input(' >> 숫자를 입력하세요 : '))
    updateGame(human, human_input)
    showBoard()
    if isWin(human):
        print('You Win !')
        break

    # 3-4. 컴퓨터 차례
    # computer가 놓을 자리를 선택
    computer_input = getComputerNumber()
    if computer_input == -1:
        print('The gamed ended in a tie ~~~~~~~ !!!') # 비겼음
        break
    updateGame(computer, computer_input)
    print(' >> 컴퓨터의 선택 : ', computer_input)
    showBoard()
    if isWin(computer):
        # 컴퓨터가 이겼음
        print('You loose ~~~~~~~ !!!')
        break
