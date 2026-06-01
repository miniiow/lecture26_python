from Member.member_dao import MemberDAO
from Member.member import Member
# ==========================
# 회원관리 서비스로직(Controller) : MemberService
class MemberService:
    ADMIN_ID = 'admin'
    ADMIN_PASSWORD = '1234'

    def __init__(self, memberDao):
        self.__dao = memberDao
        self.current_user = None
        self.join(Member(MemberService.ADMIN_ID,MemberService.ADMIN_PASSWORD,'관리자'))

    # 회원가입
    def join(self, member):
        # 대소문자 구별하지 않음
        # 어떻게 id가 입력되었는지 모르니까 일단 다 소문자로 변셩
        # member.set_id(member.get_id().lower())
        # if not self.is_valid_id(member.get_id()):
        #     return False

        # 이미 있는 아이디 있는지 확인하기 > 있으면 Error / 없으면 추가
        if self.__dao.is_exist(member.get_id()):
            return False

        self.__dao.insert_member(member)
        return True
    
    # def is_valid_id(id):
    #     # 입력한 아이디가 유효한지 확인
    #     if id.isalpha(): return True


    # 로그인
    def login(self, id, password):
        member = self.__dao.get_member_info(id)
        if member:
            if password == member.get_password():
                self.current_user = id
                return True
        return False
    
    # 로그아웃
    def logout(self):
        self.current_user = None
    
    # 전체회원목록
    def list_members(self):
        member_list = self.__dao.get_all_members()
        if member_list:
            return member_list
        return False
    
    # 회원상세
    def view_member_info(self, id):
        if self.__dao.is_exist(id):
            return self.__dao.get_member_info(id)
        return None
    
    # 회원수정
    def update_member_info(self, id, member):
        if self.current_user != id: return False
        return self.__dao.update_member_info(id, member)
            
    def update_member_password(self, id, org_password, new_password):
        if self.current_user != id: return False
        member = self.__dao.get_member_info(id)
        if not member: return False

        # DB에 저장된 pw와 사용자가 입력한 기존pw랑 같는지 비교
        # 동일하면 비밀번호 수정.
        if member.get_password() == org_password:
            member.set_password(new_password)
            return True
        return False

    # 회원탈퇴
    def remove_member(self, id):
        print('remove_member: ', self.current_user)
        if self.current_user == id or self.current_user == MemberService.ADMIN_ID:
            return self.__dao.remove_member(id)
        return False

    
if __name__ == '__main__':
    ms = MemberService(MemberDAO())
    ms.join(Member('dbwls', '1234', '유징'))
    members = ms.list_members()
    for member in members:
        print(member)
    ms.login('dbwls', '1234')
    print(ms.current_user)
    ms.logout()
    print(ms.current_user)
    print(ms.view_member_info('dbwls'))
    ms.login('dbwls', '1234')
    ms.login(MemberService.ADMIN_ID, MemberService.ADMIN_PASSWORD)
    print(ms.update_member_password('dbwls', '1234', '1111'))
    print(ms.view_member_info('dbwls'))
    print(ms.remove_member('dbwls'))
    print(ms.view_member_info('dbwls'))