A = ' ' + input()

#완전탐색

#선택할 문자의 위치를 i1 i2 i3 i4
# 1<= i1 < i2 < i3 < i4 = 100

cnt = 0
for i1 in range(1,len(A)):
    for i2 in range(i1 + 1,len(A)):
        for i3 in range(i2 + 1,len(A)):
            for i4 in range(i3 + 1,len(A)):
                if i1 + 1 == i2 and i3 + 1 == i4:
                    if A[i1] == '(' and A[i2] == '(' and A[i3] ==')' and A[i4] ==')':
                        cnt += 1

print(cnt)