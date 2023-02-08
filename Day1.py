


def main():
    f=open('Day1.txt')
    clist=f.readlines()
    f.close()
    totalcal=[]
    calsum=0
    for line in clist:
        if line=='\n':
            totalcal.append(calsum)
            calsum=0
        else:
            calsum+=int(line)
    if calsum!=0:
        totalcal.append(calsum)
    maxcal=max(totalcal)
    print('The elf with the most calories is carrying '+str(maxcal)+' calories.')
    sortcal=sorted(totalcal,reverse=True)
    top3cal=sum(sortcal[0:3])
    print('The top 3 elves are carrying '+str(top3cal)+' calories.')

if __name__ == '__main__':
    main()