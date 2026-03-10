import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    a = int(input_data[0])
    b = int(input_data[1])

    max_val = b
    is_prime = [True] * (max_val + 1)
    is_prime[0] = is_prime[1] = False
    
    factor_count = [0] * (max_val + 1)


    for i in range(2, max_val + 1):
        if factor_count[i] == 0: 
            for j in range(i, max_val + 1, i):
                temp = j
                while temp % i == 0:
                    factor_count[j] += 1
                    temp //= i
                    

    primes = [True] * (max_val + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(max_val**0.5) + 1):
        if primes[i]:
            for j in range(i*i, max_val + 1, i):
                primes[j] = False

    answer = 0
    for i in range(a, b + 1):
        if primes[factor_count[i]]:
            answer += 1
            
    print(answer)

solve()