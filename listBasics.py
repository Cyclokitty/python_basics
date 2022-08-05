cats = ['Princess', 'Tiger', 'Bootsie', 'Lucky', 'Belle', 'Freddie', 'Daisy', 'Lucy', 'Simon']

def addCat(name):
    #for cat in cats:
    if name not in cats:
        cats.append(name)

print(cats)
addCat('Tigger')
print(cats)
addCat('Freddie')
print(cats)
addCat('Rialto the Meowto')
print(cats)
cats.sort()
print(cats)