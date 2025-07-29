def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read
        return f.read()

def main():
    book_content = get_book_text("books/frankenstein.txt")
    print(book_content)


main()
