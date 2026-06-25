from Member.member import Member
from Member.member_dao import MemberDAO


class MemberService:
    ADMIN_ID = 'admin'
    ADMIN_PASSWORD = '1234'
    ADMIN_NAME = '관리자'
    ADMIN_NO = 0  # 관리자는 회원번호 0번

    def __init__(self, member_dao):
        self.__dao = member_dao
        self.current_user = None    # 현재 로그인한 회원의 id
        # 관리자 계정 초기화
        if not self.__dao.is_member_exist(MemberService.ADMIN_ID):
            self.__dao.insert_member(Member(
                MemberService.ADMIN_NO,
                MemberService.ADMIN_ID,
                MemberService.ADMIN_PASSWORD,
                MemberService.ADMIN_NAME
            ))

    # 회원가입
    def join_member(self, member):
        if self.__dao.is_member_exist(member.get_id()):
            return False
        # 회원번호 자동 부여 (1부터 1씩 증가)
        next_no = self.__dao.get_max_no() + 1
        member.set_member_no(next_no)
        return self.__dao.insert_member(member)

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

    # 관리자 여부 확인
    def is_admin(self):
        return self.current_user == MemberService.ADMIN_ID

    # 전체회원목록 (관리자 제외)
    def get_all_members(self):
        member_list = self.__dao.select_all_members()
        if not member_list:
            return None
        # 관리자 계정은 제외하고 반환
        result = [m for m in member_list if m.get_id() != MemberService.ADMIN_ID]
        return result if result else None

    # 회원상세
    def get_member_info(self, id):
        if self.__dao.is_member_exist(id):
            return self.__dao.select_member_info(id)
        return None

    # 비밀번호 수정
    def modify_member_password(self, id, org_password, new_password):
        if self.current_user != id:
            return False
        member = self.__dao.select_member_info(id)
        if not member:
            return False
        if member.get_password() == org_password:
            member.set_password(new_password)
            return self.__dao.update_member_info(id, member)
        return False

    # 회원탈퇴
    def remove_member(self, id):
        # 관리자는 삭제 불가
        if id == MemberService.ADMIN_ID:
            return False
        # 본인이거나 관리자만 삭제 가능
        if self.current_user == id or self.current_user == MemberService.ADMIN_ID:
            return self.__dao.delete_member(id)
        return False