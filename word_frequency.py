STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def clean_text(text):
    import string
    text = text.lower()
    text_to_keep = ""
    for char in text:
        if not char in string.punctuation:
            text_to_keep += char
    return text_to_keep

def remove_from_list(list_of_items, items_to_remove):
    new_list = []
    for item in list_of_items:
        if not item in items_to_remove:
            new_list.append(item)
    return(new_list)

def get_word_dict(word_list):
    word_dict = {}
    for idx in range(len(word_list)):
        word_dict[word_list[idx]] = word_list.count(word_list[idx])
    return word_dict

def format_output(sorted_dict):
    for word in sorted_dict:
        return f""


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    opened_file = file.open()
    text = opened_file.read()
    words = clean_text(text).split()
    word_list = remove_from_list(words, STOP_WORDS)
    word_dict = get_word_dict(word_list)
    sorted_dict = sorted(word_dict.items(), key = lambda x: x[1], reverse=True)
    print(sorted_dict)
        






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
