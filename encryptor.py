'''
Designed to be a catch-all module for common encryption types
'''

import math

def reverse(message):
    '''returns a message in reverse order'''
    return message[::-1]


def caesar(message, key):
    '''returns an encrypted message by shifting the characters according to the key argument'''
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
    translated = ''
    for char in message:
    # note: only characters in the variable "symbols" will be encrypted / decrypted
    # set each character == a number, given it's position in the symbols list
        if char in symbols:
            char_index = symbols.find(char)
            translated_index = char_index + key
            # handle wrap around
            if translated_index >= len(symbols):
                translated_index -= len(symbols)
            elif translated_index < 0:
                translated_index += len(symbols)

            translated += symbols[translated_index]
        else:
            # append the char if it is not in the list of 'symbols'
            translated += char
    return translated


def transposition(message, key):
    '''returns an encrypted message by creating a row of columns(= to the key value) and inputing the message, then rewriting it top-down, left to right'''
    num_of_chars = len(message)
    
    cipher = [[]]
    i = 0
    row = 0
    for char in message:
        if i%key == 0 and i != 0:
            cipher.append([])
            row += 1
        cipher[row].append(char)
        i += 1        

    while len(cipher[row]) != key:
        cipher[row].append("")

    print(cipher)

    translated_cipher = ""
    for columns in range(len(cipher[0])):
        for rows in range(len(cipher)):
            translated_cipher += cipher[rows][columns]

    return translated_cipher


if __name__ == "__main__":
    message = "common sense is not so common."
    key = 8

    print(transposition(message, key))