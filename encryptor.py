'''
Designed to be a catch-all module for common encryption types
'''

class Encrypt:
    
    def __init__(self):
        #self.message = message
        pass

    @staticmethod
    def reverse(message):
        '''returns a message in reverse order'''
        return message[::-1]


    @staticmethod
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