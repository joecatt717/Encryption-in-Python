# Transposition Cipher Encryp/Decrypt Files

import time, os, sys, transpositionDecrypt, transpositionEncrypt

def main():
    inputFilename = 'frankenstein.txt'
    # BE CAREFUL! If a file with the outputFilename name already exists...
    # this program will overwrite that file:
    outputFilename = 'frankenstein.encrypted.txt'
    my_key = 10
    my_mode = 'encrypt' # set to encrypt or decrypt

    # if the input file does not exist the program terminates early:
    if not os.path.exists(inputFilename):
        print("The file: %s does not exist...")
        sys.exit()
    else:
        print('Fetching your file...')

    #if the output file already exists, give the user a chance to qui:
    if os.path.exists(outputFilename):
        print("The output file already exists, and continueing will overwrite your file")
        choice = input("Would you like to continue? Y/N >>>")
        choice = choice.lower()
        if not choice.startswith('y'):
            sys.exit()

    # read in the message from the input file:
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    # Measure how long the encryption/decryption takes:
    start_time = time.time()
    if my_mode == 'encrypt':
        translated = transpositionEncrypt.encrypt_message(my_key, content)
    else:
        translated = transpositionDecrypt.decrypt_message(my_key, content)
    total_time = round(time.time() - start_time, 2)
    print('%sion time: %s seconds' % (my_mode.title(), total_time))

    # Write out the translated message to the output file:
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

if __name__ == '__main__':
    main()