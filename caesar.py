'''
caesar cipher
encrypt and decrypt messages by shifting the symbol value by a key value
'''

import pyperclip

def setup():
    # The string to be encrypted/decrypted:
    message = input("Type your message here: -> ")

    # The encryption/decryption key:
    while True:
        try:
            key = int(input("Enter your key here: -> "))
            break
        except ValueError:
            print("Key must be an integer. Try again...")

    # Set the mode to either encryption or decryption
    while True:
        try:
            mode = input("encrypt or decrypt: -> ")
            if mode.startswith('e'):
                mode = "encrypt"
                break
            elif mode.startswith('d'):
                mode = "decrypt"
                break
        except:
            print("Please type 'encrypt' or 'decrypt'.")

    while True:
        try:
            print("Please input which set of symbols you would like to use.")
            print("1: l-alph, 2: u-l-alph, 3: u-l-alph-nums, 4: u-l-alph-nums-punc")
            symbols = int(input("-> "))
            if symbols in range(1,5):
                break
            else:
                print('Out of range. Try again')
        except ValueError:
            print("Please input a number between 1 and 4")

    return message, key, mode, symbols


def cipher(message, key, mode, symbols):

    # set up the variable to be returned at the end of the function
    translated = ''

    # Set the symbols for the cipher based on the input
    # All sets include "space" at the end of their list of characters
    if symbols == 1:
        symbols = "abcdefghijklmnopqrstuvwxyz "
    elif symbols == 2:
        symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    elif symbols == 3:
        symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
    elif symbols == 4:
        symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?.', "

    for char in message:
        # note: only characters in the variable "symbols" will be encrypted / decrypted
        # set each character == a number, given it's position in the symbols list
        if char in symbols:
            char_index = symbols.find(char)

            # perform encryption / decryption:
            if mode == 'encrypt':
                translated_index = char_index + key
            elif mode == 'decrypt':
                translated_index = char_index - key

            # handle the wrap-around (i.e. translate 'z' + 5 should == 'e')
            if translated_index >= len(symbols):
                translated_index -= len(symbols)
            elif translated_index < 0:
                translated_index += len(symbols)

            translated = translated + symbols[translated_index]

        else:
            # append the char if it is not in the list of 'symbols'
            translated += char

    return translated

message, key, mode, symbols = setup()

print(cipher(message, key, mode, symbols))