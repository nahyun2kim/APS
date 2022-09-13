test = input().split("-")  

answer = 0   
if test[0] != "":  
    answer += sum(map(int,test[0].split("+")))

for i in range(1,len(test)):   
    answer -= sum(map(int,test[i].split("+")))

print(answer)