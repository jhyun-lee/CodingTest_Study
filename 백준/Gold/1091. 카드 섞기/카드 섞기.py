import sys
import queue

n = int(sys.stdin.readline())
# 이사람한테는 가면 안됨 
P = list(map(int, sys.stdin.readline().split()))
# 이렇게 섞을수 있음 i 번째 카드를 s[i]로 이동시킴
S = list(map(int, sys.stdin.readline().split()))

Card=[i for i in range(n)]
initial_cards = list(Card)

def MoveCard(Save_Card): # 섞기
    Return_Card=[0 for i in range(n)]
    for i in range(n):
        Return_Card[S[i]] = Save_Card[i]

    return Return_Card

    
def Check_Card(Save_Card): # 맞는지 확인하기
    for i in range(n):
        if P[Save_Card[i]] != i % 3:
            return False
    return True

FlipCount=0

while True:
    if Check_Card(Card):
        print(FlipCount)
        break
    
    Card = MoveCard(Card)
    FlipCount+=1


    if Card == initial_cards:
        print(-1)
        break


