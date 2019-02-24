import csv

with open('KakaoTalk_Chat_CIVAR.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        if 'invited' in row[2]:
            print(row[2])

# macOS 카카오톡에서 출력할 수 있는 대화 로그 csv 파일을 통해서 가입 멤버 순서를 구함
