from Order.order import Order
from Order.order_dao import OrderDAO
from Order.order_item_dao import OrderItemDAO

class OrderService:    
    def __init__(self, order_dao, order_item_dao):
        self.__dao = order_dao
        self.__item_dao = order_item_dao

    # 주문 추가
    def add_order(self, order):
        next_no = self.__dao.get_max_no() + 1
        order.set_order_no(str(next_no))
        return self.__dao.insert_order(order)
    
    # 회원 주문 전체 삭제
    def remove_all_orders(self, member_id):
        return self.__dao.delete_all_orders(member_id)

    # 주문 삭제
    def remove_order(self, member_id, order_no):
        return self.__dao.delete_order(member_id, order_no)

    # 주문 정보 조회
    def get_order_info(self, member_id):
        return self.__dao.select_all_orders(member_id)

    # 주문 아이템 추가
    def add_order_item(self, order_item):
        return self.__item_dao.insert_order_item(order_item)

    # 주문 아이템 조회
    def get_order_item(self, member_id):
        result = self.__item_dao.select_all_order_items(member_id)
        if result is not None:
            return result
        return None
    

    # 주문 아이템 삭제
    def remove_order_item(self, member_id):
        if self.__item_dao.delete_all_order_items(member_id):
            return True
        return False
    
if __name__ == '__main__':
    dao = OrderDAO()
    item_dao = OrderItemDAO()
    osv = OrderService(dao, item_dao)

    dao.clear_orderDB()