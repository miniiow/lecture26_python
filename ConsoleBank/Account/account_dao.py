from Account.account import Account

class AccountDAO:
    def __init__(self):
        self.__accountDB = {} # 계좌번호: account 객체

    # 계좌등록
    def insert_account(self, account):
        account_no = account.get_account_no()
        # DB에 입력한 account_no가 없으면 등록
        if account_no not in self.__accountDB:
            self.__accountDB[account_no] = account
            return True
        return False

    def select_account_by_account_no(self, account_no):
        if account_no in self.__accountDB.keys():
            return self.__accountDB[account_no]
        return None

    def select_accounts_by_member_id(self, member_id):
        account_list = []
        for account in self.__accountDB.values():
            if account.get_member_id() == member_id:
                account_list.append(account)
        if len(account_list):
            return account_list
        return None
    
    def select_all_accounts(self):
        account_list = list(self.__accountDB.values())
        if account_list:
            return account_list
        return None

    # 계좌수정
    def update_account(self, account_no, account):
        if account_no in self.__accountDB:
            self.__accountDB[account_no] = account
            return True
        return False

    # 계좌삭제
    def delete_account(self, account_no):
        if account_no in self.__accountDB:
            self.__accountDB.pop(account_no)
            return True
        return False



if __name__ == '__main__':
    dao = AccountDAO()
    ac_list = dao.select_all_accounts()
    print(ac_list)
    dao.insert_account(Account('111111', '유징', 10000, '1234'))
    dao.insert_account(Account('123123', '유징징', 5000, '1234'))
    for account in dao.select_all_accounts():
        print(account)
    print(dao.select_account_by_account_no('111111'))
    print()
    for account in dao.select_accounts_by_member_id('유징징'):
        print(account)
    dao.update_account('123123', Account('123123', '유징징', 25000, '1234'))
    print(dao.select_account_by_account_no('123123'))
    print()
    dao.delete_account('123123')
    print(dao.select_account_by_account_no('123123'))