class OrderItem:
    def __init__(self, member_id, order_no, book_no, count, price):
        self.__member_id = member_id
        self.__order_no = order_no
        self.__book_no = book_no
        self.__count = count
        self.__price = price

    def get_member_id(self):
        return self.__member_id
    def get_order_no(self):
        return self.__order_no
    def get_book_no(self):
        return self.__book_no
    def get_count(self):
        return self.__count
    def get_price(self):
        return self.__price

    def set_member_id(self, member_id):
        self.__member_id = member_id
    def set_order_no(self, order_no):
        self.__order_no = order_no
    def set_book_no(self, book_no):
        self.__book_no = book_no
    def set_count(self, count):
        self.__count = count
    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return f'회원번호: {self.__member_id} 주문번호: {self.__order_no} 책번호: {self.__book_no} 개수: {self.__count} 금액: {self.__price:,}원'