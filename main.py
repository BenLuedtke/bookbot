import sys
from stats import count_words, count_characters,sort_counts


def get_book_text(filepath:str) -> str:
    '''Takes filepath as an input and returns text as a string'''
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif len(sys.argv) == 2:
        _,path_to_book = sys.argv

        book_text = get_book_text(path_to_book)
        number_of_words = count_words(book_text)
        sorted_chars = sort_counts(count_characters(book_text))
        print('============ BOOKBOT ============')
        print('Analyzing book found at books/frankenstein.txt...')
        print('----------- Word Count ----------')
        print(f'Found {number_of_words} total words')
        print('--------- Character Count -------')
        for i in sorted_chars:
            if i["char"].isalpha() == True:
                print(i['char'] + ": " + str(i['num']))



main()