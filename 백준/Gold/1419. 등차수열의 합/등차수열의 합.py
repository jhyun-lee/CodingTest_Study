import sys

def count_multiples(low, high, k, min_val):
    actual_low = max(low, min_val)
    if actual_low > high:
        return 0

    return (high // k) - ((actual_low - 1) // k)

def solve():
    l = int(sys.stdin.readline())
    r = int(sys.stdin.readline())
    k = int(sys.stdin.readline())

    if k == 2:
        print(max(0, r - max(l, 3) + 1))
    elif k == 3:
        print(count_multiples(l, r, 3, 6))
    elif k == 4:
        ans = count_multiples(l, r, 2, 10)
        if l <= 12 <= r:
            ans -= 1
        print(max(0, ans))
    elif k == 5:
        print(count_multiples(l, r, 5, 15))

solve()