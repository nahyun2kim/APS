def solution(orders, course):
    answer = []
    alpha = ["0"]
    for order in orders:
        for i in range(len(order)):
            alpha.append(order[i])
    alpha = list(set(alpha))
    alpha.sort()
    
    def dfs(idx, n, cnt, crs):
        if idx == n:
            if cnt in ans.keys():
                ans[cnt].append(crs[1:])
            else:
                ans[cnt] = [crs[1:]]
            return
        
        for i in range(alpha.index(crs[-1])+1, len(alpha)):
            tmp_string = crs + alpha[i]
            if not visit[i]:
                tmp_cnt = count(tmp_string[1:])
                if not tmp_cnt == 0:
                    visit[i] = True
                    dfs(idx+1, n, tmp_cnt, tmp_string)
                    visit[i] = False
    
    def count(string):
        count = 0
        for order in orders:
            flag = True
            for i in range(len(string)):
                if not string[i] in order:
                    flag = False
            if flag:
                count += 1
        if count > 1:
            return count
        return 0
    
    for n in course:
        ans = {}
        visit = [False]*(len(alpha)+1)
        dfs(0, n, 0,'0')
        if not len(ans.keys()) == 0:
            max_key = max(ans.keys())
            for key in ans[max_key]:
                answer.append(key)
    
    answer.sort()
    return answer