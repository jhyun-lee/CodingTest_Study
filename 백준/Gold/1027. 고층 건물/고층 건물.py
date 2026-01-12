import sys


n = int(sys.stdin.readline())
Build = list(map(int, sys.stdin.readline().split()))
answer=0

def LineCheck(a,b,c):
    # 시작, 끝, 중간빌딩
    #(a,Build[a]) ,(b,Build[b]), (c,Build[c])

    Case_1 = (Build[b]-Build[a])/(b-a)

    Case_2 = (Build[c]-Build[a])/(c-a)

    # 안겹침
    if Case_1 > Case_2:
        return False
    
    return True

    
Build_Map = [[] for _ in range(n)]


for i in range(n-1):
    Case_1 = (Build[i+1]-Build[i])
    Build_Map[i].append(i+1)
    Build_Map[i+1].append(i)

    for j in range(i+2,n):
        Case_2 = (Build[j]-Build[i])/(j-i) 
        if Case_1 < Case_2:
            Case_1 = Case_2
            Build_Map[i].append(j)
            Build_Map[j].append(i)
            


for i in Build_Map:
    answer = max(answer,len(i))

print(answer)

        

