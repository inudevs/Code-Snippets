"""디미워드 단어장 오브젝트를 로드, 디미워드 서버에 동기화"""

import json
import requests


def login(user):
    """로그인하고 토큰을 반환"""

    req = requests.post('https://dimiwords.tk:5000/api/auth/login', json=user)
    return json.loads(req.text)['token']


def send(token):
    """토큰의 계정 정보로 서버에 단어 생성"""

    filename = f"./books/{input('BOOK: ')}.json"

    with open(filename, 'r') as file:
        book = json.loads(file.read())
        print(book)

    for word in book['words']:
        print(word)
        req = requests.post('https://dimiwords.tk:5000/api/create/word', json={
            'token': token,
            'en': word['en'],
            'ko': word['ko']
        })
        print(req.text)
