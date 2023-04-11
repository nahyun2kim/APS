def solution(phone_book):
    check = {}
    for p in phone_book:
        for i in range(len(p)):
            check[p[:i]] = 1
    for p in phone_book:
        if p in check.keys():
            return False
    return True