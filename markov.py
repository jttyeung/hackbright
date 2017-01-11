from random import choice
import sys


file_path = "green-eggs.txt"


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

def make_chains(text_string):
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
    while index < len(word_list) - 2:
        chains[tuple(word_list[index:index + 2])] = word_list[index + 2]
        index += 1

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    first_text = choice(chains.keys())
    text += "{} {} {} ".format(first_text[0], first_text[1], chains.get(first_text))
    next_key = (first_text[1], chains.get(first_text))

    # print first_text, "-----1st"
    # print next_key, "-----next"
    # print chains.get(first_text), "-----value of tuple"
    # print text, "-----text"
    # print

    while next_key in chains:
        try:
            text += "{} ".format(chains.get(next_key))
            next_key = (next_key[1], chains.get(next_key))
            # print next_key, "-----next key"
            # print text
        except KeyError:
            break
    return text


# Open the file and turn it into one long string
input_text = open_and_read_file(file_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
