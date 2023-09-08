from random import *
over=1
wicket=0
total=0
print('Team 1:')
while(over<=6):
    if(wicket<5):
        print(f'over{over}:',end=' ')
        balls=0
        while(balls<6):
            if(wicket<5):
                ball=randint(0,9)
                if(ball>=0 and ball<=6):
                    print(ball,end=' ')
                    total=total+ball
                elif(ball==7):
                    out=randint(0,3)
                    if(out==0):
                        print(end='B ')
                        wicket+=1
                    elif(out==1):
                        print(end='C ')
                        wicket+=1
                    elif(out==2):
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
        print('\tTotal:',total,end=' ')
        print('\tWicket:',wicket,end=' ')
        print()
    over+=1
print('Team 2:')
over=1
wicket=0
total_1=0
while(over<=6):
    if(wicket<5):
        if(total_1<total):
            print(f'over{over}:',end=' ')
            balls=0
            while(balls<6):
                if(wicket<5):
                    if(total_1<total):
                        ball=randint(0,9)
                        if(ball>=0 and ball<=6):
                            print(ball,end=' ')
                            total_1=total_1+ball
                        elif(ball==7):
                            out=randint(0,3)
                            if(out==0):
                                print(end='B ')
                                wicket+=1
                            elif(out==1):
                                print(end='C ')
                                wicket+=1
                            elif(out==2):
                                print(end='S ')
                                wicket+=1
                            else:
                                print(end='R ')
                                wicket+=1
                        elif(ball==8):
                            print(end='N ')
                            total_1+=1
                            balls-=1
                        else:
                            print(end='W ')
                            total_1+=1
                            balls-=1
                balls+=1
            print('\tTotal:',total_1,end=' ')
            print('\tWicket:',wicket,end=' ')
            print()
    over+=1
if(total<total_1):
    print('Team 2 won.')
elif(total==total_1):
    print('Tie match')
else:
    print('Team 1 won')
