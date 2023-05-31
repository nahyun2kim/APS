def solution(n, words):
    answer = [0, 0]
    nth = [1] + [0] * (n - 1)
    keywords = [words[0]]
    for i in range(1, len(words)):
        nth[i % n] += 1
        if words[i] in keywords or keywords[-1][-1] != words[i][0]:
            answer[0] = i % n + 1
            answer[1] = nth[i % n]
            break
        keywords.append(words[i])
    return answer