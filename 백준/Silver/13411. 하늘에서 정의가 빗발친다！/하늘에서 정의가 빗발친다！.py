import sys,math

def CalDistance(x,y):
    dist = math.sqrt(x*x+y*y)

    return dist

Count = int(input())
list =[]

for i in range(Count):
    x,y,v = map(int,sys.stdin.readline().split())
    Time = CalDistance(x,y)/v
    list.append([i,Time])

list = sorted(list, key=lambda a: (a[1], a[0]))

for i in range(Count):
    print(list[i][0]+1)