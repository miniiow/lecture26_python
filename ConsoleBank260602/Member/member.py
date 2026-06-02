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
    def set_id(self, id):
        self.__id = id

    def __str__(self):
        return f'{self.__id}\t{self.__name}\t{self.__password}'