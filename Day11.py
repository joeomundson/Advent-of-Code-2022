
import re

'''Monkey 1:
  Starting items: 96, 82, 61, 99, 82, 84, 85
  Operation: new = old + 8
  Test: divisible by 7
    If true: throw to monkey 0
    If false: throw to monkey 7'''

def monkeyparser(m):
    monkeydata={}
    mnums=re.findall(r'Monkey (\d+):',m)
    mitems=re.findall(r'Starting items:\s(.*\d\d)',m)
    mops=re.findall(r'Operation: new =\s(.*)',m)
    mtest=list(map(int,re.findall(r'Test: divisible by\s(\d*)',m)))
    mtrue=list(map(int,re.findall(r'If true: throw to monkey\s(\d)',m)))
    mfalse=list(map(int,re.findall(r'If false: throw to monkey\s(\d)',m)))
    for i in range(8):
        items=list(map(int,re.findall(r'(\d\d)',mitems[i])))
        monkeydata[mnums[i]+'_items']=items
        monkeydata[mnums[i]+'_ops']=mops[i]
        monkeydata[mnums[i]+'_test']=mtest[i]
        monkeydata[mnums[i]+'_true']=mtrue[i]
        monkeydata[mnums[i]+'_false']=mfalse[i]
        monkeydata[mnums[i]+'_inspect']=0
    return(monkeydata)

def main():
    f=open('Day11.txt')
    monkeybiz=f.read()
    f.close()
    
    m=monkeyparser(monkeybiz)
    for h in range(10000):
        for i in range(8):
            for j in m[str(i)+'_items']:
                old=j 
                newitem=eval(m[str(i)+'_ops'])
                if newitem>=9699690:
                    newitem=newitem%9699690
                #newitem=newitem//3
                if newitem%m[str(i)+'_test'] == 0:
                    m[str(m[str(i)+'_true'])+'_items'].append(newitem)
                else:
                    m[str(m[str(i)+'_false'])+'_items'].append(newitem)
                m[str(i)+'_inspect']+=1
            m[str(i)+'_items']=[]
        
    for i in range(8):
        print(i,m[str(i)+'_inspect'])
    
            
    
if __name__ == '__main__':
    main()
    
    