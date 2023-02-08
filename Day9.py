
import re


def movenode(x1,y1,x2,y2):
    xdif=x1-x2
    ydif=y1-y2
    if abs(xdif)+abs(ydif)==4:
        x2+=int((xdif/2))
        y2+=int((ydif/2))
    elif abs(xdif)>1:
        x2+=int((xdif/2))
        y2=y1
    elif abs(ydif)>1:
        y2+=int((ydif/2))
        x2=x1
    #input()
    return([x2,y2])

def main():
    f=open('Day9.txt')
    moves=f.readlines()
    f.close()
    
    been={}
    tailknots=9
    xh,yh=0,0
    xyt=[[0,0] for j in range(tailknots)]
    
    for move in moves:
        dir=move[0]
        dis=int(move[2:])
        #print(xh,yh,xt,yt,dir,dis)
        if dir=='L': vec=(-1,0)
        if dir=='R': vec=(1,0)
        if dir=='D': vec=(0,-1)
        if dir=='U': vec=(0,1)
        for i in range(dis):
            xh+=vec[0]
            yh+=vec[1]
            for j in range(tailknots):
                if j==0:
                    xyt[j]=movenode(xh,yh,xyt[j][0],xyt[j][1])
                #print(xyt[j-1][0])
                #input()
                else:
                    xyt[j]=movenode(xyt[j-1][0],xyt[j-1][1],xyt[j][0],xyt[j][1])
                if j==tailknots-1:
                    been[''.join(str(xyt[j][0])+','+str(xyt[j][1]))]=1
        print(dir,dis,xyt)
                
                    
    

    #print(been)
    print(len(been))
    
    
if __name__ == '__main__':
    main()
    
    