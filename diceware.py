#! /usr/bin/python

from random import SystemRandom
from argparse import ArgumentParser

# allow manually setting pass phrase length
parser = ArgumentParser(description='Generate Diceware passphrases')
parser.add_argument(
    '--length',
    help='how many words in the phrase',
    default=4
)
args = parser.parse_args()


def generate_word_dict():
    wordlist = open('wordlist.txt', 'r')
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


# rolls = [generate_dice_roll() for i in xrange(0, args.length)]

def main(total_words):
    words = generate_word_dict()
    
    phrase = [words[generate_dice_roll()] for i in xrange(0, total_words)]
    print(' '.join(phrase))


main(args.length)
