import sys
input = sys.stdin.readline

N = int(input())

# 최대 공약수 구하기
def get_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소 공배수 구하기
def get_lcm(a, b):
    if a == 0 or b == 0: return 0
    return (a * b) // get_gcd(a, b)


# 숫자 전체 공배수 ㅇㅇ
def get_lcm_of_list(nums):
    save = str(nums)
    nums = [int(n) for n in save if int(n) != 0]
    if not nums: return 1
    
    res = nums[0]
    for i in range(1, len(nums)):
        res = get_lcm(res, nums[i])
        
    return res

Base = get_lcm_of_list(N)

def solve():
    k=0

    while True:
        NowK = 10**k
        Start = NowK*N


        for i in range(NowK):
            Now = Start + i

            if Now%Base==0:
                print(Now)
                return
            

        k+=1
                
solve()




