class Game:
    def __init__(self, game_no, title, maker, price):
        self.__game_no = game_no    # 게임번호
        self.__title = title        # 게임이름
        self.__maker = maker        # 제작사
        self.__price = price        # 가격

    def get_game_no(self):
        return self.__game_no
    def get_title(self):
        return self.__title
    def get_maker(self):
        return self.__maker
    def get_price(self):
        return self.__price

    def set_game_no(self, game_no):
        self.__game_no = game_no
    def set_title(self, title):
        self.__title = title
    def set_maker(self, maker):
        self.__maker = maker
    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return f'[{self.__game_no}] 게임이름: {self.__title} 제작사: {self.__maker} 가격: {self.__price}원'
