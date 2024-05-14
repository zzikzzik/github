import math # 루트 사용
import sys #빠른 입출력
print = sys.stdout.write

min,max = map(int,input().split())
list = [2]
i = 1
while (2*i+1) <= max:
    num = [2*i + 1]
    list += num
    i += 1
i = 0
while list[i] < int(math.sqrt(max)):
    for j in list:
        if (j%list[i] == 0) and (j != list[i]):
            list.remove(j)
    i += 1
list = set(list)
for i in range(min,max+1):
    if i in list:
        print(str(i)+"\n")