n = int(input())
List = []
for i in range(n):
    List.append(list(map(int,input().split())))
List.sort()
for i in List:
    print(i[0],i[1])
    #이게되네