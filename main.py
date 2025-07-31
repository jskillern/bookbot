from stats import get_num_words
from stats import letter_count
from stats import letter_list
from stats import sort_on
import sys


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filename = sys.argv[1]

    def get_book_text(filepath):
     with open(filepath) as f:
            return f.read()

   
    book_content = get_book_text(filename)

    num_words = get_num_words(book_content) 

    letters = letter_count(book_content)

    char_list = letter_list(letters)

    char_list.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filename}...")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count ---------")
    

    for char_dict in char_list:
        if char_dict["char"].isalpha():
            print(f'{char_dict["char"]}: {char_dict["num"]}')


main()
