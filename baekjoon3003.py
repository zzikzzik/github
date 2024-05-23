List = list(map(int,input().split()))
Need = [1,1,2,2,2,8]
for i in range(6):
    List[i] = Need[i] - List[i]
    print(List[i], end=" ")