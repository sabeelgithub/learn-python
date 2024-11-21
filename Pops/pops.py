library = []

def add_book_to_library(book_name,author_name):
    library.append({"book":book_name,"author":author_name})
    return "Book Added To Library"

def list_book_in_the_library():
    for book in library:
        print(f"{book.get('book')} by {book.get('author')}")

add_book_to_library("Times of India","Sabeel")
add_book_to_library("Times of Kerala","Anshida")
list_book_in_the_library()