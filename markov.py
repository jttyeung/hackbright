from random import choice
import sys


file_path = sys.argv[1]
ngrams = int(sys.argv[2])

def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_text = open(file_path)
    read_file = file_text.read()
    file_text.close()

    return read_file


file_string = open_and_read_file(file_path)

def make_chains(file_string, ngrams):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    index = 0
    word_list = file_string.split()
    while index < len(word_list) - ngrams:
        key_words = tuple(word_list[index:index + ngrams])
        if key_words not in chains:
            chains[key_words] = [word_list[index + ngrams]]
        else:
            chains[key_words].append(word_list[index + ngrams])
        index += 1

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    chains_key = choice(chains.keys())

    for n in range(ngrams):  # add initial ngram key words to text
        text += "{} ".format(chains_key[n])

    random_value = choice(chains.get(chains_key))  # select a random value from the ngram key words
    text += "{} ".format(random_value)  # add random initial value to text
    next_key = []  # create an empty list for the next key

    for position in range(ngrams + 1):
        if position == 0:  # skip if first position - already appended above
            pass
        elif position < ngrams:
            next_key.append(chains_key[position])
        else:
            next_key.append(random_value)

    next_key = tuple(next_key)  # rebind next_key list as a tuple

    while next_key in chains:
        try:
            random_value = choice(chains.get(next_key))
            text += "{} ".format(random_value)
            chains_key = next_key
            next_key = []

            for position in range(ngrams + 1):
                if position == 0:  # skip if first position - already appended above
                    pass
                elif position < ngrams:
                    next_key.append(chains_key[position])
                else:
                    next_key.append(random_value)

            next_key = tuple(next_key)
        except KeyError:
            break
    return text


# Open the file and turn it into one long string
input_text = open_and_read_file(file_path)

# Get a Markov chain
chains = make_chains(input_text, ngrams)

# Produce random text
random_text = make_text(chains)

print random_text
