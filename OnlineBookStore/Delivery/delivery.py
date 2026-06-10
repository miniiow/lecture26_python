class Delivery:
    # 배송상태
    STATUS = {1: '발송준비', 2: '발송완료', 3: '배송중', 4: '배송완료'}

    def __init__(self, member_id, delivery_no, order_no, delivery_date= None, delivery_address=None):
        self.__member_id = member_id
        self.__delivery_no = delivery_no
        self.__order_no = order_no
        self.__delivery_date = delivery_date
        self.__delivery_status = 1
        self.__delivery_address = delivery_address

    def get_member_id(self):
        return self.__member_id
    def get_delivery_no(self):
        return self.__delivery_no
    def get_order_no(self):
        return self.__order_no
    def get_delivery_date(self):
        return self.__delivery_date
    def get_delivery_status(self):
        return self.__delivery_status
    def get_delivery_address(self):
        return self.__delivery_address
    def get_status_text(self):
        Delivery.STATUS.get(self.__delivery_status, '알수없음')

    def set_member_id(self, member_id):
        self.__member_id = member_id
    def set_delivery_no(self, delivery_no):
        self.__delivery_no = delivery_no
    def set_order_no(self, order_no):
        self.__order_no = order_no
    def set_delivery_date(self, delivery_date):
        self.__delivery_date = delivery_date  
    def set_delivery_address(self, delivery_address):
        self.__delivery_address = delivery_address
    def set_delivery_status(self, delivery_status):
        if delivery_status not in Delivery.STATUS:
            return False
        self.__delivery_status = delivery_status
        return True 

    def __str__(self):
        return f'회원아이디: {self.__member_id} 배송번호: {self.__delivery_no} 주문번호: {self.__order_no}\n날짜: {self.__delivery_date} 상태: {self.get_status_text()} 주소: {self.__delivery_address}'