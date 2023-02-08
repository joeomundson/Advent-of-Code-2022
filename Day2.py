
#A=rock
#B=paper
#C=scissors
#X=rock / lose
#Y=paper / draw
#Z=scissors / win


def main():
    f=open('Day2.txt')
    RPSlist=f.readlines()
    f.close()
    score=0
    for RPS in RPSlist:
        E=RPS[0]
        M=RPS[2]
        if M=='X':  #lose
            if E=='A': #lose to rock -scissors
                score+=3
            if E=='B': #lose to paper -rock
                score+=1
            if E=='C': #lose to scissors -paper
                score+=2
        if M=='Y':  #draw
            score+=3
            if E=='A': #draw with rock -rock
                score+=1
            if E=='B': #draw with paper -paper
                score+=2
            if E=='C': #draw with scissors -scissors
                score+=3
        if M=='Z':  #win
            score+=6
            if E=='A': #win against rock -paper
                score+=2
            if E=='B': #win against paper -scissors
                score+=3
            if E=='C': #win against scissors -rock
                score+=1
                
        #part 1:        
        '''if M=='X':  #rock
            score+=1
            if E=='A':
                score+=3
            if E=='C':
                score+=6
        if M=='Y':  #paper
            score+=2
            if E=='B':
                score+=3
            if E=='A':
                score+=6
        if M=='Z':  #scissors
            score+=3
            if E=='C':
                score+=3
            if E=='B':
                score+=6'''
                
                
    print(score)
        

if __name__ == '__main__':
    main()