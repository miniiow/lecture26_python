from Game.game import Game
import joblib


class GameDAO:
    GAME_DB_FILE = 'C:/lecture/python26/GameStore/DB/gameDB.pkl'

    def __init__(self):
        self.__load_gameDB()

    def __load_gameDB(self):
        try:
            # self.__gameDB: game_no를 key로 하는 딕셔너리
            self.__gameDB = joblib.load(GameDAO.GAME_DB_FILE)
        except (FileNotFoundError, EOFError):
            self.__gameDB = {}
            self.save_gameDB()

    # 저장
    def save_gameDB(self):
        joblib.dump(self.__gameDB, GameDAO.GAME_DB_FILE)

    # 게임 추가
    def insert_game(self, game):
        if self.is_game_exist(game.get_game_no()):
            return False
        self.__gameDB[game.get_game_no()] = game
        self.save_gameDB()
        return True

    # 게임 전체 목록
    def select_all_games(self):
        return list(self.__gameDB.values())

    # 게임 상세 조회
    def select_game_info(self, game_no):
        if self.is_game_exist(game_no):
            return self.__gameDB[game_no]
        return None

    # 게임 삭제
    def delete_game(self, game_no):
        if self.is_game_exist(game_no):
            self.__gameDB.pop(game_no)
            self.save_gameDB()
            return True
        return False

    # 게임 수정
    def update_game(self, game_no, game):
        if self.is_game_exist(game_no):
            self.__gameDB[game_no] = game
            self.save_gameDB()
            return True
        return False

    # 등록된 게임 확인
    def is_game_exist(self, game_no):
        if game_no in self.__gameDB.keys():
            return True
        return False

    # gameDB.pkl 파일 초기화
    def clear_gameDB(self):
        self.__gameDB = {}
        self.save_gameDB()

    # 게임번호 최대값 조회 (없으면 0 -> 게임번호는 1부터 1씩 증가)
    def get_max_no(self):
        if not self.__gameDB:
            return 0
        max_no = 0
        for game in self.__gameDB.values():
            game_no = int(game.get_game_no())
            if game_no > max_no:
                max_no = game_no
        return max_no
