def solution(answers):
    answer = []
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    
    cnts = [0] * 4
    for i in range(len(answers)):
        v1 = p1.pop(0)
        v2 = p2.pop(0)
        v3 = p3.pop(0)
        
        if v1 == answers[i]:
            cnts[1] += 1
        if v2 == answers[i]:
            cnts[2] += 1
        if v3 == answers[i]:
            cnts[3] += 1
            
        p1.append(v1)
        p2.append(v2)
        p3.append(v3)
        
    for j in range(1, len(cnts)):
        if cnts[j] == max(cnts):
            answer.append(j)
    
    return answer