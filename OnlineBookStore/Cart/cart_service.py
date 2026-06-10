from Cart.cart import Cart
from Cart.cart_dao import CartDAO
from Cart.cart_item import CartItem
from Cart.cart_item_dao import CartItemDAO

class CartService:
    def __init__(self, cart_dao, cart_item_dao):
        self.__dao = cart_dao
        self.__item_dao = cart_item_dao

    # 장바구니 정보 조회
    def get_cart_info(self, member_id):
        return self.__dao.select_cart_info(member_id)

    # 장바구니 삭제
    def clear_cart(self, member_id):
        self.__item_dao.delete_all_cart_items(member_id)
        if self.__dao.delete_cart(member_id):
            return True
        return False


    # 장바구니 아이템 추가
    def add_cart_item(self, member_id, book_no, count):
        if self.__dao.is_cart_exist(member_id):
            if self.__item_dao.insert_cart_item(CartItem(member_id, book_no, count)):
                return True
            return False
        return False

    # 장바구니 아이템 전체 조회
    def get_all_cart_items(self, member_id):
        return self.__item_dao.select_all_cart_items(member_id)
    
    # 장바구니 아이템 조회
    def get_cart_item(self, member_id, book_no):
        result = self.__item_dao.select_cart_item(member_id, book_no)
        if result is not None:
            return result
        return None

    # 장바구니 아이템 삭제
    def remove_cart_item(self, member_id, book_no):
        if self.__item_dao.delete_cart_item(member_id, book_no):
            return True
        return False

if __name__ == '__main__':
    dao = CartDAO()
    itemdao = CartItemDAO()
    cartsv = CartService(dao, itemdao)
    dao.clear_cartDB()
    itemdao.clear_cartItemDB()

    dao.insert_cart(Cart('dbwls'))
    dao.insert_cart(Cart('abc'))

    itemdao.insert_cart_item(CartItem('dbwls', '1', 3))
    itemdao.insert_cart_item(CartItem('dbwls', '2', 1))
    itemdao.insert_cart_item(CartItem('abc', '1', 1))

    print(dao.select_cart_info('dbwls'))

    for item in itemdao.select_all_cart_items('dbwls'):
        print(item)

    print(itemdao.delete_cart_item('dbwls', '2'))
    for item in itemdao.select_all_cart_items('dbwls'):
        print(item)

    itemdao.delete_all_cart_items('dbwls')
    print(itemdao.select_all_cart_items('dbwls'))
