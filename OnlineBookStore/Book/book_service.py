from Book.book import Book
from Book.book_dao import BookDAO

class BookService:
    def __init__(self, book_dao):
        self.__dao = book_dao

    # 책 추가
    def add_book(self, book):
        next_no = self.__dao.get_max_no() + 1
        book.set_book_no(str(next_no))
        return self.__dao.insert_book(book)

    # 모든 책 조회
    def get_all_books(self):
        all_books = self.__dao.select_all_books()
        if all_books:
            return all_books
        return None
    
    # 책 상세조회
    def get_book_info(self, book_no):
        book = self.__dao.select_book_info(book_no)
        if book:
            return book
        return None

    # 책 정보 수정
    def modify_book_info(self, book_no, book):
        if self.__dao.select_book_info(book_no) is not None:
            return self.__dao.update_book(book_no, book)
        return False

    # 책 삭제
    def remove_book(self, book_no, book):
        if book:
            return self.__dao.delete_book(book_no)
        return False
    
if __name__ == '__main__':
    dao = BookDAO()
    dao.clear_bookDB()
    booksv = BookService(dao)

    book = booksv.get_all_books()
    if book is None:
        print('* 등록된 책이 없습니다.')
    
    booksv.add_book(Book('1','잠자유징','설유진','쿨쿨출판사',5000,20))
    booksv.add_book(Book('1','냠냠유징','설유진','냠냠출판사',1800,3))

    for book in booksv.get_all_books():
        print(book)
    print('='*50)
    print(booksv.get_book_info('1'))
    print('책 수정','='*50)
    booksv.modify_book_info('1', Book('1','드르렁유징','설유진','쿨쿨출판사',8000,3))
    print(booksv.get_book_info('1'))