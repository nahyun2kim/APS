def solution(enroll, referral, seller, amount):
    profit = {i:0 for i in enroll}
    refer = {i:'' for i in enroll}
    for e, r in zip(enroll, referral):
        if not r == '-':
            refer[e] = r
    for s, a in zip(seller, amount):
        st = [(s, a*100)]
        while st:
            name, price = st.pop()
            if refer[name] and price >= 10:
                profit[name] += price - price//10
                st.append((refer[name], price//10))
            elif not refer[name]:
                profit[name] += price - price//10
            else:
                profit[name] += price
    return [profit[i] for i in enroll]