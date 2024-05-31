goal = int(input())
fiveKgNum = goal//5
remain = goal%5

if remain==0:
    print(fiveKgNum)
elif remain==1:
    if fiveKgNum >= 1:
        print(fiveKgNum+1) #5kg 포대 하나 빼고 3kg 2개 더하니 +1
    else:
        print("-1")
elif remain==2:
    if fiveKgNum >= 2:
        print(fiveKgNum+2) #5kg 포대 두개 빼고 3kg 4개 더하니 +2
    else:
        print("-1")
elif remain==3:
    print(fiveKgNum+1) #그냥 3kg 하나 더하니 +1
elif remain==4:
    if fiveKgNum >= 1:
        print(fiveKgNum+2) # 5kg 하나 빼고 3kg 3개 더하기
    else:
        print("-1")