# 근무 태도 점수와 동료 평가 점수
#어떤 사원이 다른 임의의 사원보다 두 점수가 모두 낮은 경우가 한 번이라도 있다면 그 사원은 인센티브를 받지 못함
# 두 점수의 합이 높은 순으로 석차를 내어 석차에 따라 인센티브가 차등 지급

# 동석차의 수만큼 다음 석차는 건너뜀

def solution(scores):
    answer = 0
    wanho_a, wanho_b = scores[0]
    wanho_sum = wanho_a + wanho_b    
    
    for i in range(len(scores)):
        scores[i].append(i)
        
    scores.sort(key= lambda x : (-x[0],x[1]))
    
    
    Base_List = []
    Max_Count = 0
    
    for i in scores:
        if Max_Count <=i[1]:
            Max_Count = i[1]
            Base_List.append(i)
        else:
            if i[2] == 0:
                return -1

        
        
    rank = 1
    for a, b, idx in Base_List:
        if a + b > wanho_sum:
            rank += 1


        
    
    return rank