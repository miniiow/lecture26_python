from Member.member import Member
# ==========================
# 회원 데이터 접근(CRUD): MemberDAO
class MemberDAO:
    def __init__(self):
        self.__memberDB = {}

    # 회원가입
    def insert_member(self, member):
        if self.is_exist(member.get_id()):
            return False
        self.__memberDB[member.get_id()] = member
        return True

    # 가입한 회원 있는지 확인
    # 반환받은 id가 있으면 True반환 / 없으면 False반환
    def is_exist(self, id):
        if id in self.__memberDB.keys():
            return True
        return False

    # 회원목록
    def get_all_members(self):
        if self.__memberDB:
            return list(self.__memberDB.values())
        
    # 회원정보상세
    def get_member_info(self, id):
        if self.is_exist(id):
            return self.__memberDB[id]
        else:
            return None
    
    # 회원탈퇴
    def remove_member(self, id):
        if self.is_exist(id):
            self.__memberDB.pop(id)
            # del self.__memberDB[id]
            return True
        else:
            return False
        
    # 회원수정
    def update_member_info(self, id, member):
        if self.is_exist(id):
            self.__memberDB[id] = member
            return True
        return False
    
# 클래스 동작 테스트 (단위테스트, unit test)
# 모듈 테스트 할때 if __name__ 문 안에 넣어서 진행
if __name__ == '__main__':
    dao = MemberDAO()

    member = Member('dbwls', '1234', '유진')
    dao.insert_member(member)
    print(dao.is_exist('dbwls'))
    member = Member('a123', '1234','AAA')
    dao.insert_member(member)
    print(dao.get_member_info('dbwls'))
    print(dao.get_member_info('a123'))

    members = dao.get_all_members()
    print('[get_all_members] =======')
    for member in members:
        print(member)

    member = dao.get_member_info('dbwls')
    if member:
        member.set_password('1111')
        dao.update_member_info('dbwls', member)
    
    members = dao.get_all_members()
    print('[get_all_members] =======')
    for member in members:
        print(member)

    dao.remove_member('dbwls')
    members = dao.get_all_members()
    print('[get_all_members] =======')
    for member in members:
        print(member)