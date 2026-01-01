import sys

N,M = map(int,sys.stdin.readline().split())


SnowList=[0]
SnowList.extend(list(map(int,sys.stdin.readline().split())))

def FindCal(location,Time,Size):
    if Time==0 or location>=N:
        return Size
    
    case_1, case_2 = 0, 0

    if location+1 <= N:
        case_1 = FindCal(location+1,Time-1,Size+SnowList[location+1])


    if location+2 <= N:
        case_2 = FindCal(location+2,Time-1,Size//2+SnowList[location+2])
    
    Size = max(Size, case_1,case_2)

    return Size

print(FindCal(0,M,1))