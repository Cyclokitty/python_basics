# not reg exp. Just going thru a chunk of text and 
# testing if the chuck is 12 char long, if certain chunks
# are digits, if a couple of chunks are just a hyphen
# This only tests for a phone number that is one particular
# format 123-456-7890. If a phone number used other punctuation
# or just a string of numbers, the test fails.

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

isTrue = isPhoneNumber('415-555-4242')
print(f'{isTrue}')
isThisTrue = isPhoneNumber('Taco Hut')
print(f'{isThisTrue}')
