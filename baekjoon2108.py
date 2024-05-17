import sys
print = sys.stdout.write
input = sys.stdin.readline #시간초과 나서 이렇게했음

arr = []
sum = 0
Dict = {}

T = int(input().rstrip())
for i in range(T):
    n = int(input().rstrip())
    arr.append(n)
    sum += n
    Dict[n] = 0
arr.sort()
for i in arr:
    Dict[i] += 1
max = max(Dict.values())
maxList = []
for k, v in Dict.items():
    if v == max:
        maxList.append(k)
maxList.sort()

print(str(round(sum/T))+"\n")
print(str(arr[int((T-1)/2)])+"\n")
if len(maxList) == 1:
    print(str(maxList[0])+"\n")
else :
    print(str(maxList[1])+"\n")
print(str(arr[T-1] - arr[0])+"\n")