from member import Member
from member_dao import MemberDAO
from member_service import MemberService

class MemberManager:
    START_MENU = ['종료','로그인','회원가입']
    ADMIN_MENU = ['로그아웃', '회원목록','회원정보조회','회원탈퇴']
    MEMBER_MENU = ['로그아웃','내정보조회','내정보수정','회원탈퇴']
   
    
    def __init__(self):
        # DB에 대한 의존성 주입
        self.ms = MemberService(MemberDAO())
    
    def main(self):
        self.show_welcome()
        
        while True:
            menu = self.select_menu(MemberManager.START_MENU)
            if menu == 0: break
            elif menu == 1: # 로그인
                id = input('>> id : ')
                password = input('>> password : ')

                if self.ms.login(id, password):
                    if self.ms.current_user == MemberService.ADMIN_ID:
                        self.start_admin_menu()
                    else:
                        self.ms.current_user = id
                        self.start_member_menu()
                else:
                    print('로그인에 실패하였습니다.')

            elif menu == 2: # 회원가입
                id = input('>> id : ')
                password = input('>> password : ')
                name = input('>> name : ')
                member = Member(id, password, name)
                if self.ms.join(member):
                    print('회원가입이 완료되었습니다.')
                else:
                    print('회원가입에 실패하였습니다.')
            else: # 예외
                print('없는 메뉴입니다.')
        self.say_goodbye()

    # 관리자 메뉴
    def start_admin_menu(self):
        title = '관리자메뉴'
        print(self.print_title(title))
        while True:
            menu = self.select_menu(MemberManager.ADMIN_MENU)
            if menu == 0:
                self.ms.logout()
                break
            elif menu == 1: # 회원목록
                self.list_all_member()
            elif menu == 2: # 회원정보조회
                id = input('>> id : ')
                member_info = self.ms.view_member_info(id)
                if member_info:
                    # 비밀번호 제외한 회원목록
                    print(f'{member_info.get_id()}\t{member_info.get_name()}')
                else:
                    print('없는 회원입니다.')
            elif menu == 3: # 회원강퇴
                id = input('>> id : ')
                if self.ms.remove_member(id):
                    print('회원강퇴가 완료되었습니다.')
                else:
                    print('없는 회원입니다.')
            else:
                print('없는 메뉴입니다.')

    # 회원 메뉴
    def start_member_menu(self):
        title = '회원메뉴'
        print(self.print_title(title))
        while True:
            menu = self.select_menu(MemberManager.MEMBER_MENU)
            if menu == 0:
                self.ms.logout()
                break
            elif menu == 1: # 회원정보조회
                member_info = self.ms.view_member_info(self.ms.current_user)
                if member_info:
                    print(member_info)
                else:
                    print('없는 회원입니다.')
            elif menu == 2: # 회원정보수정
                member_info = self.ms.view_member_info(self.ms.current_user)
                if member_info:
                    password = input('>> password : ')
                    member_info.set_password(password)
                    if self.ms.update_member_info(self.ms.current_user, member_info):
                        print('회원수정이 완료되었습니다.')
                    else:
                        print('회원수정에 실패하였습니다.')
            # ==========================
            # 비밀번호 수정 메뉴 만들기
            # ==========================
            elif menu == 3: # 회원탈퇴
                self.ms.remove_member(self.ms.current_user)
                self.ms.current_user = None
                print('회원탈퇴가 완료되었습니다.')
                break
            else:
                print('없는 메뉴입니다.')


    def list_all_member(self):
            print(self.ms.current_user)
            if self.ms.current_user !=  MemberService.ADMIN_ID:
                print('사용권한이 없습니다.')
                return
            
            # 관리자 정보 빼고 모든 멤버 정보 반환
            member_list = self.ms.list_members()
            if len(member_list) <= 1:
                print('가입한 회원이 없습니다.')
            else:
                for member in member_list[1:]:
                    print(member) 

    def show_welcome(self):
        title = 'YJ Member Manager'
        print(self.print_title(title))

    def print_title(self, title):
        return f"{'=' * 50}\n{title:^50}\n{'='*50}"

    def say_goodbye(self):
        print('안녕히 가세요.')

    def print_menu(self, menu_list):
        print('-' * 50)
        for i in range(1, len(menu_list)):
            print(f'{i}. {menu_list[i]}')
        print(f'0. {menu_list[0]}')
        print('-' * 50)

    def select_menu(self, menu_list):
        self.print_menu(menu_list)
        try:
            menu = int(input('메뉴 선택 : '))
            return menu
        except ValueError:
            return -1

if __name__ == '__main__':
    app = MemberManager()
    app.main()