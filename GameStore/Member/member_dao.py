from Member.member import Member
import joblib

# ==========================
# 회원 데이터 접근(CRUD): MemberDAO
class MemberDAO:
    MEMBER_DB_FILE = 'C:/lecture/python26/GameStore/DB/memberDB.pkl'

    def __init__(self):
        self.__load_memberDB()

    def __load_memberDB(self):
        try:
            # self.__memberDB: id를 key로 하는 딕셔너리
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

    # memberDB.pkl 파일 초기화
    def clear_memberDB(self):
        self.__memberDB = {}
        self.save_memberDB()
    
    # 회원번호 최대값 조회 (없으면 0 -> 회원번호는 1부터 1씩 증가)
    def get_max_no(self):
        if not self.__memberDB:
            return 0
        max_no = 0
        for member in self.__memberDB.values():
            member_no = int(member.get_member_no())
            if member_no > max_no:
                max_no = member_no
        return max_no