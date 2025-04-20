def sort_dict(char_dict):
    char_list = []
    for char in char_dict:
        if char.isalpha():
            num = char_dict[char]
            char_list.append({"char": char, "num": num})

    def sort_on(dict):
        return dict["char"]

    char_list.sort(reverse=False, key=sort_on)
    return char_list


def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars(text):
    lowered_text = text.lower()
    char_dict = {}
    for char in lowered_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict
