"""새로운 디미워드 단어장 오브젝트를 생성, './books' 폴더에 저장"""

import json
from PyInquirer import prompt


def new():
    """사용자에게 단어를 입력받아 단어장 오브젝트를 생성, 저장"""

    wordbook = prompt([
        {
            'type': 'input',
            'name': 'name',
            'message': '단어장 제목을 입력하세요: ',
            'filter': lambda val: val.replace(' ', '-')
        },
        {
            'type': 'input',
            'name': 'intro',
            'message': '단어장 소개를 입력하세요: ',
        }
    ])

    words = []
    while True:
        word = prompt([
            {
                'type': 'input',
                'name': 'en',
                'message': '영단어를 입력하세요: '
            },
            {
                'type': 'input',
                'name': 'ko',
                'message': '한글 뜻을 입력하세요(,로 구별): ',
                'filter': lambda val: [i.strip() for i in val.split(',')]
            }
        ])
        print(word)
        words.append(word)
        if input('enter to continue...'):
            break

    filename = './books/' + wordbook['name'] + '.json'
    # print(f'output wordbook object to file {filename}')
    try:
        with open(filename, 'w') as file:
            json.dump({
                'name': wordbook['name'],
                'intro': wordbook['intro'],
                'words': words
            }, file, indent=4, ensure_ascii=False)
            file.write('\n')
        print('success')
    except BaseException:
        print('error')
        print(json.dumps({
            'name': wordbook['name'],
            'intro': wordbook['intro'],
            'words': words
        }, indent=4, ensure_ascii=False))
