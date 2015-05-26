#! /usr/bin/python

import requests
from bs4 import BeautifulSoup
from argparse import ArgumentParser

parser = ArgumentParser(description='Generate Diceware passphrases')
parser.add_argument(
    '--length',
    help='how many words in the phrase',
    default=6
)
args = parser.parse_args()

wordlist = open('wordlist.txt', 'r')
words = {}

for entry in wordlist:
    num, word = entry.split('\t')
    words[num] = word[:-1]

print 'Generating Diceware passphrase...\n'
params = 'sets=%s&num=5&min=1&max=6&order=random&format=html&rnd=new' % args.length
page = requests.get('https://www.random.org/integer-sets/?%s' % params)

soup = BeautifulSoup(page.content)
data = soup.find('ul', class_='data').find_all('li')

phrase = []
for el in data:
    key = ''.join(el.get_text().split(' '))
    phrase.append(words[key])

print ' '.join(phrase)
