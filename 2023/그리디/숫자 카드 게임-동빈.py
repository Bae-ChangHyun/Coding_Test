
#! [모범답안]
# n,m=map(int,input().split())
# result=0

# # 1번 솔루션
# for i in range(n):
#     data=list(map(int,input().split()))
#     min_val=min(data)
#     result=max(result,min_val)
# # 2번 솔루션 
# for i in range(n):
#     data=list(map(int,input().split()))
#     min_val=1001
#     for a in data:
#         min_val=min(min_val,a)
#     result=max(result,min_val)
#? 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수를 찾기
#? 나동빈 코딩테스트(p.98), 2019 국가 교육기관 코딩 테스트 

#! [내 답안]
matrix=[]
answer=0
for i in range(row):
    matrix.append(list(map(int,input().split())))

min_num=[]
for i in range(row):
    min_num.append(min(matrix[i]))
print(max(min_num))