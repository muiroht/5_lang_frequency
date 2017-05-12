import sys
import os
import re
import collections
import pprint


def load_data(filepath):
    if not os.path.exists(filepath):
        sys.exit('File does not exists: {0}'.format(filepath))
    return open(filepath, 'r')


def make_words_counter(file_handler):
    words_counter = collections.Counter()
    for line in file_handler:
        words = [word.lower() for word in re.split('\W+', line) if word]
        words_counter.update(words)
    return words_counter


def get_most_frequent_words(words_counter, count):
    return [x[0] for x in words_counter.most_common(count)]


def print_freq_words(word_list):
    pprint.pprint(word_list)


if __name__ == '__main__':
    count_required_sys_args = 2
    count_freq_words = 10
    if len(sys.argv) != count_required_sys_args:
        sys.exit('Usage: python lang_frequency.py <path to file>')
    file_handler = load_data(sys.argv[1])
    words_counter = make_words_counter(file_handler)
print_freq_words(get_most_frequent_words(words_counter, count_freq_words))
