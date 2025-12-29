N=input()
Base = 665
CountSix =0

while(True):
    Next = Base+1
    Base = Next

    if str(Next).count('666')>=1:
        CountSix+=1

    if CountSix==int(N):
        print(Base)
        break
