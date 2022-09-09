class Library:
    def __init__(self, listOfBooks) -> None:
        self.books = listOfBooks

    def displayAvaibleOfBooks(self):
        print("Books present in this library are : ")
        for book in self.books:
            print("\t*" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(
                f"you have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry ,This book is either not available or has already been issued to someone else. Please wait untill the book is available")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this books !Hope you enjoy readind it ")


class Student:
    def requestBook(self):
        self.book = input("Enter the name of book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of book you want to return: ")
        return self.book


if __name__ == "__main__":
    centralLibrary = Library(["Algoritdhm", "Django", "clrs", "Python"])
    centralLibrary.displayAvaibleOfBooks()
    student = Student()
    while(True):
        welcomeMsg = '''=====welcome to central library=====
                    please choose an option:
                    1. Listing  all the books
                    2. Request a book
                    3. Add/Return a book
                    4. Exit the Library  
                    '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvaibleOfBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for chosing library ")
            exit()
        else:
            print("Invaild choice!")