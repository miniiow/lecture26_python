from Cart.cart import Cart
import joblib

class CartDAO:
    CART_DB_FILE = 'C:/lecture/python26/OnlineBookStore/DB/cartDB.pkl'
    def __init__(self):
        self.__load_cartDB()

    # 장바구니 데이터 로드
    def __load_cartDB(self):
        try:
            self.__cartDB = joblib.load(CartDAO.CART_DB_FILE)
        except (FileNotFoundError, EOFError):
            self.__cartDB = {}
            self.save_cartDB()

    # 저장
    def save_cartDB(self):
        joblib.dump(self.__cartDB, CartDAO.CART_DB_FILE)

    # 장바구니 생성
    # 모든 회원은 하나의 장바구니만 가질 수 있음
    def insert_cart(self, cart):
        if self.is_cart_exist(cart.get_member_id()):
            return False
        self.__cartDB[cart.get_member_id()] = cart
        self.save_cartDB()
        return True

    # 장바구니 목록 조회
    def select_cart_info(self, member_id):
        if self.is_cart_exist(member_id):
            return self.__cartDB[member_id]
        return None

    # 장바구니 삭제
    def delete_cart(self, member_id):
        if self.is_cart_exist(member_id):
            self.__cartDB.pop(member_id)
            self.save_cartDB()
            return True
        return False

    # 장바구니 여부 조회
    def is_cart_exist(self, member_id):
        if member_id in self.__cartDB.keys():
            return True
        return False

    # cartDB.pkl 파일 초기화
    def clear_cartDB(self):
        self.__cartDB = {}
        self.save_cartDB()

if __name__ == '__main__':
    dao = CartDAO()
    dao.clear_cartDB()

    cart1 = Cart('dbwls')
    cart2 = Cart('abc')
    print(dao.insert_cart(cart1))
    print(dao.insert_cart(cart2))
    print(dao.insert_cart(cart1))
    print(dao.select_cart_info('dbwls'))
    print(dao.select_cart_info('abc'))

    dao.delete_cart('abc')
    result = dao.select_cart_info('abc')
    if result is None:
        print('장바구니가 없는 회원입니다.')
    else:
        print(result)
    