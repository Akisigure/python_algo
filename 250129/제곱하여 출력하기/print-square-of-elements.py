n = int(input())

arr = map(int,input().split())

res = [i ** 2 for i in arr]

for i in res:
    print(i,end=' ')