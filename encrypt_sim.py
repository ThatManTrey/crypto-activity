#Simple cryptography example
#Created by Trey Phillips
#8 Oct 2019

#Online Python IDE: https://repl.it/repls/ImprobableHumiliatingPi
#Source of inspiration: http://practicalcryptography.com/ciphers/simple-substitution-cipher/
#Good resource for the youngsters: https://www.w3schools.com/python/default.asp

#my sister's notes:
#*Incorporate "throwing things around" :)
#	- maybe throw a ball around so that students can help with creating cipher
#*Once we have the program written, give students free reign to
#	give each other encrypted messages to decrypt
#	- she suggested providing plastic eggs to put the messages
#		in so that students can give each other eggs
#		rather than just pieces of paper
#*Keep explanations minimal
#	- maybe we could start with a more hands on description of
#		cryptography before we go into coding
#	- after main coding demo and a few walkthroughs we can go
#		into detail about the code

#global variables to keep it simple
alphabet = " abcdefghijklmnopxrstuvwxyz" #language alphabet
cipher = " zyxwvutsrqponmlkjihgfedcba"   #language cipher

#encryption function - takes in phrase, encrypts
#variables are named to keep concept grounded
#dependent on globals
def encrypt(phrase):
  newstring = str()
  for character in range(len(phrase)):
    for letter in range(len(alphabet)):
      if alphabet[letter] == phrase[character]:
        newstring = newstring + cipher[letter]
  return newstring

#decryption function - takes in phrase, decrypts
#variables are named to keep concept grounded
#dependent on globals
def decrypt(phrase):
  newstring = str()
  for character in range(len(phrase)):
    for letter in range(len(cipher)):
      if cipher[letter] == phrase[character]:
        newstring = newstring+ alphabet[letter]
  return newstring

myword = input("Enter your string!")    #takes user input

myword = encrypt(myword)    #shows encryption
print(myword)

myword = decrypt(myword)    #shows decryption
print(myword)
