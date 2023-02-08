
import re



def main():
    f=open('Day5.txt')
    stacks=f.readlines()
    f.close()
    
    col=[[0 for i in range(0)] for j in range(9)]
    for i in range(7,-1,-1):
        j=stacks[i]
        print(j)
        for k in range(9):
            if len(j)>=(k*4+1) and j[k*4+1]!=' ':
                col[k].append(j[k*4+1])
                
    part=2   
    for i in range(10,514):
        j=stacks[i]
        match=re.search(r'(\d+) from (\d) to (\d)',j)
        num=int(match.group(1))
        scol=int(match.group(2))-1
        ecol=int(match.group(3))-1
        delcol=len(col[scol])-num
        for k in range(num):
            if part==1:
                l=col[scol].pop()
            if part==2:
                l=col[scol].pop(delcol)
            col[ecol].append(l)
    
    outstr=''
    for i in col:
        outstr+=i[-1]
    print(outstr)
    
    
if __name__ == '__main__':
    main()
    
    