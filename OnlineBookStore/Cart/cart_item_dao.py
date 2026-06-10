from Cart.cart_item import CartItem
import joblib

class CartItemDAO:
    CART_ITEM_DB_FILE = 'C:/lecture/python26/OnlineBookStore/DB/cartItemDB.pkl'
    def __init__(self):
        self.__load_cartItemDB()

    def __load_cartItemDB(self):
        try:
            self.__cartItemDB = joblib.load(CartItemDAO.CART_ITEM_DB_FILE)
        except (FileNotFoundError, EOFError):
            self.__cartItemDB = {}
            self.save_cartItemDB()

    def save_cartItemDB(self):
        joblib.dump(self.__cartItemDB, CartItemDAO.CART_ITEM_DB_FILE)

    # 장바구니 아이템 생성
    def insert_cart_item(self, cartItem):
        if self.is_cart_item_exist(cartItem.get_member_id(), cartItem.get_book_no()):
            return False
        # key값으로 member_id와 book_no를 같이 사용 > 한 회원이 같은 책을 중복해서 장바구니에 담을 수 없음
        key = (cartItem.get_member_id(), cartItem.get_book_no()) 
        self.__cartItemDB[key] = cartItem
        self.save_cartItemDB()
        return True
    
    # 장바구니 아이템 전체조회
    def select_all_cart_items(self, member_id):
        result = []
        for key, item in self.__cartItemDB.items():
            if key[0] == member_id:
                result.append(item)
        if not result:
            return None
        return result

    # 장바구니 아이템 한 개 조회
    def select_cart_item(self, member_id, book_no):
        if self.is_cart_item_exist(member_id, book_no):
            return self.__cartItemDB[(member_id, book_no)]
        return None

    # 장바구니 아이템 삭제
    def delete_cart_item(self, member_id, book_no):
        if self.is_cart_item_exist(member_id, book_no):
            self.__cartItemDB.pop((member_id, book_no))
            self.save_cartItemDB()
            return True
        return False

    # 장바구니 아이템 전체 삭제
    def delete_all_cart_items(self, member_id):
        member_key = []
        for key in self.__cartItemDB.keys():
            if key[0] == member_id:
                member_key.append(key)
        if not member_key:
            return False
        for _ in member_key:
            self.__cartItemDB.pop(_)
        self.save_cartItemDB()
        return True


    # 장바구니 여부 조회
    def is_cart_item_exist(self, member_id, book_no):
        if (member_id, book_no) in self.__cartItemDB.keys():
            return True
        return False

    # cartItemDB.pkl 파일 초기화
    def clear_cartItemDB(self):
        self.__cartItemDB = {}
        self.save_cartItemDB()

if __name__ == '__main__':
    dao = CartItemDAO()
    dao.clear_cartItemDB()

    item1 = CartItem('dbwls', '1', 3)
    item2 = CartItem('dbwls', '2', 1)
    item3 = CartItem('dbwls', '3', 4)
    dao.insert_cart_item(item1)
    dao.insert_cart_item(item2)
    dao.insert_cart_item(item3)

    print('목록조회')
    print(dao.select_cart_item('dbwls', '1'))
    print(dao.select_cart_item('dbwls', '2'))
    print(dao.select_cart_item('dbwls', '3'))

    dao.delete_cart_item('dbwls', '2')
    print('삭제 후 목록조회')
    items = dao.select_all_cart_items('dbwls')
    for item in items:
        print(item)

    