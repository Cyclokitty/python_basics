# use the regex search with pipe, and brackets

import re

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo1 = batRegex.search('Batmobile has lost its wheel')
print(mo1.group())
print(mo1.group(1))

mo2 = batRegex.search('The Batcopter is rad.')
print(mo2.group())
print(mo2.group(1))

# regex with optional matching with a question mark
# (wo)? mearns wo is the optional part. If there, it'll retrieve it
# Match zero or one of the group preceding this question mark

moreRegex = re.compile(r'Bat(wo)?man')
mo3 = moreRegex.search('The Adventures of Batman')
print(mo3.group())

mo4 = moreRegex.search('The Adventures of Batwoman')
print(mo4.group())

# matching zero or with the star (asterix)
#  the group that precedes the star can occur any number of times in the text

starRegex = re.compile(r'Bat(wo)*man')
mo5 = starRegex.search('The Adventures of Batwoman')
mo6 = starRegex.search('The Adventures of Batman')
print(mo5.group())
print(mo6.group())

anyWo = re.compile(r'(wo)*')
mo7 = anyWo.search('wowowowowowbowowowow')
print(mo7.group())