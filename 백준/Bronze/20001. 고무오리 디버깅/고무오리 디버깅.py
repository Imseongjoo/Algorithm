start = input()
cnt = 0
if start == '고무오리 디버깅 시작':
    while True:
        Q = input()
        if Q == '문제':
            cnt += 1
        elif Q == '고무오리':
            if cnt > 0:
                cnt -= 1
            else:
                cnt += 2
        elif Q == '고무오리 디버깅 끝':
            break
    if cnt <= 0:
        print('고무오리야 사랑해')
    else:
        print('힝구')