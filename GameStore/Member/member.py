class Member:
    def __init__(self, member_no, id, password, name):
        self.__member_no = member_no    # 회원번호 (자동 1씩 증가)
        self.__id = id                  # 아이디
        self.__password = password      # 비밀번호
        self.__name = name              # 회원명


    def get_member_no(self):
        return self.__member_no
    def get_id(self):
        return self.__id
    def get_password(self):
        return self.__password
    def get_name(self):
        return self.__name

    def set_member_no(self, member_no):
        self.__member_no = member_no
    def set_id(self, id):
        self.__id = id
    def set_password(self, password):
        self.__password = password
    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return f'회원번호: {self.__member_no} 아이디: {self.__id} 이름: {self.__name}'