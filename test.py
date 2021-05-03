# Transposition Cipher Test

import random, sys, transpositionDecrypt, transpositionEncrypt

def main():
    random.seed(42) # Set the random "seed" to a static value

    for i in range(20): # Run 20 tests
        # Generate random messages to test.

        # The message will have a random length:
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4,20)

        # Convert the message string to a list to shuffle it:
        message = list(message)
        random.shuffle(message)
        message = ''.join(message) # convert the shuffled list back into a string

        print('Test #%s: "%s..."' %(i + 1, message[:50]))

        # Check all possible keys for each message:
        for key in range(1, int(len(message)/2)):
            encrypted = transpositionEncrypt.encrypt_message(key, message)
            decrypted = transpositionDecrypt.decrypt_message(key, encrypted)

            #if the decryption doesn't match the original message, display
            # an erro rmessage and quit
            if message != decrypted:
                print('Mismatch with key %s and message %s.' % (key, message))
                print('Decrypted as: ' + decrypted)
                sys.exit()

    print('Transposition cipher test passed.')

# If transpositionTest.py is run (instead of imported as a module) call
# the main() function:
if __name__ == '__main__':
    main()