class Purchase:
    def __init__(self, member_no, game_no):
        self.__member_no = member_no    # 회원번호
        self.__game_no = game_no        # 게임번호

    def get_member_no(self):
        return self.__member_no
    def get_game_no(self):
        return self.__game_no

    def set_member_no(self, member_no):
        self.__member_no = member_no
    def set_game_no(self, game_no):
        self.__game_no = game_no

    def __str__(self):
        return f'회원번호: {self.__member_no} / 게임번호: {self.__game_no}'