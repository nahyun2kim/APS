def solution(book_time):
    answer = 0
    time = [0]*(24*60+10)
    for st, ed in book_time:
        sth, sts = map(int, st.split(':'))
        edh, eds = map(int, ed.split(':'))
        time[sth*60 + sts] += 1
        time[edh*60 + eds + 10] -= 1
    room = 0
    for t in time:
        room += t
        answer = max(answer, room)
    return answer