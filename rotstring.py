#!/usr/bin/python3

from itertools import product
from string import ascii_lowercase as alphabet

    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	for eachLetter in realText:
		if eachLetter in ' ':
		    outText.append(' ')
       		elif eachLetter in uppercase:
            index = uppercase.index(eachLetter)
			crypting = (index + step) % 26
			cryptText.append(crypting)
			newLetter = uppercase[crypting]
			outText.append(newLetter)
		elif eachLetter in lowercase:
			index = lowercase.index(eachLetter)
			crypting = (index + step) % 26
			cryptText.append(crypting)
			newLetter = lowercase[crypting]
			outText.append(newLetter)
    return ''.join(outText)

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
def caesar_brutusforce(realText):
	## cutting edge bruteforce for caesar ciphers. I'm just taking a stab at this.
	for i in range(1, 26):
		result = caesar_decrypt(realText, i)
		temp = str(i) + ": " + result +"\n"
		print(temp)
    

brutusforce = caesar_brutusforce('qPbqr EBG Nhgb')

