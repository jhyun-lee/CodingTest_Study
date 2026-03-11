import sys

input = sys.stdin.readline


N,M = map(int,input().split())


BookList= list(map(int,input().split()))

BookList_A =[]
BookList_B =[]

for i in BookList:

    if i<0:
        BookList_A.append(-i)
    else:
        BookList_B.append(i)



BookList_A.sort(key=lambda x : -x)
BookList_B.sort(reverse=True)


answer=0

for i in range(0, len(BookList_A), M):
    answer += BookList_A[i] * 2


for i in range(0, len(BookList_B), M):
    answer += BookList_B[i] * 2

print(answer-max(BookList_A+BookList_B))