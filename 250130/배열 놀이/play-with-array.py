# n q : 3 3
# 원소의 값(n) : 1 8 5
# q개의 줄에 걸쳐 질의 주어짐
# 1 ?
# 2 ? 이런식

# 1 : x번째 원소
# 2 : 원소중에 일치하는걸 찾고 몇번째인지 출력
# > 여러개라면 가장 인덱스 작은것 출력
# > 없으면 0

# x부터 y까지 공백으로 구분하여 출력

cnt = 0

n, q = list(map(int,input().split()))

arr = list(map(int,input().split()))

temp = [0]

for i in range(n):
    temp.append(arr[i])

for i in range(q):
    que = list(map(int,input().split()))

    if que[0] == 1 :
        a = que[1]
        print(temp[a])
    if que[0] == 2 :
        b = que[1]
        for j in range(1,n+1):
            if b == temp[j]:
                print(j)
                break
    if que[0] == 3 :
        s,e = que[1],que[2]
        for i in range(s,e+1):
            print(temp[i],end=' ')
        print()