
import re


def main():
    f=open('Day7.txt')
    path=f.readlines()
    f.close()
    curdir=['root']
    dirs={}
    dirs['root']=0
    totalsize=0
    
    for line in path:
        if line[0:6] == '$ cd /': 
            curdir=['root']
        elif line[0:7] == '$ cd ..': 
            curdir.pop()
        elif re.search(r'\$ cd \w+',line):
            thisdir=line[5:-1]
            curdir.append(thisdir)
            dirs[''.join(curdir)]=0
        elif re.search(r'(\d)+ \w+',line):
            data=re.search(r'(\d+) \w+',line)
            size=int(data.group(1))
            i=1
            for dir in curdir:
                incdir=curdir[:i]
                dirs[''.join(incdir)]+=size
                i+=1
                
    
    for dir in dirs:
        if dirs[dir]<=100000:
            totalsize+=dirs[dir]
    print(totalsize)
    
    #part 2
    totalspace=70000000
    usedspace=dirs['root']
    freespace=totalspace-usedspace
    neededspace=30000000-freespace
    print(neededspace)
    
    deldir='root'
    for dir in dirs:
        if dirs[dir]>=neededspace:
            print(dir+' '+str(dirs[dir]))
            if dirs[dir]<dirs[deldir]:
                print('!!!'+dir+' '+str(dirs[dir]))
                deldir=dir
    print(dirs[deldir])
    
    
if __name__ == '__main__':
    main()
    
    