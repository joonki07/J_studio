class Book:
    bookname = ""
    writer = ""
    
    def set_info(self, bookname, writer = "미상"):
        self.bookname = bookname
        self.writer = writer
        
    def print_info(self):
        print("책 제목 : " + self.bookname)
        print("책 저자 : " + self.writer)
        
book1 = Book()
book2 = Book()

book1.set_info("파이썬", "민경태")
book2.set_info("어린왕자", "생텍쥐페리")

book1.print_info()
book2.print_info()
