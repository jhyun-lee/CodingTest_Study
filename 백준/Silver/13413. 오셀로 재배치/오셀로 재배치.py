import sys,math

Count = int(input())

for i in range(Count):
    len_Input = int(input())
    Base_1 = input()
    Base_2 = input()

    Count_W=0
    Count_B=0

    for i in range(len_Input):
        if Base_2[i]!=Base_1[i]:
            
            if Base_2[i]=='W':
                Count_W+=1
            elif Base_2[i]=='B':
                Count_B+=1

    Flip = 0
    change=0

    if Count_W>Count_B:
        Flip= Count_W-Count_B
        change = Count_W-Flip
    else:
        Flip= Count_B-Count_W
        change = Count_B-Flip

    print(Flip+change)