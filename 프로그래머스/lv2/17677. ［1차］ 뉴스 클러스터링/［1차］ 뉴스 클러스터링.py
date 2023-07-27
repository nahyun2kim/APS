def str2arr(string):
    string = string.lower()
    arr = [string[i:i+2] for i in range(len(string)-1) if string[i:i+2].isalpha()]
    return arr

def solution(str1, str2):
    arr1 = str2arr(str1)
    arr2 = str2arr(str2)
    
    if len(arr1) == 0 and len(arr2) == 0:
        return 65536
    if len(arr1) == 0 or len(arr2) == 0:
        return 0
    
    a_temp = arr1[:]
    a_result = arr1[:]
    result = []
    
    for i in arr2:
        if i not in a_temp:
                a_result.append(i)
        else:
            a_temp.remove(i)
            
        if i in arr1:
            arr1.remove(i)
            result.append(i)
    
    return len(result) * 65536 // len(a_result)