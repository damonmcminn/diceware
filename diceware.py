#! /usr/bin/python

from random import SystemRandom
from argparse import ArgumentParser
import os

# allow manually setting pass phrase length
parser = ArgumentParser(description='Generate Diceware passphrases')
parser.add_argument(
    '--length',
    type=int,
    help='how many words in the phrase',
    default=4
)
args = parser.parse_args()


def generate_word_dict(path):
    wordlist = open('{0}/wordlist.txt'.format(path), 'r')
    words = {}

    for entry in wordlist:
        num, word = entry.split('\t')
        words[int(num)] = word[:-1]

    return words

def roll(multiplier=1):
    r = SystemRandom()
    return r.randint(1, 6)*multiplier

def generate_dice_roll():
    nums = [1, 10, 100, 1000, 10000]
    return sum([roll(i) for i in nums])

def generate_phrase(words, length):
    word_list = [words[generate_dice_roll()] for i in range(0, length)]
    return ' '.join(word_list)

def main(total_words):
    path = os.path.dirname(os.path.abspath(__file__))
    words = generate_word_dict(path)

    # give a choice of seven phrases
    for i in range(0, 7):
        print(generate_phrase(words, total_words))


# APPLICATION START
main(args.length)
