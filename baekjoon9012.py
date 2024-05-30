T = int(input())
for i in range(T):
    open = 0
    PS = input()
    for j in PS:
        if j == "(":
            open += 1
        elif j == ")":
            if open == 0:
                open = -1
                break
            else: open -= 1
    if open != 0 :
        print("NO")
    else:
        print("YES")