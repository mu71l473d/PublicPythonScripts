#!/usr/bin/python3

from itertools import product
from string import ascii_lowercase as alphabet


def caesar_encrypt(realText, offset):
	return realText.translate(str.maketrans(alphabet, alphabet[offset:] + alphabet[:offset]))

def caesar_decrypt(cipherText, offset):
	outText = []
	decryptText = []	
	
	for letter in alphabet:
		if letter in ' ':
			outText.append(' ')
		else:
			index = alphabet.index(letter)
			decrypting = (cipherText - offset) % 26
			decryptText.append(decrypting)
			newLetter = lowercase[decrypting]
			outText.append(newLetter)
	return ''.join(outText)			


def caesar_brutusforce(cipherText):

    # # cutting edge bruteforce for caesar ciphers. I'm just taking a stab at this.

    for i in range(1, 26):
        result = caesar_decrypt(cipherText, i)
        temp = str(i) + ': ' + result + '\n'
        print(temp)


print(caesar_decrypt("vet", 4))
