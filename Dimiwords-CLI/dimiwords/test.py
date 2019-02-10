"""단어 테스트"""

from PyInquirer import prompt, Validator, ValidationError


class NumberValidator(Validator):
    """prompt를 통해 받은 입력이 숫자인지 검증"""

    def validate(self, document, ):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message=str(document),
                cursor_position=len(document.text))


def test():
    """단어 테스트"""

    question = prompt({
        'type': 'input',
        'name': 'answer',
        'message': '적당한',
        # 'choices': ['adequate', 'delicate', 'fundamental'],
        'validate': NumberValidator()
    })
    print(question['answer'])
