def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    words_count = get_words_count(text)
    print(f"Book has {words_count} words.")
    chars_count = get_char_count(text)
    print(chars_count)


def get_text(path):
    with open(path, "r") as f:
        text = f.read()
        return text


def get_words_count(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    text = text.lower()
    chars = dict()
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


main()
