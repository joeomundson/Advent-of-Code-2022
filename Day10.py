
import re



def main():
    f=open('Day10.txt')
    instructions=f.readlines()
    f.close()
    
    X=[[1,1]]
    for line in instructions:
        if re.search(r'noop',line):
            inst='N'
            try:
                X.append([X[-1][0]+1,X[-1][1]])
            except:
                X.append([1,1])
        else:
            inst='A'
            add=int(line[5:])
            try:
                X.append([X[-1][0]+1,X[-1][1]])
            except:
                X.append([1,1])
            X.append([(X[-1][0])+1,(X[-1][1])+add])
    
    print(X)
    signal=0
    for i in [19,59,99,139,179,219]:
        
        signal+=X[i][0]*X[i][1]
        print(X[i][0],X[i][1],X[i][0]*X[i][1])
    #print(X)
    print(signal)
        
    CRT=''
    for i in range(len(X)):
        j=i
        while j>39:
            j-=40
        
        if abs(j-X[i][1])<2:
            CRT+='#'
        else:
            CRT+=' '
        #print(j,X[i][1],)
    for j in range(6):
        print(CRT[j*40:(j+1)*40])
        
            
    
if __name__ == '__main__':
    main()
    
    