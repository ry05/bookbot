import sys
from stats import count_words, char_count, sort_character_counts

def get_book_text(book_path):
    with open(book_path) as f:
        book_contents = f.read()

    return book_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    book = get_book_text(path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    print("----------- Word Count ----------")
    print(count_words(book))

    print("--------- Character Count -------")

    characters = char_count(book)
    sorted_characters = sort_character_counts(characters)

    for character_record in sorted_characters:
        character = character_record["char"]
        if not character.isalpha():
            continue
        print(f"{character}: {character_record["num"]}")

main()
