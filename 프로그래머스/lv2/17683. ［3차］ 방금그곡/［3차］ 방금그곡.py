def str2time(st, ed):
    sth, sts = map(int, st.split(':'))
    edh, eds = map(int, ed.split(':'))
    res = edh*60 + eds - sth*60 - sts
    return res if res >= 0 else res + 1440

def rep(string):
    string = string.replace('C#', 'H')
    string = string.replace('D#', 'I')
    string = string.replace('F#', 'J')
    string = string.replace('G#', 'K')
    string = string.replace('A#', 'L')
    return string

def solution(m, musicinfos):
    answer = '(None)'
    long_time = 0
    m = rep(m)
    for info in musicinfos:
        st, ed, title, music = info.split(',')
        time = str2time(st, ed)
        music = rep(music)
        div, mod = divmod(time, len(music))
        all_music = music * div + music[:mod]
        if m in all_music and long_time < time:
            answer = title
            long_time = time
    return answer