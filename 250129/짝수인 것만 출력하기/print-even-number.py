n = int(input())
arr = list(map(int,input().split()))

even_arr = [i for i in arr if i % 2 == 0]

for i in even_arr :
    print(i,end=' ')