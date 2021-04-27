import re
def solution(new_id):
    answer = ''
    #print("원본: " + new_id)

    #1.대문자 소문자로 변경
    answer = new_id.lower()
    # print("1차:" + answer)

    #2. 특수문자 제거
    #-_.
    characters = '~!@#$%^&*()=+[{]}:?,<>/'
    for x in range(len(characters)):
        answer = answer.replace(characters[x],"")
    # print("2차: "+answer)

    #3. 마침표가 2번 이상 연속되면 마침표 하나로 치환
    answer = re.sub('(([.])\\2{1,})', '.', answer)
    # print("3차:" + answer)
    #4. 마침표가 처음, 끝에 위치 시 제거

    if answer[0] == '.':
        answer = answer [1:]

    if len(answer)>= 2 and answer[-1] == '.':
        answer = answer[:-1]

    #print('4단계: '+answer)

    #5. 빈 문자열일 경우 a를 대입
    if len(answer) == 0 :
        answer = 'a'
                
    #6. 16자 이상일 경우 15자까지만 출력
    if len(answer) > 15 :
        answer = answer[:15]

        if answer[-1] == '.':
            answer = answer[:-1]
    #print("6단계: " + answer)
    #7.
    if len(answer) <= 2:
        for x in range(3):
            if len(answer) >2:
                break
            answer = answer + answer[-1]

    print(answer)
    return answer


solution('...!@BAT#*..y.abcdefghijklm.')
solution('z-+.^.')
solution('=.=')
solution('123_.def')
solution('abcdefghijklmn.p')

