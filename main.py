from stats import get_num_words
from stats import letter_count

def main():


    def get_book_text(filepath):
     with open(filepath) as f:
            return f.read()

   
    book_content = get_book_text("books/frankenstein.txt")


    num_words = get_num_words(book_content) 


    print(f"{num_words} words found in the document")
    print(letter_count(book_content))

main()
