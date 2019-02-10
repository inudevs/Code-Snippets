"""디미워드 단어장 오브젝트를 로딩"""

import json


def load(name):
    """name의 단어장 오브젝트 파일을 읽어 그 내용을 딕셔너리로 반환"""
    with open(f'./books/{name}.json') as file:
        wordbook = json.load(file)
    return wordbook
