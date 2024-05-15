import math
import sys
print = sys.stdout.write
input = sys.stdin.readline

min,max = map(int,input().split())
TfList = [True for i in range(max)]
#TfList 의 i번째 의미 : i+1은 소수인가?
primes = list(range(2,int(math.sqrt(max))+1))
TfList[0] = False
for i in primes:
    j = 2
    while i * j <= max:
        TfList[i*j-1] = False
        j += 1

for i in range(min,max +1):
    if TfList[i-1]:
        print(str(i)+"\n")

#5/15 : 어제 문제점 : 큰 수의 제곱근 이하의 약수로 나는게 아닌 리스트 속 요소들로만 나누었음.