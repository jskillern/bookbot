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


def letter_list(letters):
    char_list = []
    for letter in letters:
        count = letters[letter]
        char_dict = {"char": letter, "num": count}
        char_list.append(char_dict)
    return char_list


def sort_on(letters):
     return letters["num"]