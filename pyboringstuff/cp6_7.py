import re


# Cahpter 6

spam = "That is Alice's cat."
print(spam)

spam = 'Hello, world!'
print(spam[1])

name = 'Al'
age = 4000
print(f'My name is {name}. Next year I will be {age + 1}.')

print('----------------')

# Chapter 7

def isPhoneNumber(text):
    if len(text) != 12:
        return False

    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    
    return True

text = '415-555-4242'
print(isPhoneNumber(text))
text = '090-1111-2222'
print(isPhoneNumber(text))

print('----------------')

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo)
print(mo.group())


print('----------------')

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')

print(mo)
print(mo.group(2))
