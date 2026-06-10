# id, password, name은 회원가입 시 필수입력사항 / phone, email, address는 선택사항 > 기본값 None
class Member:
    def __init__(self, id, password, name, phone=None, email=None, address=None):
        self.__id = id
        self.__password = password
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__address = address

    def get_id(self):
        return self.__id
    def get_password(self):
        return self.__password
    def get_name(self):
        return self.__name
    def get_phone(self):
        return self.__phone
    def get_email(self):
        return self.__email
    def get_address(self):
        return self.__address
    
    def set_name(self, name):
        self.__name = name
    def set_password(self, password):
        self.__password = password
    def set_id(self, id):
        self.__id = id
    def set_phone(self, phone):
        self.__phone = phone
    def set_email(self, email):
        self.__email = email
    def set_address(self, address):
        self.__address = address

    def __str__(self):
        return f'아이디: {self.__id} 이름: {self.__name} 비밀번호: {self.__password}\n휴대폰: {self.__phone} 이메일: {self.__email} 주소: {self.__address}'