def solution(participant, completion):
    answer = {}
    
    for p in participant:
        answer[p] = answer.get(p, 0) + 1
    
    for c in completion:
        answer[c] -= 1
    
    for a in answer:
        if answer[a]:
            return a