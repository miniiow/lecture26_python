from Account.account import Account
from Account.account_dao import AccountDAO

class AccountService:
    # 클래스 변수 : 계좌번호
    # 생성규칙 : 6자리 숫자로된 문자열
    account_no_seq = 111111

    def __init__(self, account_dao):
        self.__dao = account_dao
    
    def create_account(self, account):
        # 계좌번호를 생성하여 반영
        account.set_account_no(str(AccountService.account_no_seq))
        AccountService.account_no_seq += 1
        return self.__dao.insert_account(account)

    def get_all_accounts(self):
        return self.__dao.select_all_accounts()

    def get_members_accounts(self, id):
        return self.__dao.select_accounts_by_member_id(id)
    
    # 잔액확인
    def get_account_balance(self, account_no):
        account = self.__dao.select_account_by_account_no(account_no)
        if account:
            return account.get_balance()
        else:
            return None

    # 입금
    # account의 잔액변경
    def deposit(self, account_no, amount):
        account = self.__dao.select_account_by_account_no(account_no)
        if account:
            new_balance = account.get_balance() + amount
            account.set_balance(new_balance)
            return self.__dao.update_account(account_no, account)
        return False

    # 출금
    def withdraw(self, id, account_no, amount, password):   # 입력한 id, pw 맞는지 확인
        # 마이너스 통장 지원 안함
        account = self.__dao.select_account_by_account_no(account_no)
        if account != None:
            # 입력한 id,pw가 다를경우 KeyError 예외 발생
            if account.get_member_id() != id or account.get_password() != password:
                raise KeyError
            new_balance = account.get_balance() - amount
            if new_balance < 0:
                raise ValueError
            account.set_balance(new_balance)
            return self.__dao.update_account(account_no, account)
        raise KeyError

    # 계좌해지
    def delete_account(self, id, account_no, password):
        # 등록된 계좌번호 있는지 확인 후, 있으면 account변수에 저장
        account = self.__dao.select_account_by_account_no(account_no)
        if not account :
            return False
        if account.get_member_id() != id or account.get_password() != password:
            raise KeyError
        return self.__dao.delete_account(account_no)
    
if __name__ == '__main__':
    aservice = AccountService(AccountDAO())
    # 서비스가 부르는 애는 계좌번호를 생성할 수 없다 > AccountService만 계좌번호를 생성할 수 있음
    aservice.create_account(Account(0,'유징', 10000, '1234'))
    aservice.create_account(Account(0,'유징징', 32500, '1234'))
    for account in aservice.get_all_accounts():
        print(account)
    print()
    for account in aservice.get_members_accounts('유징'):
        print(account)

    print('계좌조회')
    aservice.deposit('111111', 5000)
    for account in aservice.get_members_accounts('유징'):
        print(account)
    aservice.deposit('111118', 5000)
    for account in aservice.get_members_accounts('유징'):
        print(account)
    
    print('출금')
    for account in aservice.get_members_accounts('유징'):
        print(account)
    try:
        aservice.withdraw('유징', '111111', 50000000, '15151654')
    
    except KeyError:
        print('id 또는 pw 잘못 입력')
    except ValueError:
        print('출금할 금액이 부족합니다.')
    from account import Account