def roundfloat(n):
    sum = int(n)
    n -= int(n)
    if n >= 0.5:
        return sum+1
    else:
        return sum

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
cuttingNum = roundfloat(n * 0.15)
sum = 0
for i in range(cuttingNum,n-cuttingNum):
    sum += arr[i]
if n == 0:
    print(0)
else:
    print(roundfloat(sum/(n - 2 * cuttingNum)))
