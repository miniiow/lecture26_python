from Purchase.purchase import Purchase
import joblib


class PurchaseDAO:
    PURCHASE_DB_FILE = 'C:/lecture/python26/GameStore/DB/purchaseDB.pkl'

    def __init__(self):
        self.__load_purchaseDB()

    def __load_purchaseDB(self):
        try:
            # self.__purchaseDB: {member_no: [Purchase, Purchase, ...]} 형태의 딕셔너리
            self.__purchaseDB = joblib.load(PurchaseDAO.PURCHASE_DB_FILE)
        except (FileNotFoundError, EOFError):
            self.__purchaseDB = {}
            self.save_purchaseDB()

    # 저장
    def save_purchaseDB(self):
        joblib.dump(self.__purchaseDB, PurchaseDAO.PURCHASE_DB_FILE)

    # 구매 추가 (라이브러리에 게임 등록)
    def insert_purchase(self, purchase):
        member_no = purchase.get_member_no()
        # 회원의 라이브러리가 없으면 생성
        if member_no not in self.__purchaseDB:
            self.__purchaseDB[member_no] = []
        # 이미 구매한 게임이면 추가하지 않음
        for p in self.__purchaseDB[member_no]:
            if p.get_game_no() == purchase.get_game_no():
                return False
        self.__purchaseDB[member_no].append(purchase)
        self.save_purchaseDB()
        return True

    # 회원의 라이브러리(구매 목록) 조회
    def select_purchases_by_member(self, member_no):
        if member_no in self.__purchaseDB:
            return self.__purchaseDB[member_no]
        return None

    # 회원이 특정 게임을 구매했는지 확인
    def is_purchased(self, member_no, game_no):
        if member_no not in self.__purchaseDB:
            return False
        for p in self.__purchaseDB[member_no]:
            if p.get_game_no() == game_no:
                return True
        return False

    # 회원 탈퇴 시 해당 회원의 라이브러리 전체 삭제
    def delete_all_purchases(self, member_no):
        if member_no in self.__purchaseDB:
            self.__purchaseDB.pop(member_no)
            self.save_purchaseDB()
            return True
        return False

    # 게임 삭제 시 모든 회원의 라이브러리에서 해당 게임 제거
    def delete_purchases_by_game(self, game_no):
        for member_no in list(self.__purchaseDB.keys()):
            self.__purchaseDB[member_no] = [
                p for p in self.__purchaseDB[member_no]
                if p.get_game_no() != game_no
            ]
            # 라이브러리가 비면 키 자체 제거
            if not self.__purchaseDB[member_no]:
                self.__purchaseDB.pop(member_no)
        self.save_purchaseDB()
        return True

    # 게임 삭제 시 모든 회원의 라이브러리에서 해당 게임 제거
    # 회원이 구매한 게임번호가 삭제하려는 게임번호와 다르면 남기고 맞다면 리스트에 추가하지 않음
    def delete_purchases_by_game(self, game_no):
       
        non_game_members = []
        for member_no in self.__purchaseDB:
            new_game_list = []
            for purchase in self.__purchaseDB[member_no]:
                if purchase.get_game_no() != game_no:
                    new_game_list.append(purchase)
            self.__purchaseDB[member_no] = new_game_list
            if len(new_game_list) == 0:
                non_game_members.append(member_no)
        for member_no in non_game_members:      # 게임 삭제 후 구매목록이 비워진 회원은 DB에서 정리
            self.__purchaseDB.pop(member_no)
        self.save_purchaseDB()
        return True

    # 전체 구매 데이터 (관리자용)
    def select_all_purchases(self):
        return self.__purchaseDB

    # purchaseDB.pkl 파일 초기화
    def clear_purchaseDB(self):
        self.__purchaseDB = {}
        self.save_purchaseDB()