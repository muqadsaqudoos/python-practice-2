from random import *
def main():
    over=1
    total=0
    wicket=0
    while(over<=6):
        if(wicket<6):
            print(f'over{over}:',end='')
            balls = 0
            while balls <6:
                ball = randint(0, 9)
                if ball >= 0 and ball <= 6:
                    if(wicket<6):
                        print(ball, end = ' ')
                        total=total+ball
                elif ball == 7:
                    out = randint(0, 3)
                    if(wicket<6):
                        if out == 0:
                            print(end = 'B ')
                            wicket+=1
                        elif out == 1:
                            print(end = 'C ')
                            wicket+=1
                        elif out == 2:
                            print(end = 'S ')
                            wicket+=1
                        else:
                            print(end = 'R ')
                            wicket+=1
                elif ball == 8:
                    if(wicket<6):
                        print(end = 'W ')
                        total=total+1
                        balls-=1
                else:
                    if(wicket<6):
                        print(end = 'N ')
                        total=total+1
                        balls-=1
                balls+=1
            print('\tTotal:',total,end='')
            print('\tWickets:',wicket,end='')
            print()
            over+=1    
main()
