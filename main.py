def main():

    def get_book_text(filepath):
     with open(filepath) as f:
            return f.read()

   
    book_content = get_book_text("books/frankenstein.txt")

   
    def num_of_words(book_content):
        num_words = 0
        words = book_content.split()
        for word in words:
            num_words += 1
        return num_words
    

    num_words = num_of_words(book_content) 


    print(f"{num_words} words found in document")

main()
