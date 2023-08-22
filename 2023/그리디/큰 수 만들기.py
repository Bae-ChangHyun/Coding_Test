
#! [모범답안]
# def solution(number, k):
#     stack = []
#     for num in number:
#         while len(stack) > 0 and stack[-1] < num and k > 0:
#             k -= 1
#             stack.pop()
#         stack.append(num)
#     if k != 0:
#         stack = stack[:-k]
#     return ''.join(stack)

#? 스택으로 푸는 문제.
#? 나와 동일한 방식으로 풀었지만, 더 간단
#? https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    num=[int(i) for i in number]
    answer=[]

    for i in range(len(number)):
        if(len(answer)==0):
            answer.append(number[i])
        elif(answer[-1]<number[i]):
            while(k!=0):
                if(len(answer)==0):
                    break
                if(answer[-1]>=number[i]):
                    break
                else:
                    answer.pop(-1)
                    k-=1
            answer.append(number[i])
        else:
            answer.append(number[i])
    answer=answer[:len(number)-k]
    answer="".join(answer)
                
    return answer
            
        