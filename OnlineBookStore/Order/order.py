from datetime import datetime
# 배송 테이블 없이 order에서 사용
class Order:
    def __init__(self, order_no, member_id, total_price):
        self.__order_no = order_no
        self.__member_id = member_id
        self.__total_price = total_price
        self.__order_date = datetime.now().strftime('%Y-%m-%d')

    def get_order_no(self):
        return self.__order_no
    def get_member_id(self):
        return self.__member_id
    def get_total_price(self):
        return self.__total_price
    def get_order_date(self):
        return self.__order_date
    
    def set_order_no(self, order_no):
        self.__order_no = order_no
    def set_total_price(self, total_price):
        self.__total_price = total_price
    
    def __str__(self):
        return f'주문번호: {self.__order_no} 회원번호: {self.__member_id} 총금액: {self.__total_price:,}원 주문일자: {self.__order_date}'