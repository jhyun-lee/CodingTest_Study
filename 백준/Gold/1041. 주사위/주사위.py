import sys
import queue

n = int(sys.stdin.readline())
cube = list(map(int, sys.stdin.readline().split()))

Min_Cube = min(cube[2],cube[3])

One_Cube_Min = min(cube)
Two_Cube_Min=987654321
Three_Cube_Min = 987654321

Save_cube=[cube[4],cube[0],cube[1],cube[5]]

for i in range(len(Save_cube)):
    Cube_1 = Save_cube[i]
    Cube_2 =0

    if i==len(Save_cube)-1:
        Cube_2 = Save_cube[0]
    else:
        Cube_2 = Save_cube[i+1]

    
    Three_Cube_Min = min(Three_Cube_Min,Min_Cube+Cube_1+Cube_2)

for i in range(len(cube)):
    for j in range(i+1,len(cube)):
        if i + j == 5:
            continue
        
        Two_Cube_Min = min(Two_Cube_Min,cube[i]+cube[j])


if n == 1:
    print(sum(cube) - max(cube))
else:
    Three_Cube = 4
    Two_Cube =  (n-1)*4 + (n-2)*4
    One_Cube = (n-1)*(n-2)*4 +(n-2)*(n-2)

    answer = Three_Cube* Three_Cube_Min + Two_Cube * Two_Cube_Min+ One_Cube*One_Cube_Min
    print(answer)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
