from Purchase.purchase import Purchase
from Purchase.purchase_dao import PurchaseDAO


class PurchaseService:
    def __init__(self, purchase_dao):
        self.__dao = purchase_dao

    # 게임 구매 (라이브러리에 추가)
    def buy_game(self, member_no, game_no):
        purchase = Purchase(member_no, game_no)
        return self.__dao.insert_purchase(purchase)

    # 회원의 라이브러리 조회
    def get_my_library(self, member_no):
        return self.__dao.select_purchases_by_member(member_no)

    # 이미 구매한 게임인지 확인
    def is_purchased(self, member_no, game_no):
        return self.__dao.is_purchased(member_no, game_no)

    # 회원 탈퇴 시 라이브러리 삭제
    def remove_member_library(self, member_no):
        return self.__dao.delete_all_purchases(member_no)

    # 게임 삭제 시 모든 라이브러리에서 게임 제거
    def remove_game_from_all(self, game_no):
        return self.__dao.delete_purchases_by_game(game_no)

    # 전체 구매 데이터 조회 (관리자용)
    def get_all_purchases(self):
        return self.__dao.select_all_purchases()
