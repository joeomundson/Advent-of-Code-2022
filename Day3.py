
#A=rock
#B=paper
#C=scissors
#X=rock / lose
#Y=paper / draw
#Z=scissors / win
import re

def prioritizer(b):
    if b.isupper():
        res=ord(b)-38
    else:
        res=ord(b)-96
    print(b)
    print(res)
    return res

def main():
    f=open('Day3.txt')
    sacks=f.readlines()
    f.close()
    result=0
    inc=3
    i=0
    j=0
    print(len(sacks))
    for bag in sacks:
        if i==0:
            a=bag
            i+=1
        elif i==1:
            b=bag
            i+=1
        elif i==2:
            c=bag
            i=0
            j+=1
            print(j)
            for x in a:
                match=re.search(x,b)
                if match:
                    match2=re.search(x,c)
                    if match2:
                        result+=(prioritizer(x))
                        break
        
    
    
    
    
    
    
    '''
    for bag in sacks:
        bag1=bag[:(len(bag)//2)]
        bag2=bag[(len(bag)//2):]
        for b in bag1:
            match=re.search(b,bag2)
            if match:
                result+=(prioritizer(b))
                break'''
    print(result)
                
            
if __name__ == '__main__':
    main()
    
    
    '''>>> ord('a')
97
>>> chr(97)
'a'
>>> chr(ord('a') + 3)
'd'
>>>'''