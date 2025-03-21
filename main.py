from stats import get_words_count


def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    words_count = get_words_count(text)
    chars_count = get_char_count(text)
    sorted_list = convert_dict_to_sorted_list(chars_count)
    print_report(sorted_list, book_path, words_count)


def get_text(path):
    with open(path, "r") as f:
        text = f.read()
        return text


def get_char_count(text):
    text = text.lower()
    chars = dict()
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def sort_on(dict):
    return dict["count"]


def convert_dict_to_sorted_list(chars_count):
    sorted_list = []
    for ch in chars_count:
        sorted_list.append({"char": ch, "count": chars_count[ch]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list


def print_report(sorted_list, book_path, num_words):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['count']} times")
    print("--- End report ---")


main()
