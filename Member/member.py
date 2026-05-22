# 데이터 모델 정의 : Member
class Member:
    def __init__(self, id, password, name):
        self.__id = id
        self.__password = password
        self.__name = name

    def get_id(self):
        return self.__id
    def get_password(self):
        return self.__password
    def get_name(self):
        return self.__name
    def set_password(self, password):
        self.__password = password

    def __str__(self):
        return f'{self.__id}\t{self.__name}\t{self.__password}'


# ==========================
# 회원관리 서비스로직(Controller) : MemberService
class MemberService:
    def __init__(self, memberDao):
        self.__dao = memberDao

    # 회원가입
    def join(self, member):
        # 이미 있는 아이디 있는지 확인하기 > 있으면 Error / 없으면 추가
        if self.__dao.is_exist(member.get_id()):
            return False
        self.__dao.insert_member(member)
        return True
    
    # 로그인
    def login(self, id, password):
        member = self.__dao.get_member_info(id)
        if member:
            if password == member.get_password():
                return id
        return None
    
    # 로그아웃
    def logout(self):
        return '로그아웃 성공'
    
    # 전체회원목록
    def list_members(self):
        member_list = self.__dao.get_all_members()
        if member_list:
            return member_list
        return False
    
    # 회원상세
    def list_member_info(self, id):
        member_info = self.__dao.get_member_info(id)
        return member_info
    
    # 회원탈퇴
    def remove_member(self, id):
        return self.__dao.remove_member(id)
    
    # 회원수정
    def update_member_info(self, id, member):
        member_info = self.__dao.update_member_info(id, member)
        return member_info


# ==========================
# 회원 데이터 접근(CRUD): MemberDAO
class MemberDAO:
    def __init__(self):
        self.__memberDB = {}

    # 회원가입
    def insert_member(self, member):
        self.__memberDB[member.get_id()] = member

    # 가입한 회원 있는지 확인
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
            del self.__memberDB[id]
            return True
        else:
            return False
        
    # 회원수정
    def update_member_info(self, id, member):
        if self.is_exist(id):
            self.__memberDB[id] = member
            return True
        return False