T = int(input())
#for z in range(T):
#    i,j = map(int,input().split())
#    List = list(map(int,input().split()))
#    num = List[j]
#    th = 0
#    bigger = []
#    for a in range(i):
#        if List[a] > num:
#            th += 1
#            bigger.append(List[a])
#    frontList = List[:j]
#    for b in range(i-1,-1,-1):
#        if bigger == []:
#            backList = []
#        elif List[b] == min(bigger):
#            backList = List[b:]
#            break
#    
#    print(th + frontList.count(num) + backList.count(num) +1)


#상특) 시키는거 그대로 구현함
def backThrow(List):
    return List[1:] + [List[0]]

for z in range(T):
    order = 1
    i,j = map(int,input().split())
    List = list(map(int,input().split()))
    List[j] = str(List[j])
    while True:
        while type(List[0]) != str:
            Tf = 0
            for k in List[1:]:
                if int(k) > int(List[0]):
                    Tf = 1
                    List = backThrow(List)
            if Tf == 0:
                del List[0]
                order += 1
        Tf = 2
        for k in List[1:]:
                if k > int(List[0]):
                    Tf = 1
                    List = backThrow(List)
                    break
        if Tf == 2:
            print(order)
            break