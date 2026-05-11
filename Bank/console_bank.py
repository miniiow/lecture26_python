class Account:
    def __init__(self, account_no, owner, balance):
        self.__account_no = account_no
        self.__owner = owner
        self.__balance = balance

    def __str__(self):
        return f'{self.__account_no}\t{self.__owner}\t{self.__balance}'
    
    def deposit(self, amount):      # 입금
        self.__balance += amount
    def whitdraw(self, amount):     # 출금
        self.__balance -= amount

    def get_account_no(self):
        return self.__account_no
    def get_owner(self):
        return self.__owner
    def get_balance(self):
        return self.__balance

class AccountService:
    def __init__(self):
        self.__account_list = []

    def create_account(self, account_no, owner, balance):
        account = Account(account_no, owner, balance)
        self.__account_list.append(account)
        return True
    def list_account(self):
        return self.__account_list
    def deposit(self, account_no, amount):
        for account in account_list:
            if account.get_account_no() == account_no:
                account.deposit(amount)
                break
        return True
    def whitdraw(self, account_no, amount):
        for account in account_list:
            if account.get_account_no() == account_no:
                account.whitdraw(amount)
                break
        return True


# 메뉴와 사용자 interaction에 따른 서비스 호출
def select_menu():
    print('====================================================')
    print(' 1.계좌생성 | 2.계좌목록 | 3.입금 | 4.출금 | 0.종료')
    print('====================================================')
    menu = int(input('>> 메뉴선택 : '))
    return menu

# accountServese
aservice = AccountService()

print()
print('=============== UJ Bank ===============')
while True:
    menu = select_menu()
    if menu == 0 : break
    elif menu == 1 :    # 계좌생성
        # 계좌번호, 예금주, 잔액 입력을 방아서 계좌 생성
        account_no = input('> 계좌번호 : ')
        owner = input('> 예금주 : ')
        balance = int(input('> 초기입금액 : '))

        if aservice.create_account(account_no, owner, balance):
            print(' 결과 : 계좌가 생성되었습니다.')

    elif menu == 2:     # 계좌목록
        account_list = aservice.list_account()
        print('-----------')
        print('계좌목록')
        print('-----------')
        for account in account_list:
            print(account)

    elif menu == 3:     # 입금
        account_list = aservice.list_account()
        print('-----------')
        print(' 예금')
        print('-----------')
        account_no = input('> 계좌번호 : ')
        amount = int(input('> 예금액 : '))
        if aservice.deposit(account_no, amount):
            print('결과: 입금이 성공되었습니다.')

    elif menu == 4:     # 출금
        account_list = aservice.list_account()
        print('-----------')
        print(' 출금')
        print('-----------')
        account_no = input('> 계좌번호 : ')
        amount = int(input('> 출금액 : '))
        if aservice.whitdraw(account_no, amount):
            print('결과: 출금이 성공되었습니다.')
    else:
        print('\n[오류] 메뉴에 없는 숫자를 입력하셨습니다.\n다시 입력해주세요')
        continue


print('\n======= 이용해 주셔서 감사합니다. =======\n')