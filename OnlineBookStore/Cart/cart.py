class Cart:
    def __init__(self, member_id):
        self.__member_id = member_id

    def get_member_id(self):
        return self.__member_id
    
    def __str__(self):
        return f'회원아이디: {self.__member_id}'