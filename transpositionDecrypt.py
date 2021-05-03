# Transposition Cipher Decryption

import math, pyperclip

def main():
    my_message = 'Cenoonommstmme oo snnio. s s c'
    my_key = 8

    plaintext = decrypt_message(my_key, my_message)

    # Print with a |(called "pipe" character) after it in case
    # there are spaces at the end of teh decrypted message:
    print(plaintext + '|')

    pyperclip.copy(plaintext)


def decrypt_message(key, message):
    # Find the number of Columns in our grid
    # Find the number of Rows in our grid
    columns = math.ceil(len(message)/key)
    rows = key
    
    # Find the number of shaded boxes in our grid
    num_of_shaded_boxes = (columns*rows)-len(message)

    # each string in plaintext is equal to an individual column
    plaintext = ['']*columns

    # The column and row variables point to where each character will go in plaintext
    # initiate rows and columns to zero here...
    col = 0
    row = 0

    # Loop through each character in "message"
    # one character, then shift column, then next character, then shift column...
    for char in range(len(message)):
        plaintext[col] += message[char]
        col += 1

    # if we are out of columns or at a shaded box, go back to the first column of the next row
        if (col == columns) or (col == columns - 1 and row >= rows - num_of_shaded_boxes):
            col = 0
            row += 1
    #join the columns together, and return the function 
    return ''.join(plaintext)

if __name__ == '__main__':
    main()