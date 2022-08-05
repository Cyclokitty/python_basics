# display the inventory of a player in the game Knights Of Dread

playerInventory = {
    'arrow': 12,
    'gold coin': 42,
    'rope': 1,
    'torch': 6,
    'dagger': 1
}

def listInventory(list):
    count = 0
    print('Inventory:')
    for k, v in playerInventory.items():
        print(f'{v} {k}')
        count += v
    print(f'Total number of items: {count}')

listInventory(playerInventory)

# Once our intrepid player has killed the dragon, our player can add the dragon's treasure to their own inventory. Pillaging is good!

dragonInventory = ['gold coin', 'arrow', 'rope', 'ruby','magic hat', 'arrow', 'gold coin']

def addBooty(oldStuff, newStuff):
    count = 0
    print('Inventory: ')

    for item in newStuff:
        if item in oldStuff:
            oldStuff[item] += 1
        else:
            oldStuff[item] = 1

    for k, v in oldStuff.items():
        count += v
        print(f'{k} {v}')

    print(f'Total number of items: {count}')

addBooty(playerInventory, dragonInventory)