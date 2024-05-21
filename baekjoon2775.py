def sum(list,i,j):
    summation = 0
    for k in range(j+1):
        summation += list[i-1][k] #i,j를 받고 i-1층의 0 ~ j까지의 합을 리턴.
    return summation

Apartment = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14]]
T = int(input())
maxK = 0
for a in range(T):
    k = int(input())
    n = int(input()) - 1
    if maxK < k:
        maxK = k
        while len(Apartment) <= maxK:
            Apartment.append(["_","_","_","_","_","_","_","_","_","_","_","_","_","_"])
    if Apartment[k][n-1] != "_":
        print(Apartment[k][n])
    else:
        for i in range(1,k):
            for j in range(n+1):
                if Apartment[i][j] == "_":
                    Apartment[i][j] = sum(Apartment,i,j)
        print(sum(Apartment,k,n))