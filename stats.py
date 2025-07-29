def get_num_words(book_content):
        num_words = 0
        words = book_content.split()
        for word in words:
            num_words += 1
        return num_words