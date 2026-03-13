import sys



N= int(input())
StrList =[]

answerList = [0 for _ in range(26)]
answer = 0


for i in range(N):

    save = input().strip()

    power = len(save) - 1 

    for char in save:
        answerList[ord(char) - ord('A')] += 10 ** power
        power -= 1


Count =9

answerList.sort(reverse=True)


for i in range(10):
    answer+=answerList[i]*Count
    Count-=1


print(answer)

