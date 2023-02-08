
import re


def main():
    f=open('Day8.txt')
    forest=f.readlines()
    f.close()
    farray=[[1 for i in range(99)] for j in range(99)]
    i=0
    for row in forest:
        line=re.search(r'(\d+)',row)
        farray[i]=line.group(1)
        i+=1
        
    tfarray=list(map(list,zip(*farray))) #transpose the array
    visible=98*4
    bestview,besttree,ibest,jbest=0,0,0,0
    
    for i in range(1,98): #99
        for j in range(1,98): #100
            tree=farray[i][j]
            left=farray[i][:j]
            right=farray[i][j+1:]
            top=''.join(tfarray[j][:i])
            bottom=''.join(tfarray[j][i+1:])
            viewleft,viewright,viewup,viewdown=0,0,0,0
            if tree>max(left) or tree>max(right) or tree>max(top) or tree>max(bottom):
                visible+=1
            for a in reversed(left):
                if a<=tree:
                    viewleft+=1
                if a>=tree:
                    break
            for a in right:
                if a<=tree:
                    viewright+=1
                if a>=tree:
                    break
            for a in reversed(top):
                if a<=tree:
                    viewup+=1
                if a>=tree:
                    break
            for a in bottom:
                if a<=tree:
                    viewdown+=1
                if a>=tree:
                    break
            viewscore=viewleft*viewright*viewup*viewdown
            if viewscore>bestview:
                bestview=viewscore
                ibest=i
                jbest=j
                besttree=tree
                
    print(visible,'trees are visible from the outside.')
    print('The highest scenic score is',bestview,'from a tree of height',besttree,'at index [',ibest,jbest,'].')
    
if __name__ == '__main__':
    main()
    
    