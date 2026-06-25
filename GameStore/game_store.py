from Member.member import Member
from Member.member_dao import MemberDAO
from Member.member_service import MemberService
from Game.game import Game
from Game.game_dao import GameDAO
from Game.game_service import GameService
from Purchase.purchase_dao import PurchaseDAO
from Purchase.purchase_service import PurchaseService

class GameStore:
    START_MENU = ['종료', '로그인', '회원가입', '게임 목록 조회']
    MEMBER_MENU = ['로그아웃', '게임 목록 조회', '게임 구매', '내 라이브러리', '내 정보']
    MY_INFO_MENU = ['돌아가기', '정보조회', '비밀번호 수정', '회원탈퇴']
    ADMIN_MENU = ['로그아웃', '회원 관리', '게임 관리', '라이브러리 관리']
    ADMIN_MEMBER_MENU = ['돌아가기', '회원 목록 조회', '회원 상세 조회', '회원 삭제']
    ADMIN_GAME_MENU = ['돌아가기', '게임 추가', '게임 수정', '게임 삭제']
    ADMIN_LIBRARY_MENU = ['돌아가기', '회원별 라이브러리 조회']

    def __init__(self):
        self.ms = MemberService(MemberDAO())
        self.gs = GameService(GameDAO())
        self.ps = PurchaseService(PurchaseDAO())

    def main(self):
        self.show_welcome()
        self.run_start_menu()
        self.say_goodbye()


    def run_start_menu(self):
        while True:
            menu = self.select_menu(GameStore.START_MENU)
            if menu == 0:   # 종료
                return
            elif menu == 1: # 로그인
                if self.menu_login():
                    if self.ms.is_admin():
                        self.run_admin_menu()
                    else:
                        self.run_member_menu()
            elif menu == 2: # 회원가입
                self.menu_join()
            elif menu == 3: # 게임 목록 조회
                self.menu_view_all_games()
            else:
                print('!!! 없는 메뉴입니다.')


    def run_member_menu(self):
        title = '회원 메뉴'
        print(self.print_title(title))
        while True:
            if self.ms.current_user is None:
                return
            menu = self.select_menu(GameStore.MEMBER_MENU)
            if menu == 0:   # 로그아웃
                self.menu_logout()
                return
            elif menu == 1: # 게임 목록 조회
                self.menu_view_all_games()
            elif menu == 2: # 게임 구매
                self.menu_buy_game()
            elif menu == 3: # 내 라이브러리
                self.menu_view_my_library()
            elif menu == 4: # 내 정보
                self.run_my_info_menu()
            else:
                print('!!! 없는 메뉴입니다.')


    def run_my_info_menu(self):
        title = '내 정보 메뉴'
        print(self.print_title(title))
        while True:
            if self.ms.current_user is None:
                return
            menu = self.select_menu(GameStore.MY_INFO_MENU)
            if menu == 0:   # 돌아가기
                return
            elif menu == 1: # 정보 조회
                self.menu_view_my_info()
            elif menu == 2: # 비밀번호 수정
                self.menu_update_password()
            elif menu == 3: # 회원탈퇴
                if self.menu_delete_membership():
                    return
            else:
                print('!!! 없는 메뉴입니다.')

    def run_admin_menu(self):
        title = '관리자 메뉴'
        print(self.print_title(title))
        while True:
            if self.ms.current_user is None:
                return
            menu = self.select_menu(GameStore.ADMIN_MENU)
            if menu == 0:   # 로그아웃
                self.menu_logout()
                return
            elif menu == 1: # 회원 관리
                self.run_admin_member_menu()
            elif menu == 2: # 게임 관리
                self.run_admin_game_menu()
            elif menu == 3: # 라이브러리 관리
                self.run_admin_library_menu()
            else:
                print('!!! 없는 메뉴입니다.')

    # 관리자-회원관리 메뉴
    def run_admin_member_menu(self):
        title = '관리자 - 회원 관리'
        print(self.print_title(title))
        while True:
            menu = self.select_menu(GameStore.ADMIN_MEMBER_MENU)
            if menu == 0:   # 돌아가기
                return
            elif menu == 1: # 회원 목록 조회
                self.menu_view_all_members()
            elif menu == 2: # 회원 상세 조회
                self.menu_view_member_info()
            elif menu == 3: # 회원 삭제
                self.menu_delete_member_admin()
            else:
                print('!!! 없는 메뉴입니다.')

    # 관리자-게임관리 메뉴
    def run_admin_game_menu(self):
        title = '관리자 - 게임 관리'
        print(self.print_title(title))
        while True:
            menu = self.select_menu(GameStore.ADMIN_GAME_MENU)
            if menu == 0:   # 돌아가기
                return
            elif menu == 1: # 게임 추가
                self.menu_add_game()
            elif menu == 2: # 게임 수정
                self.menu_update_game()
            elif menu == 3: # 게임 삭제
                self.menu_delete_game()
            else:
                print('!!! 없는 메뉴입니다.')

    # 관리자-라이브러리관리 메뉴
    def run_admin_library_menu(self):
        title = '관리자 - 라이브러리 관리'
        print(self.print_title(title))
        while True:
            menu = self.select_menu(GameStore.ADMIN_LIBRARY_MENU)
            if menu == 0:   # 돌아가기
                return
            elif menu == 1: # 회원별 라이브러리 조회
                self.menu_view_member_library()
            else:
                print('!!! 없는 메뉴입니다.')


    def menu_join(self):
        id = input('> 아이디 : ')
        password = input('> 비밀번호 : ')
        name = input('> 이름 : ')
        member = Member(None, id, password, name)
        if self.ms.join_member(member):
            print('!!! 회원가입이 완료되었습니다.')
        else:
            print('!!! 이미 사용 중인 아이디입니다.')

    def menu_login(self):
        id = input('> 아이디 : ')
        password = input('> 비밀번호 : ')
        if self.ms.login(id, password):
            member = self.ms.get_member_info(id)
            print(f'!!! {member.get_name()}님 환영합니다.')
            return True
        print('!!! 아이디 또는 비밀번호가 일치하지 않습니다.')
        return False

    def menu_logout(self):
        self.ms.logout()
        print('!!! 로그아웃되었습니다.')


    def menu_view_all_games(self):
        games = self.gs.get_all_games()
        if not games:
            print('!!! 등록된 게임이 없습니다.')
            return
        print('-' * 50)
        for game in games:
            print(game)
        print('-' * 50)


    def menu_buy_game(self):
        games = self.gs.get_all_games()
        if not games:
            print('!!! 등록된 게임이 없습니다.')
            return
        print('-' * 50)
        for game in games:
            print(game)
        print('-' * 50)

        game_no = input('> 구매할 게임번호 : ')
        game = self.gs.get_game_info(game_no)
        if not game:
            print('!!! 해당 게임이 존재하지 않습니다.')
            return

        # 현재 로그인한 회원 정보
        member = self.ms.get_member_info(self.ms.current_user)
        member_no = member.get_member_no()

        # 이미 구매한 게임 확인
        if self.ps.is_purchased(member_no, game_no):
            print('!!! 이미 보유 중인 게임입니다.')
            return

        if self.ps.buy_game(member_no, game_no):
            print(f'!!! [{game.get_title()}] 구매가 완료되었습니다. 라이브러리에서 확인하세요.')
        else:
            print('!!! 구매에 실패하였습니다.')


    def menu_view_my_library(self):
        member = self.ms.get_member_info(self.ms.current_user)
        member_no = member.get_member_no()

        purchases = self.ps.get_my_library(member_no)
        if not purchases:
            print('!!! 보유 중인 게임이 없습니다.')
            return

        print('-' * 50)
        print(f'[{member.get_name()}님의 라이브러리]')
        print('-' * 50)
        for purchase in purchases:
            game = self.gs.get_game_info(purchase.get_game_no())
            if game:
                print(game)
        print('-' * 50)


    def menu_view_my_info(self):
        member = self.ms.get_member_info(self.ms.current_user)
        if member:
            print(member)
        else:
            print('!!! 회원 정보를 찾을 수 없습니다.')

    def menu_update_password(self):
        org_password = input('> 현재 비밀번호 : ')
        new_password = input('> 새 비밀번호 : ')
        if self.ms.modify_member_password(self.ms.current_user, org_password, new_password):
            print('!!! 비밀번호가 변경되었습니다.')
        else:
            print('!!! 비밀번호 변경에 실패하였습니다.')

    def menu_delete_membership(self):
        confirm = input('> 정말 탈퇴하시겠습니까? (y/n) : ')
        if confirm.lower() != 'y':
            print('!!! 탈퇴가 취소되었습니다.')
            return False
        member = self.ms.get_member_info(self.ms.current_user)
        member_no = member.get_member_no()
        if self.ms.remove_member(self.ms.current_user):
            # 라이브러리도 함께 삭제
            self.ps.remove_member_library(member_no)
            self.ms.logout()
            print('!!! 회원 탈퇴가 완료되었습니다.')
            return True
        print('!!! 회원 탈퇴에 실패하였습니다.')
        return False


    def menu_view_all_members(self):
        members = self.ms.get_all_members()
        if not members:
            print('!!! 등록된 회원이 없습니다.')
            return
        print('-' * 50)
        for member in members:
            print(member)
        print('-' * 50)

    def menu_view_member_info(self):
        id = input('> 조회할 회원 아이디 : ')
        member = self.ms.get_member_info(id)
        if member and id != MemberService.ADMIN_ID:
            print(member)
        else:
            print('!!! 해당 회원을 찾을 수 없습니다.')

    def menu_delete_member_admin(self):
        id = input('> 삭제할 회원 아이디 : ')
        if id == MemberService.ADMIN_ID:
            print('!!! 관리자 계정은 삭제할 수 없습니다.')
            return
        member = self.ms.get_member_info(id)
        if not member:
            print('!!! 해당 회원을 찾을 수 없습니다.')
            return
        member_no = member.get_member_no()
        if self.ms.remove_member(id):
            # 라이브러리도 함께 삭제
            self.ps.remove_member_library(member_no)
            print('!!! 회원이 삭제되었습니다.')
        else:
            print('!!! 회원 삭제에 실패하였습니다.')


    def menu_add_game(self):
        title = input('> 게임 이름 : ')
        maker = input('> 제작사 : ')
        try:
            price = int(input('> 가격 : '))
        except ValueError:
            print('!!! 가격은 숫자로 입력해야 합니다.')
            return
        # 게임번호는 자동 부여
        game = Game(None, title, maker, price)
        if self.gs.add_game(game):
            print('!!! 게임이 추가되었습니다.')
        else:
            print('!!! 게임 추가에 실패하였습니다.')

    def menu_update_game(self):
        game_no = input('> 수정할 게임번호 : ')
        game = self.gs.get_game_info(game_no)
        if not game:
            print('!!! 해당 게임을 찾을 수 없습니다.')
            return
        print('!!! 변경할 항목만 입력하세요. (빈 값은 기존 정보 유지)')
        title = input(f'> 게임 이름 [{game.get_title()}] : ') or game.get_title()
        maker = input(f'> 제작사 [{game.get_maker()}] : ') or game.get_maker()
        price_in = input(f'> 가격 [{game.get_price()}] : ')
        try:
            price = int(price_in) if price_in else game.get_price()
        except ValueError:
            print('!!! 가격은 숫자로 입력해야 합니다.')
            return
        new_game = Game(game_no, title, maker, price)
        if self.gs.modify_game_info(game_no, new_game):
            print('!!! 게임 정보가 수정되었습니다.')
        else:
            print('!!! 게임 수정에 실패하였습니다.')

    def menu_delete_game(self):
        game_no = input('> 삭제할 게임번호 : ')
        if not self.gs.get_game_info(game_no):
            print('!!! 해당 게임을 찾을 수 없습니다.')
            return
        if self.gs.remove_game(game_no):
            self.ps.remove_game_from_all(game_no)
            print('!!! 게임이 삭제되었습니다.')
        else:
            print('!!! 게임 삭제에 실패하였습니다.')


    def menu_view_member_library(self):
        id = input('> 조회할 회원 아이디 : ')
        if id == MemberService.ADMIN_ID:
            print('!!! 관리자는 라이브러리가 없습니다.')
            return
        member = self.ms.get_member_info(id)
        if not member:
            print('!!! 해당 회원을 찾을 수 없습니다.')
            return
        member_no = member.get_member_no()
        purchases = self.ps.get_my_library(member_no)
        if not purchases:
            print(f'!!! {member.get_name()}님은 보유 중인 게임이 없습니다.')
            return
        print('-' * 50)
        print(f'[{member.get_name()}님의 라이브러리]')
        print('-' * 50)
        for purchase in purchases:
            game = self.gs.get_game_info(purchase.get_game_no())
            if game:
                print(game)
        print('-' * 50)


    def show_welcome(self):
        title = 'YJ Game Store'
        print(self.print_title(title))

    def say_goodbye(self):
        print('이용해주셔서 감사합니다. 안녕히 가세요.')

    def print_title(self, title):
        return f"{'=' * 50}\n{title:^50}\n{'=' * 50}"

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
    app = GameStore()
    app.main()
