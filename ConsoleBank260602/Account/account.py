class Account:
    # 정규화 및 나중에 DB연결 고려하여 생성할 것 >> 데이터들은 정규화로 통일하는 것이 좋다
    def __init__(self, account_no, owner, balance, password):
        self.__account_no = account_no
        self.__owner = owner
        self.__balance = balance
        self.__password = password


    def get_account_no(self):
        return self.__account_no
    def get_owner(self):
        return self.__owner
    def get_balance(self):
        return self.__balance
    def get_password(self):
        return self.__password
    
    def set_balance(self, balance):
        self.__balance = balance
    def set_account_no(self, account_no):
        self.__account_no = account_no

    def __str__(self):
        return f'계좌번호 = {self.__account_no} 계좌주 = {self.__owner} 잔액 = {self.__balance} 비밀번호 = {self.__password}'
    
if __name__ == '__main__':
    # 유닛 테스트(간략하게 확인)
    ac = Account(111111, '유징', 10000, '1234')
    print(ac)
    print(ac.get_account_no)
    print(ac.get_balence)
    print(ac.get_owner)
    print(ac.get_password)
    