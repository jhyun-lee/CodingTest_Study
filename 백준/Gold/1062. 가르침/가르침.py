import sys
from itertools import combinations

input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    
    if k < 5:
        print(0)
        return
    if k == 26:
        print(n)
        return

    # 필수 글자 세트
    base_set = {'a', 'n', 't', 'i', 'c'}
    word_set = []

    all_candidates = set()

    for _ in range(n):
        word = input().strip()
        needed = set(word) - base_set
        word_set.append(needed)
        all_candidates.update(needed)

    can_learn = list(all_candidates)
    
    if len(can_learn) <= k - 5:
        print(n)
        return


    max_count = 0
    for learn_comb in combinations(can_learn, k - 5):
        learned = set(learn_comb)
        
        count = 0
        for req in word_set:
            if req.issubset(learned):
                count += 1
        
        max_count = max(max_count, count)

    print(max_count)

solve()