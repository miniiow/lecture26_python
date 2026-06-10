from Order.order import Order
import joblib

class OrderDAO:
    ORDER_DB_FILE = 'C:/lecture/python26/OnlineBookStore' \
    '/DB/orderDB.pkl'
    def __init__(self):
        self.__load_orderDB()

    # 주문 데이터 로드
    def __load_orderDB(self):
        try:
            self.__orderDB = joblib.load(OrderDAO.ORDER_DB_FILE)
        except (FileNotFoundError, EOFError):
            self.__orderDB = {}
            self.save_orderDB()

    # 저장
    def save_orderDB(self):
        joblib.dump(self.__orderDB, OrderDAO.ORDER_DB_FILE)

    # 주문 생성
    def insert_order(self, order):
        if self.is_order_exist(order.get_member_id(), order.get_order_no()):
            return False
        self.__orderDB[(order.get_member_id(), order.get_order_no())] = order
        self.save_orderDB()
        return True

    # 주문 전체 조회
    def select_all_orders(self, member_id):
        result = []
        for key, order in self.__orderDB.items():
            if key[0] == member_id:
                result.append(order)
        if not result:
            return None
        return result
    
    # 회원의 주문 전체 삭제
    def delete_all_orders(self, member_id):
        member_key = []
        for key in self.__orderDB.keys():
            if key[0] == member_id:
                member_key.append(key)
        if not member_key:
            return False
        for key in member_key:
            self.__orderDB.pop(key)
        self.save_orderDB()
        return True

    # 주문 삭제
    def delete_order(self, member_id, order_no):
        if self.is_order_exist(member_id, order_no):
            self.__orderDB.pop((member_id, order_no))
            self.save_orderDB()
            return True
        return False

    # 주문 여부 확인
    def is_order_exist(self, member_id, order_no):
        if (member_id, order_no) in self.__orderDB.keys():
            return True
        return False
    
    # orderDB.pkl 파일 초기화
    def clear_orderDB(self):
        self.__orderDB = {}
        self.save_orderDB()

    # 주문번호 최대값 조회 (없으면 999 > 주문번호는 1000부터 1씩증가)
    def get_max_no(self):
        if not self.__orderDB:
            return 999
        return max(int(order.get_order_no()) for order in self.__orderDB.values())

if __name__ == '__main__':
    dao = OrderDAO()
    dao.clear_orderDB()

    item1 = Order('1', 'dbwls', 2500, '2025-01-01')
    item2 = Order('2', 'dbwls', 2500, '2025-01-01')
    item3 = Order('3', 'dbwls', 48000, '2026-02-12')
    dao.insert_order(item1)
    dao.insert_order(item2)
    dao.insert_order(item3)

    print('목록조회')
    items = dao.select_all_orders('dbwls')
    for item in items:
        print(item)

    dao.delete_order('dbwls', '2')
    print('삭제 후 목록조회')
    items = dao.select_all_orders('dbwls')
    for item in items:
        print(item)