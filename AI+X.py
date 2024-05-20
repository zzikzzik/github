import random

arr = []
while len(arr) != 6 : #6개 숫자 생성
    n = random.randint(1,45) # 1~45 난수생성
    if n not in arr: #중복 X
        arr.append(n)
print(arr)#6개 로또 숫자 출력