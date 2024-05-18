def distinguishSum(n):
    strN = str(n)
    sum = n
    for i in strN:
        sum += int(i)
    return sum

n = int(input())
Tf = True
for i in range(1,n):
    if distinguishSum(i)==n:
        print(i)
        Tf = False
        break
if Tf:
    print("0")