from Game.game import Game
from Game.game_dao import GameDAO


class GameService:
    def __init__(self, game_dao):
        self.__dao = game_dao

    # 게임 추가
    def add_game(self, game):
        # 게임번호 자동 부여
        next_no = self.__dao.get_max_no() + 1
        game.set_game_no(str(next_no))
        return self.__dao.insert_game(game)

    # 모든 게임 조회
    def get_all_games(self):
        all_games = self.__dao.select_all_games()
        if all_games:
            return all_games
        return None

    # 게임 상세조회
    def get_game_info(self, game_no):
        game = self.__dao.select_game_info(game_no)
        if game:
            return game
        return None

    # 게임 정보 수정
    def modify_game_info(self, game_no, game):
        if self.__dao.select_game_info(game_no) is not None:
            return self.__dao.update_game(game_no, game)
        return False

    # 게임 삭제
    def remove_game(self, game_no):
        if self.__dao.select_game_info(game_no):
            return self.__dao.delete_game(game_no)
        return False