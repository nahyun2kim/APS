def solution(info, query):
    answer = []
    n = len(info)
    condition = [['cpp','java','python','-'],['backend','frontend','-'],['junior','senior','-'],['chicken','pizza','-']]
    info_dict = {}
    for i in condition[0]:
        for j in condition[1]:
            for k in condition[2]:
                for r in condition[3]:
                    info_dict[i+j+k+r] = []
    
    for ii in info:
        infor = list(ii.split())
        for i in [infor[0],'-']:
            for j in [infor[1],'-']:
                for k in [infor[2],'-']:
                    for r in [infor[3],'-']:
                        info_dict[i+j+k+r].append(int(infor[4]))
                        
    for key in info_dict.keys():
        info_dict[key].sort()
        
    for q in query:
        q = q.replace(" and "," ")
        q_list = list(q.split())
        key = "".join(q_list[:4])
        cnt = info_dict[key]
        length = len(cnt)
        st = 0
        ed = length-1
        while st <= ed:
            mid = (st + ed)//2
            if int(q_list[4]) <= cnt[mid]:
                ed = mid - 1
            else:
                st = mid + 1
        answer.append(length - st)
    return answer