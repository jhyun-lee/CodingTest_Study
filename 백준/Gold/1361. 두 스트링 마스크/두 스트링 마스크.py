import sys

input = sys.stdin.readline


STR_1 = input().split()
STR_2 = input().split()


def depart(string):
    parts = string.split('*') 
    return parts[0], parts[1]



STR_1_F, STR_1_B = depart(STR_1[0])
STR_2_F, STR_2_B = depart(STR_2[0])



def Fun(STR_1_F, STR_1_B, STR_2_F, STR_2_B):

    if not (STR_1_F.startswith(STR_2_F) or STR_2_F.startswith(STR_1_F)):
        print("-1")
        return

    if not (STR_1_B.endswith(STR_2_B) or STR_2_B.endswith(STR_1_B)):
        print("-1") 
        return


    res_pref = STR_1_F if len(STR_1_F) > len(STR_2_F) else STR_2_F
    res_suff = STR_1_B if len(STR_1_B) > len(STR_2_B) else STR_2_B




    ans = None

    for i in range(min(len(res_pref), len(res_suff)) + 1):
        if i == 0 or res_pref[-i:] == res_suff[:i]:
            candidate = res_pref + res_suff[i:]
            
            if (len(candidate) >= len(STR_1_F) + len(STR_1_B) and 
                len(candidate) >= len(STR_2_F) + len(STR_2_B)):
                if ans is None or len(candidate) < len(ans):
                    ans = candidate

    if ans:
        print(ans)
    else:
        print("-1")



Fun(STR_1_F, STR_1_B, STR_2_F, STR_2_B)

