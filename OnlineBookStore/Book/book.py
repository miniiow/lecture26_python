class Book:
    def __init__(self, book_no, title, author, publisher, price, stock):
        self.__book_no = book_no
        self.__title = title
        self.__author = author
        self.__publisher = publisher
        self.__price = price
        self.__stock = stock

    def get_book_no(self):
        return self.__book_no
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_publisher(self):
        return self.__publisher
    def get_price(self):
        return self.__price
    def get_stock(self):
        return self.__stock
    
    def set_book_no(self, book_no):
        self.__book_no = book_no
    def set_book_stock(self, stock):
        self.__stock = stock

    def __str__(self):
        return f'책번호: {self.__book_no} 책제목: {self.__title}\n저자: {self.__author} 출판사: {self.__publisher} 가격: {self.__price} 재고: {self.__stock}'