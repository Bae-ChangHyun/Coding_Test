# [모범답안]
# def solution(n, lost, reserve):
#     _reserve = [r for r in reserve if r not in lost]
#     _lost = [l for l in lost if l not in reserve]
#     _resolve.sort()
#     for r in _reserve:
#         f = r - 1
#         b = r + 1
#         if f in _lost:
#             _lost.remove(f)
#         elif b in _lost:
#             _lost.remove(b)
#     return n - len(_lost)

#? 마지막 조건 여벌체육복을 가져온 사람도 잃어버릴 수 있다는, 즉 reserve와 lost에 동일한 번호가 있을 수도 있다는 것이 중요. 
#? 무조건 앞에 사람한테 먼저 빌리고, 뒤에 사람한테 물어보기. 
#? https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0
    all=[i+1 for i in range(n)]
    
    lost2=lost.copy()
    lost=list(set(lost).difference(set(reserve)))
    reserve=list(set(reserve).difference(set(lost2)))
    answer=n-len(lost)

    for i in range(len(lost)):
        if(lost[i]!=1):
            if(all[lost[i]-2] in reserve ):
                reserve.remove(all[lost[i]-2])
                answer+=1
                continue
        if(lost[i]!=n):
            if(all[lost[i]] in reserve):
                reserve.remove(all[lost[i]])
                answer+=1
                continue
    return answer
            

       
