print('''
          *       
         ***      
        *****     
       *******  
  Birthday Database  
'''
)

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter name of person: (blank to quit)')
    name = input().strip()
    if name == '':
        for k, v in birthdays.items():
            print(f'Name: {k}, Birthday: {v}')
        print('''
                    *       
                   ***      
                  *****     
                 *******  
            Birthday Database  
            '''
        )
        print('Goodbye.')
        break

    if name in birthdays:
        print(f'Birthday of {name} is {birthdays[name]} ')
    else:
        print('That name is not listed.')
        print(f'What is {name}\'s birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthdays database is updated.')