'''
Goals:
1 - Take a simple message and encrypt it using a variety of encryption methods
    Reverse Cipher
    Ceasar + Reverse Cipher
    Transcription Cipher
    Substitution
    Caesar Shift
2 - Implement PyCrypto, M2Crypto, PyOpenSSL to simplify this cryptography
    use this to encrypt entire files
'''

import math, pyperclip

def ceaser(text, s):
    #text = input text to be encrypted
    #s = the shift value in characters i.e. a to c is (s = 2)
    result = ""
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s-97) % 26 + 97)
    return result

def hack_ceaser(message):
    #message = the encrypted message
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    #attempt to crack the cypher for each letter in the alphabet
    for key in range(len(letters)):
        translated = ''
        for symbol in message:
            if symbol in letters:
                num = letters.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(letters)
                translated = translated + letters[num]
            else:
                translated = translated + symbol
        print('Hacking key #%s: %s' % (key, translated))


# Transcritpion Cipher Test
def split_len(seq, length):
    return [seq[i:i + length] for i in range(0, len(seq), length)]

def encode(key, plaintext):
    order = {
        int(val): num for num, val in enumerate(key)
    }
    ciphertext = ''
    print(order)

    for i in sorted(order.keys()):
        print(i)
        for part in split_len(plaintext, len(key)):
            print("--" + part + "--")
            try:ciphertext += part[order[i]]
            except IndexError:
                continue
    return ciphertext

def encryptMessage(key, message):
    ciphertext = [''] * key

    for col in range(key):
        position = col
        while position < len(message):
            ciphertext[col] += message[position]
            position += key
    return ''.join(ciphertext)

def decryptMessage(key, message):
    numOfColumns = math.ceil(len(message) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    plainttext = [''] * numOfColumns
    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1
            return ''.join(plaintext)

myMessage = 'Transposition Cipher'
myKey = 10
ciphertext = encryptMessage(myKey, myMessage)

print("Cipher Test is:")
print(ciphertext + '|')
pyperclip.copy(ciphertext)

decryptMessage(10, ciphertext)

'''    
print(encode('15243', 'The Disk is in the Open'))


## - Ceaser Cipher Test
text = "Social Engineering"
s = 4

print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Cipher: " + ceaser(text,s))

hack_ceaser(ceaser(text,s))
'''