import sys
from stats import get_num_words
from stats import get_num_characters
from stats import sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    num = get_num_words(get_book_text(filepath))
    print(f'Found {num} total words.')
    chars = sorted_list(get_num_characters(get_book_text(filepath)))
    print(f'Character counts: {chars}')

    for char_dict in chars:
        char = char_dict["char"]
        if char.isalpha():  # Only print alphabetic characters
            print(f'{char}: {char_dict["num"]}')

main()