
#A=rock
#B=paper
#C=scissors
#X=rock / lose
#Y=paper / draw
#Z=scissors / win
import re



def main():
    f=open('Day4.txt')
    areas=f.readlines()
    f.close()
    count=0
    for line in areas:
        match=re.search(r'(\d+)-(\d+),(\d+)-(\d+)',line)
        E1s=int(match.group(1))
        E1f=int(match.group(2))
        E2s=int(match.group(3))
        E2f=int(match.group(4))
        if E1s<=E2s<=E1f or E1s<=E2f<=E1f or E2s<=E1s<=E2f or E2s<=E1f<=E2f:
            count+=1
        #if ((E1s>=E2s) and (E1f<=E2f)) or ((E2s>=E1s) and (E2f<=E1f)):
        #    count+=1
    print(count)
if __name__ == '__main__':
    main()
    
    