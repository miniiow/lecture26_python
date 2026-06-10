from Order.order_item import OrderItem
import joblib

class OrderItemDAO:
    ORDER_ITEM_DB_FILE = 'C:/lecture/python26/OnlineBookStore/DB/orderItemDB.pkl'
    def __init__(self):
        self.__load_orderItemDB()

    def __load_orderItemDB(self):
        try:
            self.__orderItemDB = joblib.load(OrderItemDAO.ORDER_ITEM_DB_FILE)
        except (FileNotFoundError, EOFError):
            self.__orderItemDB = {}
            self.save_orderItemDB()

    def save_orderItemDB(self):
        joblib.dump(self.__orderItemDB, OrderItemDAO.ORDER_ITEM_DB_FILE)

    # 주문 아이템 생성
    def insert_order_item(self, order_item):
        if self.is_order_item_exist(order_item.get_order_no(), order_item.get_book_no()):
            return False
        key = (order_item.get_member_id(), order_item.get_order_no(), order_item.get_book_no())
        self.__orderItemDB[key] = order_item
        self.save_orderItemDB()
        return True

    # 주문 아이템 전체조회
    def select_all_order_items(self, member_id):
        result = []
        for key, item in self.__orderItemDB.items():
            if key[0] == member_id:
                result.append(item)
        if not result:
            return None
        return result

    # 주문 아이템 전체 삭제
    def delete_all_order_items(self, member_id):
        member_key = []
        for key in self.__orderItemDB.keys():
            if key[0] == member_id:
                member_key.append(key)
        if not member_key:
            return False
        for _ in member_key:
            self.__orderItemDB.pop(_)
        self.save_orderItemDB()
        return True

    # 주문 아이템 여부 확인
    def is_order_item_exist(self, order_no, book_no):
        for key in self.__orderItemDB.keys():
            if key[1] == order_no and key[2] == book_no:
                return True
        return False
    
    # orderItemDB.pkl 파일 초기화
    def clear_orderItemDB(self):
        self.__orderItemDB = {}
        self.save_orderItemDB()

if __name__ == '__main__':
    dao = OrderItemDAO()
    dao.clear_orderItemDB()

    item1 = OrderItem('dbwls','1000', '1', 3, 27000)
    item2 = OrderItem('dbwls','1001', '2', 1, 13000)
    item3 = OrderItem('dbwls','1002', '3', 5, 48000)
    dao.insert_order_item(item1)
    dao.insert_order_item(item2)
    dao.insert_order_item(item3)

    items = dao.select_all_order_items('dbwls')
    for item in items:
        print(item)

    dao.delete_all_order_items('dbwls')
    items = dao.select_all_order_items('dbwls')
    if items is None:
        print('주문 아이템 없음')
    else:
        for item in items:
            print(item)