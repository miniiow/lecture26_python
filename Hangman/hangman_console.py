from hangman import Hangman
# import hangman as hm

print()
print('========== Hangman ==========')

# def load_word_list():
#     word_list = ['APPLE', 'BANNA', 'MAN', 'WOMAN', 'TOMATO']
#     return word_list

filename = './hangman/voca.txt'

def load_word_list(filename):
    word_list = []
    with open(filename, encoding='utf-8') as f_read:
        for i in f_read:
            words = i.split()
            if words:
                word_list.append(words[0])
    return word_list

# hangman = Hangman(load_word_list())
hangman = Hangman(load_word_list(filename))

print(f'{hangman.display_word} {len(hangman.word)}글자')


while True:
    # 알파벳 입력
    letter = input('>> 알파벳 입력 : ')

    # 정답확인
    result = hangman.check_letter(letter)
    if result == Hangman.RIGHT:
        print(f'정답 : {hangman.display_word}')
    elif result == Hangman.WRONG:
        print(f'오답 : {hangman.num_try}회 시도')
    else:
        print(hangman.error_status)
        continue

    # 승패 확인
    result = hangman.is_win()
    if result == Hangman.WIN:
        print(f'승리 : {hangman.num_try}회 시도')
        break
    elif result == Hangman.LOOSE:
        print(f'패배 : {hangman.word}')
        break
    