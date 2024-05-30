A, B, V = map(int,input().split())

goal = V - A
if goal%(A-B) == 0:
    print(goal//(A-B)+1)
else : 
    print(goal//(A-B)+2)