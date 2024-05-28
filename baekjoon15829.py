T = int(input())
str = input()
sum = 0
for i in range(T):
    sum += (ord(str[i])-96)*(31**i)
print(sum%1234567891)