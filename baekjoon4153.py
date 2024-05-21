while True:
    Arr = list(map(int,input().split()))
    if Arr[0] == Arr[1] == Arr[2] == 0:
        break
    Max = max(Arr)
    Arr.remove(Max)
    sum = 0
    for i in Arr:
        sum += i*i
    if sum == Max*Max :
        print("right")
    else :
        print("wrong")