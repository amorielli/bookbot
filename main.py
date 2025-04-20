import sys

from stats import get_num_chars, get_num_words, sort_dict


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    char_dict = get_num_chars(text)
    char_list = sort_dict(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    for char_dict in char_list:
        char = char_dict["char"]
        num = char_dict["num"]
        print(f"The '{char}' character was found {num} times")
    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


main()
