# /d finds a digit
# - finds the hyphen

import re

def isPhoneNumber(text):
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phoneNumRegex.search(text)
    #print(mo)
    if mo == None:
        print(f'That\'s not a phone number: {text}')
    else:
        print(f'That\'s a phone number: {text}')
    
        


isPhoneNumber('415-555-4515')
isPhoneNumber('Laura is an awesome coder.')