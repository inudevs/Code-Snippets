import getpass
import dimiwords
from PyInquirer import prompt

for i in range(4):
    if i == 3:
        print('bye')
        exit()
    user = {
        'email': input('EMAIL: '),
        'password': getpass.getpass('PASS: ')
    }
    if '@' not in user['email']:
        print('wrong email format')
        continue
    try:
        token = dimiwords.send.login(user)
        break
    except BaseException:
        print('login error')
        continue

while True:
    answer = prompt([{
        'type': 'list',
        'name': 'menu',
        'message': 'Dimiwords CLI',
        'choices': [
            'New Wordbook',
            'Load Wordbook Object',
            'Sync words to dimiwords.tk',
            'exit'
        ]
    }])
    if answer['menu'] == 'New Wordbook':
        dimiwords.new.new()
    elif answer['menu'] == 'Load Wordbook Object':
        name = input('단어장 파일 이름: ').strip().replace(' ', '-')
        dimiwords.load.load(name)
    elif answer['menu'] == 'Sync words to dimiwords.tk':
        dimiwords.send.send(token)
    elif answer['menu'] == 'exit':
        exit()
