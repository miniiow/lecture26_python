import joblib

class DeliveryDAO:
    DELIVERY_DB_FILE = 'C:/lecture/python26/OnlineBookStore/DB/deliveryDB.pkl'
    def __init__(self):
        self.__load_deliveryDB()

    def __load_deliveryDB(self):
        try:
            self.__deliveryDB = joblib.load(DeliveryDAO.DELIVERY_DB_FILE)
        except (FileNotFoundError, EOFError):
            self.__deliveryDB = {}
            self.save_deliveryDB()

    def save_deliveryDB(self):
        joblib.dump(self.__deliveryDB, DeliveryDAO.DELIVERY_DB_FILE)

    # 배송 생성
    def insert_delivery(self, delivery):
        if self.is_delivery_exist(delivery.get_member_id(), delivery.get_delivery_no()):
            return False
        key = (delivery.get_member_id(), delivery.get_delivery_no())
        self.__deliveryDB[key] = delivery
        self.save_deliveryDB()
        return True

    # 전체 배송 조회 (관리자용)
    def select_all_deliveries(self):
        return list(self.__deliveryDB.values())

    # 회원 배송 전체 조회
    def select_member_all_delivery(self, member_id):
        result = []
        for key, delivery in self.__deliveryDB.items():
            if key[0] == member_id:
                result.append(delivery)
        return result

    # 배송 상세 조회
    def select_delivery_info(self, member_id, delivery_no):
        if self.is_delivery_exist(member_id, delivery_no):
            return self.__deliveryDB[(member_id, delivery_no)]
        return None
    
    # 회원의 배송 전체 삭제
    def delete_all_deliveries(self, member_id):
        member_key = []
        for key in self.__deliveryDB.keys():
            if key[0] == member_id:
                member_key.append(key)
        if not member_key:
            return False
        for key in member_key:
            self.__deliveryDB.pop(key)
        self.save_deliveryDB()
        return True

    # 배송 삭제
    def delete_delivery(self, member_id, delivery_no):
        if self.is_delivery_exist(member_id, delivery_no):
            self.__deliveryDB.pop((member_id, delivery_no))
            self.save_deliveryDB()
            return True
        return False

    # 배송 상태 수정
    def update_delivery_status(self, member_id, delivery_no, status):
        if self.is_delivery_exist(member_id, delivery_no):
            if self.__deliveryDB[(member_id, delivery_no)].set_delivery_status(status):
                self.save_deliveryDB()
                return True
        return False
    
    # 배송 날짜 수정 (배송완료시 변경)
    def update_delivery_date(self, member_id, delivery_no, delivery_date):
        if self.is_delivery_exist(member_id, delivery_no):
            self.__deliveryDB[(member_id, delivery_no)].set_delivery_date(delivery_date)
            self.save_deliveryDB()
            return True
        return False

    # 배송 여부 확인
    def is_delivery_exist(self, member_id, delivery_no):
        if (member_id, delivery_no) in self.__deliveryDB.keys():
            return True
        return False

    # deliveryDB.pkl 초기화
    def clear_deliveryDB(self):
        self.__deliveryDB = {}
        self.save_deliveryDB()

    # 배송번호 최대값 조회 (없으면 999 > 배송번호는 1000부터 1씩증가)
    def get_max_no(self):
        if not self.__deliveryDB:
            return 999
        return max(int(delivery.get_delivery_no()) for delivery in self.__deliveryDB.values())