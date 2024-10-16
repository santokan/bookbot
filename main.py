def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    words_count = get_words_count(text)
    print(f"Book has {words_count} words.")


def get_text(path):
    with open(path, "r") as f:
        text = f.read()
        return text


def get_words_count(text):
    words = text.split()
    return len(words)


main()
