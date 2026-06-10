from datetime import datetime

from Member.member import Member
from Member.member_dao import MemberDAO
from Member.member_service import MemberService
from Book.book import Book
from Book.book_dao import BookDAO
from Book.book_service import BookService
from Cart.cart import Cart
from Cart.cart_dao import CartDAO
from Cart.cart_item import CartItem
from Cart.cart_item_dao import CartItemDAO
from Cart.cart_service import CartService
from Delivery.delivery import Delivery
from Delivery.delivery_dao import DeliveryDAO
from Delivery.delivery_service import DeliveryService
from Order.order import Order
from Order.order_dao import OrderDAO
from Order.order_item import OrderItem
from Order.order_item_dao import OrderItemDAO
from Order.order_service import OrderService


class OnlineBookStore:
    START_MENU = ['종료', '회원가입', '로그인']
    MEMBER_MENU = ['로그아웃', '내정보', '배송조회', '주문조회', '장바구니']
    ADMIN_MENU = ['로그아웃', '회원관리', '책관리', '주문관리', '배송관리']
    MEMBER_CART_MENU = ['돌아가기', '장바구니목록조회', '장바구니삭제', '주문']
    MEMBER_MYINFO_MENU = ['돌아가기', '회원정보조회', '회원수정', '회원탈퇴']
    ADMIN_MEMBER_MENU = ['돌아가기', '회원목록조회', '회원상세조회', '회원삭제']
    ADMIN_BOOK_MENU = ['돌아가기', '책추가', '책수정', '책삭제']
    ADMIN_ORDER_MENU = ['돌아가기', '회원별주문조회', '주문취소']
    ADMIN_DELIVERY_MENU = ['돌아가기', '배송목록조회', '회원별배송조회', '배송상태수정']

    def __init__(self):
        self.ms = MemberService(MemberDAO(), CartDAO())
        self.bs = BookService(BookDAO())
        self.cs = CartService(CartDAO(), CartItemDAO())
        self.os = OrderService(OrderDAO(), OrderItemDAO())
        self.ds = DeliveryService(DeliveryDAO())

    def main(self):
        self.show_welcome()
        self.run_start_menu()
        self.say_goodbye()


    # 시작메뉴
    def run_start_menu(self):
        self.view_all_book_info()
        while True:
            menu = self.select_menu(OnlineBookStore.START_MENU)
            if menu == 0:
                return
            elif menu == 1:  # 회원가입
                self.menu_join()
            elif menu == 2:  # 로그인
                self.menu_login()
            else:
                print('없는 메뉴입니다.')

    # 회원메뉴
    def run_member_menu(self):
        while True:
            menu = self.select_menu(OnlineBookStore.MEMBER_MENU)
            if menu == 0:  # 로그아웃
                self.menu_logout()
                return
            elif menu == 1:  # 장바구니
                self.run_cart_menu()
            elif menu == 2:  # 주문조회
                self.menu_list_my_order()
            elif menu == 3:  # 배송조회
                self.menu_list_my_delivery()
            elif menu == 4:  # 내정보
                self.run_my_info_menu()
            else:
                print('없는 메뉴입니다.')

    # 회원-내 주문 조회
    def menu_list_my_order(self):
        member_id = self.ms.current_user
        orders = self.os.get_order_info(member_id)
        if not orders:
            print('!!! 주문 내역이 없습니다.')
            return
        for order in orders:
            print(order)
        print('-' * 50)
        items = self.os.get_order_item(member_id)
        if items:
            print('[주문 상세]')
            for item in items:
                print(item)
    
    # 회원-내 배송 조회
    def menu_list_my_delivery(self):
        member_id = self.ms.current_user
        deliveries = self.ds.get_member_delivery(member_id)
        if not deliveries:
            print('!!! 배송 내역이 없습니다.')
            return
        for delivery in deliveries:
            print(delivery)

    # 회원-장바구니 메뉴
    def run_cart_menu(self):
        while True:
            menu = self.select_menu(OnlineBookStore.MEMBER_CART_MENU)
            if menu == 0:  # 돌아가기
                return
            elif menu == 1:  # 장바구니목록조회
                self.menu_view_all_cart()
            elif menu == 2:  # 장바구니삭제
                self.menu_delete_cart()
            elif menu == 3:  # 주문
                self.menu_add_order()
            else:
                print('없는 메뉴입니다.')

    # 장바구니 목록 조회
    def menu_view_all_cart(self):
        member_id = self.ms.current_user
        items = self.cs.get_all_cart_items(member_id)
        if not items:
            print('!!! 장바구니가 비어있습니다.')
            return
        total = 0
        for item in items:
            book = self.bs.get_book_info(item.get_book_no())
            if book:
                subtotal = book.get_price() * item.get_count()
                total += subtotal
                print(f'{book.get_title()} | 가격: {book.get_price():,}원 | '
                      f'수량: {item.get_count()} | 소계: {subtotal:,}원')
            else:
                print(item)
        print('-' * 50)
        print(f'총 금액: {total:,}원')

    # 장바구니 삭제
    def menu_delete_cart(self):
        member_id = self.ms.current_user
        items = self.cs.get_all_cart_items(member_id)
        if not items:
            print('!!! 장바구니가 비어있습니다.')
            return
        self.menu_view_all_cart()
        book_no = input('> 삭제할 책번호 입력 : ')
        if self.cs.remove_cart_item(member_id, book_no):
            print('!!! 장바구니에서 삭제되었습니다.')
        else:
            print('!!! 삭제에 실패하였습니다.')

    # 장바구니 주문
    def menu_add_order(self):
        member_id = self.ms.current_user
 
        # 연락처/주소 정보 확인 (주문 가능 여부)
        if not self.ms.is_contact_complete(member_id):
            print('!!! 주문을 위해 연락처/이메일/주소 정보가 필요합니다.')
            phone = input('> 휴대폰 입력 : ')
            email = input('> 이메일 입력 : ')
            address = input('> 주소 입력 : ')
            if not self.ms.update_contact_info(member_id, phone, email, address):
                print('!!! 회원정보 업데이트에 실패하였습니다.')
                return
 
        items = self.cs.get_all_cart_items(member_id)
        if not items:
            print('!!! 장바구니가 비어있습니다.')
            return
        
        total_price = 0
        order_lines = []
        for item in items:
            book = self.bs.get_book_info(item.get_book_no())
            if book is None:
                print(f'!!! 책번호 {item.get_book_no()} 정보를 찾을 수 없습니다.')
                return
            if book.get_stock() < item.get_count():
                print(f'!!! [{book.get_title()}] 재고가 부족합니다. '
                      f'(재고: {book.get_stock()}, 요청: {item.get_count()})')
                return
            subtotal = book.get_price() * item.get_count()
            total_price += subtotal
            order_lines.append((book, item.get_count(), subtotal))

        # 주문 생성
        order = Order(None, member_id, total_price)
        if not self.os.add_order(order):
            print('!!! 주문 생성에 실패하였습니다.')
            return
        order_no = order.get_order_no()

        # 주문 아이템 생성 + 재고 차감
        for book, count, subtotal in order_lines:
            self.os.add_order_item(
                OrderItem(member_id, order_no, book.get_book_no(), count, subtotal))
            book.set_book_stock(book.get_stock() - count)
            self.bs.modify_book_info(book.get_book_no(), book)

        # 배송 생성
        member = self.ms.get_member_info(member_id)
        delivery = Delivery(member_id, None, order_no,
                            delivery_address=member.get_address())
        self.ds.add_delivery(delivery)

        # 장바구니 비우기
        self.cs.clear_cart(member_id)
        # 장바구니 다시 생성 (회원은 항상 장바구니 1개 가지고 있어야 함)
        self.ms.add_cart(Cart(member_id))
        print(f'!!! 주문이 완료되었습니다. (주문번호: {order_no}, '
              f'총 금액: {total_price:,}원)')
        
    # 회원-내정보 메뉴
    def run_my_info_menu(self):
        while True:
            menu = self.select_menu(OnlineBookStore.MEMBER_MYINFO_MENU)
            if menu == 0:  # 돌아가기
                return
            elif menu == 1:  # 회원정보조회
                self.menu_view_my_info()
            elif menu == 2:  # 회원수정
                self.menu_update_my_info()
            elif menu == 3:  # 회원탈퇴
                if self.menu_delete_member():
                    return
            else:
                print('없는 메뉴입니다.')

    # 회원정보 조회
    def menu_view_my_info(self):
        member = self.ms.get_member_info(self.ms.current_user)
        if member:
            print(member)
        else:
            print('!!! 회원정보를 찾을 수 없습니다.')

    # 회원수정
    def menu_update_my_info(self):
        member_id = self.ms.current_user
        member = self.ms.get_member_info(member_id)
        if not member:
            print('!!! 회원정보를 찾을 수 없습니다.')
            return
        print('!!! 변경할 항목만 입력하세요. (빈 값은 기존 정보 유지)')
        name = input(f'> 이름 [{member.get_name()}] : ')
        phone = input(f'> 휴대폰 [{member.get_phone()}] : ')
        email = input(f'> 이메일 [{member.get_email()}] : ')
        address = input(f'> 주소 [{member.get_address()}] : ')
 
        if name:
            member.set_name(name)
        if phone:
            member.set_phone(phone)
        if email:
            member.set_email(email)
        if address:
            member.set_address(address)
 
        if self.ms.modify_member_info(member_id, member):
            print('!!! 회원정보가 수정되었습니다.')
        else:
            print('!!! 회원정보 수정에 실패하였습니다.')

    # 회원탈퇴
    def menu_delete_member(self):
        member_id = self.ms.current_user
        confirm = input('> 정말 탈퇴하시겠습니까? (y/n) : ')
        if confirm.lower() != 'y':
            print('!!! 탈퇴가 취소되었습니다.')
            return False
        if self.ms.remove_member(member_id):
            print('!!! 회원탈퇴가 완료되었습니다.')
            self.ms.logout()
            return True
        else:
            print('!!! 회원탈퇴에 실패하였습니다.')
            return False

    # 관리자 메뉴
    def run_admin_menu(self):
        while True:
            menu = self.select_menu(OnlineBookStore.ADMIN_MENU)
            if menu == 0:  # 로그아웃
                self.menu_logout()
                return
            elif menu == 1:  # 회원관리
                self.run_admin_member_menu()
            elif menu == 2:  # 책관리
                self.run_admin_book_menu()
            elif menu == 3:  # 주문관리
                self.run_admin_order_menu()
            elif menu == 4:  # 배송관리
                self.run_admin_delivery_menu()
            else:
                print('없는 메뉴입니다.')

    # 관리자-회원관리 메뉴
    def run_admin_member_menu(self):
        while True:
            menu = self.select_menu(OnlineBookStore.ADMIN_MEMBER_MENU)
            if menu == 0:  # 돌아가기
                return
            elif menu == 1:  # 회원목록조회
                self.menu_view_all_members()
            elif menu == 2:  # 회원상세조회
                self.menu_view_member_info()
            elif menu == 3:  # 회원삭제
                self.menu_delete_member_admin()
            else:
                print('없는 메뉴입니다.')

    # 회원목록조회
    def menu_view_all_members(self):
        members = self.ms.get_all_members()
        if not members:
            print('!!! 등록된 회원이 없습니다.')
            return
        for member in members:
            print(member)
            print('-' * 50)

    # 회원상세조회
    def menu_view_member_info(self):
        member_id = input('> 조회할 회원 아이디 입력 : ')
        member = self.ms.get_member_info(member_id)
        if member:
            print(member)
        else:
            print('!!! 해당 회원을 찾을 수 없습니다.')
        
    # 회원삭제 (관리자)
    def menu_delete_member_admin(self):
        member_id = input('> 삭제할 회원 아이디 입력 : ')
        if member_id == MemberService.ADMIN_ID:
            print('!!! 관리자 계정은 삭제할 수 없습니다.')
            return
        if self.ms.remove_member(member_id):
            print('!!! 회원이 삭제되었습니다.')
        else:
            print('!!! 회원 삭제에 실패하였습니다.')


    # 관리자-책관리 메뉴
    def run_admin_book_menu(self):
        while True:
            menu = self.select_menu(OnlineBookStore.ADMIN_BOOK_MENU)
            if menu == 0:  # 돌아가기
                return
            elif menu == 1:  # 책추가
                self.menu_add_book()
            elif menu == 2:  # 책수정
                self.menu_update_book()
            elif menu == 3:  # 책삭제
                self.menu_delete_book()
            else:
                print('없는 메뉴입니다.')

    # 책추가
    def menu_add_book(self):
        title = input('> 책 제목 : ')
        author = input('> 저자 : ')
        publisher = input('> 출판사 : ')
        try:
            price = int(input('> 가격 : '))
            stock = int(input('> 재고 : '))
        except ValueError:
            print('!!! 가격/재고는 숫자로 입력해야 합니다.')
            return
        # 책번호는 BookService.add_book 에서 자동 부여
        book = Book(None, title, author, publisher, price, stock)
        if self.bs.add_book(book):
            print('!!! 책이 추가되었습니다.')
        else:
            print('!!! 책 추가에 실패하였습니다.')

    # 책수정
    def menu_update_book(self):
        book_no = input('> 수정할 책번호 : ')
        book = self.bs.get_book_info(book_no)
        if not book:
            print('!!! 해당 책을 찾을 수 없습니다.')
            return
        print('!!! 변경할 항목만 입력하세요. (빈 값은 기존 정보 유지)')
        title = input(f'> 제목 [{book.get_title()}] : ') or book.get_title()
        author = input(f'> 저자 [{book.get_author()}] : ') or book.get_author()
        publisher = input(f'> 출판사 [{book.get_publisher()}] : ') or book.get_publisher()
        price_in = input(f'> 가격 [{book.get_price()}] : ')
        stock_in = input(f'> 재고 [{book.get_stock()}] : ')
        try:
            price = int(price_in) if price_in else book.get_price()
            stock = int(stock_in) if stock_in else book.get_stock()
        except ValueError:
            print('!!! 가격/재고는 숫자로 입력해야 합니다.')
            return
        new_book = Book(book_no, title, author, publisher, price, stock)
        if self.bs.modify_book_info(book_no, new_book):
            print('!!! 책 정보가 수정되었습니다.')
        else:
            print('!!! 책 수정에 실패하였습니다.')

    # 책삭제
    def menu_delete_book(self):
        book_no = input('> 삭제할 책번호 : ')
        book = self.bs.get_book_info(book_no)
        if self.bs.remove_book(book_no, book):
            print('!!! 책이 삭제되었습니다.')
        else:
            print('!!! 책 삭제에 실패하였습니다.')

    # 관리자-주문관리 메뉴
    def run_admin_order_menu(self):
        while True:
            menu = self.select_menu(OnlineBookStore.ADMIN_ORDER_MENU)
            if menu == 0:  # 돌아가기
                return
            elif menu == 1:  # 회원별주문조회
                self.menu_list_member_order()
            elif menu == 2:  # 주문취소
                self.menu_delete_member_order()
            else:
                print('없는 메뉴입니다.')

    # 회원별 주문조회
    def menu_list_member_order(self):
        member_id = input('> 조회할 회원 아이디 입력 : ')
        orders = self.os.get_order_info(member_id)
        if not orders:
            print('!!! 주문 내역이 없습니다.')
            return
        for order in orders:
            print(order)
        print('-' * 50)
        items = self.os.get_order_item(member_id)
        if items:
            print('[주문 상세]')
            for item in items:
                print(item)

    # 주문취소 (회원의 전체 주문 삭제)
    def menu_delete_member_order(self):
        member_id = input('> 주문취소할 회원 아이디 입력 : ')
        order_no = input('> 취소할 주문번호 (전체취소는 빈 값) : ')
        if order_no:
            if self.os.remove_order(member_id, order_no):
                print('!!! 주문이 취소되었습니다.')
            else:
                print('!!! 주문 취소에 실패하였습니다.')
        else:
            if self.os.remove_all_orders(member_id):
                self.os.remove_order_item(member_id)
                print('!!! 회원의 전체 주문이 취소되었습니다.')
            else:
                print('!!! 취소할 주문이 없습니다.')

    # 관리자-배송관리 메뉴
    def run_admin_delivery_menu(self):
        while True:
            menu = self.select_menu(OnlineBookStore.ADMIN_DELIVERY_MENU)
            if menu == 0:  # 돌아가기
                return
            elif menu == 1:  # 배송목록조회
                self.menu_view_all_delivery()
            elif menu == 2:  # 회원별배송조회
                self.menu_view_member_delivery()
            elif menu == 3:  # 배송상태수정
                self.menu_update_delivery_status()
            else:
                print('없는 메뉴입니다.')

    # 배송 목록 전체 조회
    def menu_view_all_delivery(self):
        deliveries = self.ds.get_all_deliveries()
        if not deliveries:
            print('!!! 배송 내역이 없습니다.')
            return
        for delivery in deliveries:
            print(delivery)
            print('-' * 50)

    # 회원별 배송 조회
    def menu_view_member_delivery(self):
        member_id = input('> 조회할 회원 아이디 입력 : ')
        deliveries = self.ds.get_member_delivery(member_id)
        if not deliveries:
            print('!!! 배송 내역이 없습니다.')
            return
        for delivery in deliveries:
            print(delivery)

    # 배송 상태 수정
    def menu_update_delivery_status(self):
        member_id = input('> 회원 아이디 입력 : ')
        delivery_no = input('> 배송번호 입력 : ')
        print('배송상태:', Delivery.STATUS)
        try:
            status = int(input('> 변경할 상태 번호 입력 : '))
        except ValueError:
            print('!!! 상태 번호는 숫자로 입력해야 합니다.')
            return
        if self.ds.modify_delivery_status(member_id, delivery_no, status):
            # 배송완료(4)로 변경 시 배송일자 기록
            if status == 4:
                self.ds.modify_delivery_date(
                    member_id, delivery_no, datetime.now().strftime('%Y-%m-%d'))
            print('!!! 배송 상태가 수정되었습니다.')
        else:
            print('!!! 배송 상태 수정에 실패하였습니다.')


    def menu_join(self):  # 회원가입
        id = input('> 아이디 입력 : ')
        password = input('> 비밀번호 입력 : ')
        name = input('> 회원명 입력 : ')
        member = Member(id, password, name)
        if self.ms.join_member(member):
            print('회원가입이 완료되었습니다.')
        else:
            print('회원가입에 실패하였습니다.')
 
    def menu_login(self):  # 로그인
        id = input('> 아이디 입력 : ')
        password = input('> 비밀번호 입력 : ')
        if self.ms.login(id, password):
            print(f'{self.ms.get_member_info(id).get_name()}님 환영합니다 !')
            if self.ms.current_user == MemberService.ADMIN_ID:
                self.run_admin_menu()   # 관리자메뉴 이동
            else:
                self.run_member_menu()  # 일반회원메뉴 이동
        else:
            print('로그인에 실패하였습니다.')
 
    def menu_logout(self):  # 로그아웃
        self.ms.logout()
        print('!!! 로그아웃 되었습니다.')
        
    def show_welcome(self):
        title = 'Welcome OnlineBookStore'
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
        try:
            menu = int(input('> 메뉴입력 : '))
        except ValueError:
            return -1
        else:
            return menu

    def view_all_book_info(self):
        books = self.bs.get_all_books()
        if not books:
            print('!!! 등록된 책이 없습니다.')
            return
        for book in books:
            print(book)

if __name__ == '__main__':
    app = OnlineBookStore()
    app.main()