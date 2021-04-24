'''
reverse cipher
'''

text = input("Type your message here: -> ")

def reverse(text):
    return text[::-1]

print(reverse(text))