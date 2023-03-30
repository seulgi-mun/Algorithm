def solution(id_pw, db):
    answer = ''

    k, v = id_pw[0], id_pw[1]

    for id, pw in db:
        if k == id:
            if v == pw:
                answer = 'login'
                break
            else:
                answer = "wrong pw"
                break
        else:
            answer = 'fail'
    return answer