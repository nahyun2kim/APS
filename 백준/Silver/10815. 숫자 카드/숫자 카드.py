def binary_search(target, data):
  st = 0
  ed = len(data) - 1

  while st <= ed:
    mid = (st + ed) // 2
    if data[mid] == target:
      return '1'
    elif data[mid] > target:
      ed = mid - 1
    else:
      st = mid + 1
  return '0'

N = int(input())
numbers = sorted(list(map(int, input().split(' '))))
M = int(input())
number_cards = list(map(int, input().split(' ')))

answer = []

for card in number_cards:
  answer.append(binary_search(card, numbers))

print(' '.join(answer))