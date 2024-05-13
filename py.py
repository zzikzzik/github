# 백준 1920번
# for문하고 in 쓰면 시간초과 나서 이진분류인가 그거로함

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
n = int(input())
comArr = list(map(int, input().split()))
for i in comArr:
    min = 0
    max = len(arr) - 1
    Tf = 0
    while min+1 != max:
        mid = int((min+max)/2)
        if arr[mid] == i:
            print("1")
            Tf = 1
            break
        elif arr[mid] > i:
            max = mid
        elif arr[mid] < i:
            min = mid
    
    if Tf == 1:
        continue

    if (arr[max] == i) or (arr[min] == i):
        print("1")
    else :
        print("0")