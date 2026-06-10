from Member.member import Member
import joblib
# ==========================
# 회원 데이터 접근(CRUD): MemberDAO
class MemberDAO:
    MEMBER_DB_FILE = 'C:/lecture/python26/OnlineBookStore/DB/memberDB.pkl'
    def __init__(self):
        self.__load_memberDB()

    def __load_memberDB(self):
        try:
            self.__memberDB = joblib.load(MemberDAO.MEMBER_DB_FILE)
        except (FileNotFoundError, EOFError):
            self.__memberDB = {}
            self.save_memberDB()
        
    # 저장
    def save_memberDB(self):
        joblib.dump(self.__memberDB, MemberDAO.MEMBER_DB_FILE)

    # 회원가입
    def insert_member(self, member):
        if self.is_member_exist(member.get_id()):
            return False
        self.__memberDB[member.get_id()] = member
        self.save_memberDB()
        return True

    # 회원목록
    def select_all_members(self):
        return list(self.__memberDB.values())
        
    # 회원정보상세
    def select_member_info(self, id):
        if self.is_member_exist(id):
            return self.__memberDB[id]
        else:
            return None
    
    # 회원탈퇴
    def delete_member(self, id):
        if self.is_member_exist(id):
            self.__memberDB.pop(id)
            self.save_memberDB()
            return True
        return False
        
    # 회원수정
    def update_member_info(self, id, member):
        if self.is_member_exist(id):
            self.__memberDB[id] = member
            self.save_memberDB()
            return True
        return False
    
    # 가입한 회원 여부 확인
    def is_member_exist(self, id):
        if id in self.__memberDB.keys():
            return True
        return False