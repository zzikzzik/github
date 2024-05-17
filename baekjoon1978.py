import math

n = int(input())
arr = list(map(int, input().split()))
count = 0
for i in range(n):
    Tf = True
    root = int(math.sqrt(arr[i]))
    if arr[i] == 1:
        Tf = False
    for j in range(2,root+1):
        if arr[i]%j == 0 :
            Tf = False
    if Tf:
        count += 1
print(count)