def get_num_words(book_content):
        num_words = 0
        words = book_content.split()
        for word in words:
            num_words += 1
        return num_words

def letter_count(book_content):
    letters = {}
    words = book_content.lower()
    for text in words:
        if text in letters: 
            letters[text] += 1
        else:
            letters[text] = 1
    return letters
