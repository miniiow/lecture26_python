class DeliveryService:
    # 배송번호는 1000부터 1씩 증가
    delivery_no_seq = 1000

    def __init__(self, delivery_dao):
        self.__dao = delivery_dao

    # 배송 추가
    def add_delivery(self, delivery):
        next_no = self.__dao.get_max_no()+1
        delivery.set_delivery_no(str(next_no))
        return self.__dao.insert_delivery(delivery)

    # 관리자-전체 배송 조회
    def get_all_deliveries(self):
        return self.__dao.select_all_deliveries()

    # 회원 배송 전체 조회
    def get_member_delivery(self, member_id):
        return self.__dao.select_member_all_delivery(member_id)

    # 배송 상세 조회
    def get_delivery_info(self, member_id, delivery_no):
        return self.__dao.select_delivery_info(member_id, delivery_no)

    # 배송 상태 수정
    def modify_delivery_status(self, member_id, delivery_no, status):
        if self.__dao.update_delivery_status(member_id, delivery_no, status):
            return True
        return False

    # 배송 날짜 수정
    def modify_delivery_date(self, member_id, delivery_no, delivery_date):
        if self.__dao.update_delivery_date(member_id, delivery_no, delivery_date):
            return True
        return False
    
    # 회원 배송 전체 삭제
    def remove_all_deliveries(self, member_id):
        return self.__dao.delete_all_deliveries(member_id)

    # 배송 삭제
    def remove_delivery(self, member_id, delivery_no):
        if self.__dao.delete_delivery(member_id, delivery_no):
            return True
        return False