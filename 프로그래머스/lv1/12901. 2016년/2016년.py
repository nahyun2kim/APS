def solution(a, b):
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    first = 5
    result = (sum(month[:a]) + b - 1) % 7 + first
    return day[result if result < 7 else result - 7]