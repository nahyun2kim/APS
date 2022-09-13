N = int(input())
left = {}
right = {}
for _ in range(N):
    root, left_sub, right_sub = map(str, input().split())
    if not left_sub == ".":
        left[root] = left_sub
    if not right_sub == ".":
        right[root] = right_sub

pre_ans = []
in_ans = []
post_ans = []

def pre_order(key):
    pre_ans.append(key)
    if key in left:
        pre_order(left[key])
    if key in right:
        pre_order(right[key])
        
def in_order(key):
    if key in left:
        in_order(left[key])
    in_ans.append(key)
    if key in right:
        in_order(right[key])
        
def post_order(key):
    if key in left:
        post_order(left[key])
    if key in right:
        post_order(right[key])
    post_ans.append(key)
        
pre_order("A")
in_order("A")
post_order("A")

print("".join(pre_ans))
print("".join(in_ans))
print("".join(post_ans))