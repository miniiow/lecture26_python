from Member.member import Member
from Member.member_dao import MemberDAO
from Cart.cart import Cart
from Cart.cart_dao import CartDAO

class MemberService:
    ADMIN_ID = 'admin'
    ADMIN_PASSWORD = '1234'

    def __init__(self, memberDao, cart_dao):
        self.__dao = memberDao
        self.__cart_dao = cart_dao
        self.current_user = None
        self.join_member(Member(MemberService.ADMIN_ID, MemberService.ADMIN_PASSWORD,'관리자','010-1234-1234','admin@abc.com','관리자 주소'))
                

    # 회원가입
    def join_member(self, member):
        if self.__dao.is_member_exist(member.get_id()):
            return False
        self.__dao.insert_member(member)
        self.add_cart(Cart(member.get_id()))
        return True

    # 로그인
    def login(self, id, password):
        member = self.__dao.select_member_info(id)
        if member:
            if password == member.get_password():
                self.current_user = id
                return True
        return False
    
    # 로그아웃
    def logout(self):
        self.current_user = None
        self.__dao.save_memberDB()
    
    # 전체회원목록
    def get_all_members(self):
        member_list = self.__dao.select_all_members()
        if member_list:
            return member_list
        return False
    
    # 회원상세
    def get_member_info(self, id):
        if self.__dao.is_member_exist(id):
            return self.__dao.select_member_info(id)
        return None
    
    # 회원수정
    def modify_member_info(self, id, member):
        if self.current_user != id: return False
        return self.__dao.update_member_info(id, member)
            
    def modify_member_password(self, id, org_password, new_password):
        if self.current_user != id: return False
        member = self.__dao.select_member_info(id)
        if not member: return False
        if member.get_password() == org_password:
            member.set_password(new_password)
            return True
        return False

    # 회원탈퇴
    def remove_member(self, id):
        # 자신의 계정이나 관리자계정만 회원탈퇴를 진행할 수 있다
        if self.current_user == id or self.current_user == MemberService.ADMIN_ID:
            return self.__dao.delete_member(id)
        return False
    
    # 장바구니 추가
    def add_cart(self, cart):
        return self.__cart_dao.insert_cart(cart)
    
    # 회원정보에 phone, email, address모두 입력되어있는지 확인 > 주문 가능 여부 확인
    def is_contact_complete(self, id):
        member = self.__dao.select_member_info(id)
        if not member:
            return False
        if member.get_phone() is None:
            return False
        if member.get_email() is None:
            return False
        if member.get_address() is None:
            return False
        return True
    
    # 비어있던 회원정보 채우고 DB에 반영
    def update_contact_info(self, id, phone=None, email=None, address=None):
        member = self.__dao.select_member_info(id)
        if not member:
            return False
        if phone is not None:
            member.set_phone(phone)
        if email is not None:
            member.set_email(email)
        if address is not None:
            member.set_address(address)
        return self.__dao.update_member_info(id, member)
            