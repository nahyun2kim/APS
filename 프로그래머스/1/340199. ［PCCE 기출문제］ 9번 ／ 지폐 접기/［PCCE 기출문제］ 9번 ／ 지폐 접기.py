def solution(wallet, bill):
    answer = 0
    wallet.sort()
    bill.sort()
    while True:
        if wallet[0] < bill[0] or wallet[1] < bill[1]:
            bill[1] //= 2
            bill.sort()
            answer += 1
        else:
            break
    return answer