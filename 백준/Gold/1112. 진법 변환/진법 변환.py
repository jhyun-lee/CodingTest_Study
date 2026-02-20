import sys

input = sys.stdin.readline
x,b = map(int, input().split())


if x == 0:
    print(0)
else:
    check_Minu = False
    if b > 0 and x < 0:
        check_Minu = True
        x = -x

    result = []

    while x != 0:
        remainder = x % abs(b)
        result.append(str(remainder))
        x = (x - remainder) // b


    res_str = "".join(reversed(result))
    if check_Minu:
        print("-" + res_str)
    else:
        print(res_str)
