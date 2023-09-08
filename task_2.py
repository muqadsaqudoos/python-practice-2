from random import *
over=1
wicket=0
total=0
print("Team 1:")
while(over<=6):
    if(wicket<5):
        print(f'over{over}:',end='')
        balls=0
        while(balls<6):
            ball=randint(0,9)
            if(wicket<5):
                if(ball>=0 and ball<=6):
                    print(ball,end=' ')
                    total=total+ball
                elif(ball==7):
                    out=randint(0,3)
                    if(ball==0):
                        print(end='B ')
                        wicket+=1
                    elif(ball==1):
                        print(end='C ')
                        wicket+=1
                    elif(ball==2):
                        print(end='S ')
                        wicket+=1
                    else:
                        print(end='R ')
                        wicket+=1
                elif(ball==8):
                    print(end='N ')
                    total+=1
                    balls-=1
                else:
                    print(end='W ')
                    total+=1
                    balls-=1
            balls+=1
        over+=1
        print("\t\tTotal:",total,end='')
        print("\t\twicket:",wicket,end='')
        print()

                    

