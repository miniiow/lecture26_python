# 1. 컴퓨터가 영어단어를 생각 >> 해당 단어 글자 수 만큼 빈칸 보여주기
# 2. 사용자가 알파벳 입력
# 3. update Game
# 4. 맞으면 You win
# 5. 맞을때까지 반복
# 6. try 7번 넘었으면 You lose >> 7번 틀리면 죽음

import random

# 자료구조
def select_word():
    word_list = ['APPLE', 'BANANA', 'MAN']
    return random.choice(word_list)

limit_error = 7 # 목숨
num_error = 0   # 틀린횟수

# 게임 로직
# 1. com이 단어 선택해서 보여주기
target_word = select_word()
blank_char = '_'
word_screen = blank_char * len(target_word)

def update_screen(user_input, target_word, current_screen):
    # 알파벳이 단어에 있으면 채워주기
    for i in range(len(target_word)):
        if target_word[i] == user_input:
            current_screen = current_screen[:i] + user_input + current_screen[i+1:]
    print('정답 : ', current_screen)
    return current_screen

print(' [[ 행맨게임 ]]')
print('컴퓨터가 생각한단어 : ', target_word)
print(word_screen)
while num_error < limit_error:
    # 2. 사용자 알파벳 입력
    user_input = input(' >> 알파벳 입력 : ').upper()
     # 3. 게임 상태 업데이트
    if target_word.find(user_input) == -1:   # 없으면 오류 횟수 증가
        num_error += 1
        print(f'오답 개수 : {num_error}개')
    else:
        word_screen = update_screen(user_input, target_word, word_screen)

    # 4. 단어를 다 맞췄으면 사용자 
    # word_screen에 _가 없으면 단어를 다 맞췄다는 뜻 >> 사용자 win
    if word_screen.count(blank_char) == 0:
        print('You win !!!')
        break
# 5. 시도횠수가 limit_error 넘었으면 loose
if num_error >= limit_error:
    print('You loose ...  정답은 ', target_word)