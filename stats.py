from collections import Counter

def count_words(text):
    num_words = len(text.split())
    return f"Found {num_words} total words"

def char_count(text):
    text_lower = text.lower()
    return dict(Counter(text_lower))

def sort_character_counts(characters):
    character_records = [{"char": char, "num": count} for char, count in characters.items()]
    character_records.sort(key=_get_count, reverse=True)
    return character_records

def _get_count(character_record):
    return character_record["num"]