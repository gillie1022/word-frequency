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

def get_output_list(a_dict):
    output_list = []
    i = 0
    for item in a_dict.items():
        if i < 10:
            output_list.append(item)
            i += 1
    return output_list

def get_first_value(seq):
    return seq[0]

def get_second_value(seq):
    return seq[1]

def get_output_word_list(a_list):
    return[
        get_first_value(item)
        for item in a_list
    ]

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    opened_file = file.open()
    text = opened_file.read()
    words = clean_text(text).split()
    word_list = remove_from_list(words, STOP_WORDS)
    word_dict = get_word_dict(word_list)
    alpha_dict = dict(sorted(word_dict.items()))
    sorted_dict = dict(sorted(alpha_dict.items(), key=get_second_value, reverse=True))
    output_list = get_output_list(sorted_dict)
    output_word_list =  get_output_word_list(output_list)
    longest_word = get_longest_word(output_word_list)
    for item in output_list:
        print(f"{get_first_value(item).rjust(len(longest_word) + 2)} | {str(get_second_value(item)).ljust(3)}{int(get_second_value(item)) * '*'}")



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
