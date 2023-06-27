def cal_time(st, ed):
    stt, sts = map(int, st.split(':'))
    edt, eds = map(int, ed.split(':'))
    return edt*60 + eds - stt*60 -sts

def solution(fees, records):
    parking = {}
    for record in records:
        time, num, io = record.split()
        if num in parking:
            if io == 'IN':
                parking[num][0] = time
                parking[num][2] = 1
            else:
                parking[num][1] += cal_time(parking[num][0], time)
                parking[num][2] = 0
        else:
            parking[num] = [time, 0, 1]
    for key in parking.keys():
        if parking[key][2]:
            parking[key][1] += cal_time(parking[key][0], '23:59')
    answer = []
    for num in sorted(parking.keys()):
        if parking[num][1] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + (parking[num][1] - fees[0] + fees[2] - 1)//fees[2]*fees[3])
    return answer