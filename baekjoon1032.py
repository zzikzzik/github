n = int(input())
arr = []
answer = ""
for i in range(n):
    arr.append(input())
for i in range(len(arr[0])):
    Tf = True
    for j in range(n):
        if arr[0][i] != arr[j][i]:
            Tf = False
            break
    if Tf:
        answer += arr[0][i]
    else:
        answer += "?"
print(str(answer))