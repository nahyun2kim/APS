import re

def solution(new_id):
    #1. 대문자 -> 소문자
    new_id = new_id.lower()
    #2. 알파벳 소문자, 숫자, -, _, . 빼고 제거
    new_id = re.sub("[^a-z0-9\-_.]","",new_id)
    #3. .두개이상 반복 시 .하나로 변경
    new_id = re.sub("\.+",".",new_id)
    #4. 마침표가 처음이나 끝이라면 제거
    new_id = re.sub("^\.|\.$","",new_id)
    #5. 빈 문자열이라면, 'a'를 대입
    if len(new_id) == 0: new_id = 'a'
    #6. 길이가 16자 이상이라면 15까지, 끝이 .라면 제거
    if len(new_id) > 15: new_id = new_id[:15]
    new_id = re.sub("\.$","",new_id)
    #7. 길이가 2자 이하라면, 반복해서 붙여 3자 이상이 되도록
    if len(new_id)<3:
        while len(new_id)<3:
            new_id += new_id[-1]
    return new_id