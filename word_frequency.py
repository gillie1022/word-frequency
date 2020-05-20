STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def clean_text(text):
    punct = "!\"#$%&'()*+,./:;<=>?@[\]^_`{|}~"
    text = text.lower()
    text_to_keep = ""
    for char in text:
        if not char in punct:
            text_to_keep += char
    return text_to_keep

def get_longest_word(text):
    longest = None
    for word in text:
        if longest is None or len(word) > len(longest):
            longest = word
    return longest

def remove_from_list(list_of_items, items_to_remove):
    return [
        item
        for item in list_of_items
        if not item in items_to_remove
    ]

def get_word_dict(word_list):
    return {
        word: word_list.count(word)
        for word in word_list
    }

def get_count_value(seq):
    return seq[1]

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    opened_file = file.open()
    text = opened_file.read()
    words = clean_text(text).split()
    word_list = remove_from_list(words, STOP_WORDS)
    longest_word = get_longest_word(word_list)
    word_dict = get_word_dict(word_list)
    alpha_dict = dict(sorted(word_dict.items()))
    sorted_dict = dict(sorted(alpha_dict.items(), key=get_count_value, reverse=True))
    for word, value in sorted_dict.items():
        if value > 5:
            print(f"{word.rjust(len(longest_word))} | {str(value).ljust(2)} {value * '*'}")
        


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
