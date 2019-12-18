from itertools import product
from string import ascii_lowercase as alphabet
import string
import enchant

offset = 4
alphabet = "abcdefghijklmnopqrstuvwxyz"

d = enchant.Dict("nl_NL")

def aivdtest():
	for combo in product(alphabet, repeat=3):
		original = ''.join(combo)
		new = caesar(original, offset)
		if d.check(new) and d.check(original):
			print(original + " with rot4 = " + new)

def caesar(plaintext, offset):
	return plaintext.translate(str.maketrans(alphabet, alphabet[offset:] + alphabet[:offset]))

       
aivdtest()


