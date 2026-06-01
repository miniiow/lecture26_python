from Member.member import Member
from Member.member_dao import MemberDAO
from Member.member_service import MemberService
from Account.account import Account
from Account.account_dao import AccountDAO
from Account.acount_service import AccountService

class ConsoleBank:
    START_MENU = ['종료', '로그인', '회원가입']   # 시작메뉴
    BANKING_MENU = ['로그아웃', '계좌목록', '입금', '출금', '계좌생성', '계좌해지', '내정보']   # 회원메뉴(은행메뉴)
    MEMBER_MYINFO_MENU = ['돌아가기','비밀번호수정', '회원탈퇴']   # 내 정보 메뉴
    ADMIN_MENU = ['로그아웃','회원관리', '계좌관리']   # 관리자 메뉴
    ADMIN_ACCOUNT_MENU = ['돌아가기','전체계좌목록', '회원별계좌목록', '회원강퇴'] # 계좌관리 메뉴
    ADMIN_MEMBER_MENU = ['돌아가기', '회원목록', '회원정보조회']    # 회원관리 메뉴

    def __init__(self):
        self.msv = MemberService(MemberDAO())
        self.asv = AccountService(AccountDAO())

    def main(self):
        self.show_welcome()
        self.run_start_menu()
    
    # 시작메뉴
    def run_start_menu(self):
        while True:
            self.select_menu(ConsoleBank.START_MENU)
            menu = int(input('> 메뉴입력 : '))
            if menu == 0: break # 종료
            elif menu == 1: # 로그인
                self.menu_login()
            elif menu == 2: # 회원가입
                self.menu_join()
            else:
                print('없는 메뉴입니다.')
        self.say_goodbye()
    
    # 회원메뉴(은행메뉴)
    def run_banking_menu(self):
        title = '회원메뉴'
        print(self.print_title_line(title))
        while True:
            if self.msv.current_user is None:
                return
            self.select_menu(ConsoleBank.BANKING_MENU)
            menu = int(input('> 메뉴입력 : '))
            if menu == 0:   # 로그아웃
                self.menu_logout()
                return
            elif menu == 1: # 계좌목록
                self.menu_list_my_accounts()
            elif menu == 2: # 입금
                self.menu_deposit()
            elif menu == 3: # 출금
                self.menu_withdraw()
            elif menu == 4: # 계좌생성
                self.menu_create_account()
            elif menu == 5: # 계좌해지
                self.menu_delete_account()
            elif menu == 6: # 내정보
                self.run_my_info_menu()
            else:
                print('없는 메뉴입니다.')

    # 관리자메뉴    
    def run_admin_menu(self):
        title = '관리자 메뉴'
        print(self.print_title_line(title))
        while True:
            if self.msv.current_user is None:
                return
            self.select_menu(ConsoleBank.ADMIN_MENU)
            menu = int(input('> 메뉴입력 : '))
            if menu == 0:
                self.menu_logout()
                return
            elif menu == 1: # 회원관리
                self.menu_manage_members()
            elif menu == 2: # 계좌관리
                self.menu_manage_accounts()
            else:
                print('없는 메뉴입니다.')
    
    # 내정보메뉴
    def run_my_info_menu(self):
        title = '내정보 메뉴'
        print(self.print_title_line(title))
        while True:
            if self.msv.current_user is None:
                return
            self.select_menu(ConsoleBank.MEMBER_MYINFO_MENU)
            menu = int(input('> 메뉴입력 : '))
            if menu == 0:   # 돌아가기
                return
            elif menu == 1: # 비밀번호 수정
                self.menu_update_password()
            elif menu == 2: # 회원탈퇴
                self.menu_delete_membership()
            else:
                print('없는 메뉴입니다.')


    # 관리자-계좌메뉴
    def run_admin_account_menu(self):
        title = '관리자-계좌메뉴'
        print(self.print_title_line(title))

    # 관리자-회원관리메뉴
    def run_admin_member_menu(self):
        title = '관리자-회원관리메뉴'
        print(self.print_title_line(title))
       

    def menu_join(self): # 회원가입
        id = input('> 아이디 입력 : ')
        password = input('> 비밀번호 입력 : ')
        name = input('> 회원명 입력 : ')
        member = Member(id, password, name)
        if self.msv.join(member):
            print('회원가입이 완료되었습니다.')
        else:
            print('회원가입에 실패하였습니다.')

    def menu_login(self): # 로그인
        id = input('> 아이디 입력 : ')
        password = input('> 비밀번호 입력 : ')
        if self.msv.login(id, password):
            if self.msv.current_user == MemberService.ADMIN_ID:
                self.run_admin_menu()   # 관리자메뉴 이동
            else:
                self.msv.current_user = id
                self.run_banking_menu() # 일반회원메뉴 이동
        else:
            print('로그인에 실패하였습니다.')


    def menu_logout(self): # 로그아웃
        return self.msv.logout()

    def menu_list_my_accounts(self): # 계좌목록
        # 회원에게 계좌 있는지 먼저 확인 후 계좌목록 출력하기
        account_list = self.asv.get_members_accounts(self.msv.current_user)
        if account_list != None:
            for account in account_list:
                print(account)
        else:
            print('생성된 계좌가 없습니다.')

    def menu_deposit(self): # 입금
        account_no = input('> 계좌번호 입력 : ')
        amount = int(input('> 입금금액 입력 : '))
        if self.asv.deposit(account_no, amount):
            return print('입금 성공')
        return print('입금 중 문제발생')

    def menu_withdraw(self): # 출금
        account_no = input('> 계좌번호 입력 : ')
        amount = int(input('> 출금금액 입력 : '))
        password = input('> 비밀번호 입력 : ')
        try:
            if self.asv.withdraw(self.msv.current_user, account_no, amount, password):
                return print('출금 완료')
        except ValueError:
            print('계좌 잔액보다 더 많은 금액을 출금할 수 없습니다.')
        except Exception:
            print('출금 중 문제발생')

    def menu_create_account(self): # 계좌생성
        owner = input('> 예금자명 입력 : ')
        balance = int(input('> 초기 예금액 입력 : '))
        password = input('> 비밀번호 설정 : ')
        account = Account(0, owner, balance, password, self.msv.current_user)
        if self.asv.create_account(account):
            return print('계좌생성 성공')
        return print('계좌생성 중 문제발생')
        
    def menu_delete_account(self): # 계좌해지
        account_no = input('> 계좌번호 입력 : ')
        password = input('> 비밀번호 입력 : ')
        if self.asv.delete_account(self.msv.current_user, account_no, password):
            return print('계좌해지 성공')
        return print('계좌해지 중 문제발생')
        
    def menu_myinfo(self):  # 내정보 ?
        pass
    def menu_view_myinfo(self): # 내정보보기
        pass

    def menu_update_password(self): # 비밀번호 수정
        id = input('> 아이디 입력 : ')
        org_password = input('> 기존 비밀번호 입력 : ')
        new_password = input('> 새 비밀번호 입력 : ')
        if self.msv.update_member_password(id, org_password, new_password):
            print('비밀번호 수정 성공')
        else:
            print('비밀번호 수정 중 문제발생')

    def menu_delete_membership(self): # 회원탈퇴
        if self.msv.remove_member(self.msv.current_user):
            print('회원탈퇴 완료')
            self.menu_logout()
            return
        else:
            print('회원탈퇴 중 문제발생')

    
    def menu_manage_members(self):  # 관리자-회원관리
        return print('관리자-회원관리')
    def menu_manage_accounts(self): # 관리자-계좌관리
        return print('관리자-계좌관리')

    
    def menu_list_all_accounts(self): # 전체계좌목록
        pass

    def menu_list_member_accounts(self): # 회원별계좌목록
        pass

    
    def menu_list_members(self): # 회원목록
        pass
    def menu_view_member_info(self): # 회원정보조회
        pass
    def menu_delete_member(self): # 회원강퇴
        pass


    def show_welcome(self):
        title = 'Welcome ConsoleBank'
        print(self.print_title_line(title))

    def say_goodbye(self):
        print('안녕히 가세요.')

    def print_title_line(self, title):
        return f"{'=' * 50}\n{title:^50}\n{'='*50}"
    
    def select_menu(self, menu_list):
        print('-' * 50)
        for i in range(1, len(menu_list)):
            print(f'{i}. {menu_list[i]}')
        print(f'0. {menu_list[0]}')

        print('-' * 50)


if __name__ == '__main__':
    app = ConsoleBank()
    app.main()