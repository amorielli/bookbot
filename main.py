def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    char_dict = count_char(file_contents)

    char_list = []
    for char in char_dict:
        if char.isalpha():
            num = char_dict[char]
            char_list.append({"char":char, "num":num})

    def sort_on(dict):
        return dict["char"]

    char_list.sort(reverse=False, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document\n")
    for char_dict in char_list:
        char = char_dict["char"]
        num = char_dict["num"]
        print(f"The '{char}' character was found {num} times")
    print("--- End report ---")

def count_char(text):
    lowered_text = text.lower()
    char_dict = {}
    for char in lowered_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

main()

