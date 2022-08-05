# print items from a list with each item separated by a comma
# and a space, except the last item with is also separtated by the word 'and'.

def commaCode(list):
    for item in list:
        if item != list[-1]:
            print(f'{item}, ')
        else:
            print(f'and {item}')


def combineList(list):
    line = ''
    for item in list:
        if item != list[-1]:
            line += item + ', '
        else:
            line += 'and ' + item
    print(line)

#commaCode(['dot', 'dash', 'dig', 'dang', 'dug', 'done'])
combineList(['dot', 'dash', 'dig', 'dang', 'dug', 'done'])