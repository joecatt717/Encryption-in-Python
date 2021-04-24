#Caesar Cipher Hacker - using brute force method

import os
import sys

def hack():

    #message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
    message = input("-> ")
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    # Loop through every possible key:
    for key in range(len(symbols)):
        translated = ''

        for char in message:
            if char in symbols:
                char_index = symbols.find(char)
                translated_index = char_index - key

                if translated_index < 0:
                    translated_index += len(symbols)

                translated += symbols[translated_index]
            
            else:
                translated += char

        with open("dictionary.txt", "r") as dictionary:
            for line in dictionary:
                stripped_line = line.strip()
                if stripped_line in translated:
                    print('Key #%s: %s' % (key, translated))
                
for i in range(0,10):
    hack()