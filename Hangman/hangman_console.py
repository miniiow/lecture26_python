from hangman import Hangman

print()
print('========== Hangman ==========')
word_list = ['apple', 'banana', 'man', 'woman', 'tomato']
hangman = Hangman(word_list)
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
        pass

    # 승패 확인
    if result == Hangman.WIN:
        print(f'승리 : {hangman.num_try}회 시도')
        break
    elif result == Hangman.LOOSE:
        print(f'패배 : {hangman.word}')
        break
    