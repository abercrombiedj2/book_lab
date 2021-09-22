import pdb
from models.author import Author
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

author_1 = Author("J.K.", "Rowling")
author_repository.save(author_1)
author_2 = Author("J.R.R.", "Tolkien")
author_repository.save(author_2)
author_3 = Author("Roald", "Dahl")
author_repository.save(author_3)

book_1 = Book("Harry Potter", author_1, "Modern Classics")
book_repository.save(book_1)
book_2 = Book("Lord of the Rings", author_2, "Pengiun Classics")
book_repository.save(book_2)
book_3 = Book("Willy Wonka", author_3, "Childrens Classics")
book_repository.save(book_3)

book_repository.select_all()

pdb.set_trace()