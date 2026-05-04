# 1. 컴퓨터가 숫자를 생각한다 (1~50)
# 2. 사용자 숫자를 말한다
# 3. 숫자가 맞으면 사용자 win
# 4. 틀리면 컴퓨터가 up, down을 알려준다
# 5. 2~4번 까지 7번 반복
# 6. 7번 내에 맞추기 못하면 computer win

import random

limit = 50
turn = 7
count = 0
com_num = random.randint(1, limit)
# print('컴퓨터 숫자 : ', com_num)

print('|| 숫자 맞추기 게임 ||')
print(f'1부터 {limit}까지의 숫자 중')
print(f'{turn}안에 숫자를 맞춰야 합니다')

while count < turn:
    user_num = int(input(' >> 숫자입력 : '))
    if com_num < user_num:
        print('[system] Down...')
    elif com_num > user_num:
        print('[system] Up...')
    else:
        print(f'{count}번 만에 이겼당 !!!')
        break
    count += 1
print('졌당 !')