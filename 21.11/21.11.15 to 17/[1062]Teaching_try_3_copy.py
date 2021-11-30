from itertools import combinations
n, k = map(int, input().split())
alpha = {'b': 20, 'd': 19, 'e': 18, 'f': 17, 'g': 16, 'h': 15, 'j': 14,
            'k': 13, 'l': 12, 'm': 11, 'o': 10, 'p': 9, 'q': 8, 'r': 7,
            's': 6, 'u': 5, 'v': 4, 'w': 3, 'x': 2, 'y': 1, 'z': 0}
#각 문자에 비트마스킹을 하기위해 값을 매칭시켜둠 

if k < 5: #배울 수 있는 단어가 총 5개도 안되면 기본 단어도 못배우니까 0출력
    print(0)
else:
    k -= 5 #k에서 기본단어 개수 5개 미리 제외
    nece_chars = {'a', 'n', 't', 'i', 'c'}
    input_chars = []
    cnt = 0
    for _ in range(n):
        tmp = 0
        for c in set(input())-nece_chars: #입력받은 단어에서 필수(a,n,t,i,c)를 제외한 것중
            #print(alpha)
            tmp |= (1 << alpha[c])
        input_chars.append(tmp)
        #print(input_chars) 배워야 할 모든 문자를 비트연산자로 하나의 십진수로 표현해둠 
    power_by_2 = (2**i for i in range(21)) # 2의n승 중에 알파벳26개에서 5개를 제외한 21개에서 모든 조합을 뽑음 
    for comb in combinations(power_by_2, k):
        test = sum(comb)
        ct = 0
        for cb in input_chars:
            if test & cb == cb: #만든 조합이 우리가 필요한 글자에 있으면 ct올림 
                ct += 1
        cnt = max(cnt, ct)
    print(cnt)