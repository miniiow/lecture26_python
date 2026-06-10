class CartItem:
    def __init__(self, member_id, book_no, count):
        self.__member_id = member_id
        self.__book_no = book_no
        self.__count = count

    def get_member_id(self):
        return self.__member_id
    def get_book_no(self):
        return self.__book_no
    def get_count(self):
        return self.__count
    
    def set_member_id(self, member_id):
        self.__member_id = member_id
    def set_book_no(self, book_no):
        self.__book_no = book_no
    def set_count(self, count):
        self.__count = count

    def __str__(self):
        return f'회원아이디: {self.__member_id} 책번호: {self.__book_no} 개수: {self.__count}'