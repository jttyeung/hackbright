# put your code here.

# import timeit
import sys


def count_words_in_file(file_name):
    text_file = open(file_name)

    word_count = {}

    for line in text_file:
        words = line.rstrip().split(' ')
        for word in words:
            word = word.strip('"').strip(')').strip('!').strip('?').strip('.').strip('/').strip(',').strip(':')
            if word == '':
                continue
            word_count[word.lower()] = word_count.get(word.lower(), 0) + 1

    text_file.close()
    return word_count


def print_dictionary(dict_name, letter="t"):
    for word, count in sorted(dict_name.items()):
        if word[0] == letter:
            print word, count


dictionary_from_file = count_words_in_file(sys.argv[1])
print_dictionary(dictionary_from_file)

# def stopwatch(file_name):
#     start_time = timeit.default_timer()
#     count_words_in_file(file_name)
#     end_time = timeit.default_timer() - start_time
#     return end_time

# text_time = stopwatch('test.txt')
# twain_time = stopwatch('twain.txt')

# print text_time, twain_time
