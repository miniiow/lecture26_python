from Book.book import Book
import joblib

class BookDAO:
    BOOK_DB_FILE = 'C:/lecture/python26/OnlineBookStore/DB/bookDB.pkl'
    def __init__(self):
        self.__load_bookDB()

    # 책 데이터 로드
    def __load_bookDB(self):
        try:
            # self.__bookDB: book 객체들을 담는 딕셔너리
            self.__bookDB = joblib.load(BookDAO.BOOK_DB_FILE)
        except (FileNotFoundError, EOFError):
            self.__bookDB = {}
            self.save_bookDB()
    
    #저장
    def save_bookDB(self):
        joblib.dump(self.__bookDB, BookDAO.BOOK_DB_FILE)

    # 책 생성
    def insert_book(self, book):
        if self.is_book_exist(book.get_book_no()):
            return False
        self.__bookDB[book.get_book_no()] = book
        self.save_bookDB()
        return True
    
    # 책 전체 목록
    def select_all_books(self):
        return list(self.__bookDB.values())

    # 책 상세정보
    def select_book_info(self, book_no):
        if self.is_book_exist(book_no):
            return self.__bookDB[book_no]
        else:
            return None

    # 책 삭제
    def delete_book(self, book_no):
        if self.is_book_exist(book_no):
            self.__bookDB.pop(book_no)
            self.save_bookDB()
            return True
        else:
            return False

    # 책 수정
    def update_book(self, book_no, book):
        if self.is_book_exist(book_no):
            self.__bookDB[book_no] = book
            self.save_bookDB()
            return True
        else:
            return False

    # 등록된 책 확인
    def is_book_exist(self, book_no):
        if book_no in self.__bookDB.keys():
            return True
        return False
    
    # bookDB.pkl 파일 초기화
    def clear_bookDB(self):
        self.__bookDB = {}
        self.save_bookDB()
    
    # 책번호 최대값 조회 (없으면 0 > 백번호는 0부터 1씩증가)
    def get_max_no(self):
        if not self.__bookDB:
            return 0
        return max(int(book.get_book_no()) for book in self.__bookDB.values())


if __name__ == '__main__':
    dao = BookDAO()
    dao.clear_bookDB()
    book = Book('1', '잠자는유징', '설유진','쿨쿨출판사',5000,12)
    dao.insert_book(book)
    book = Book('2', '냠냠유징', '유진유진','냠냠출판사',2800,5)
    dao.insert_book(book)
    print(dao.is_book_exist(book.get_book_no()))
    print(dao.select_all_books())
    print('=' * 50)
    print(dao.select_book_info('1'))
    print('=' * 50)

    books = dao.select_all_books()
    for book in books:
        print(book)
    print('=' * 50)
    