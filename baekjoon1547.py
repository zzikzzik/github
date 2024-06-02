T = int(input())
ball = 1
for i in range(T):
    swapList = list(map(int,input().split()))
    if swapList[0] == ball:
        ball = swapList[1]
    elif swapList[1] == ball:
        ball = swapList[0]
print(ball)