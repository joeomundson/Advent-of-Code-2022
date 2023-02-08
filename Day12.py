def gprint(grid):
    for i in grid:
        a = ''
        if type(i) != 'str':
            for j in i:
                k = "{:<3}".format(j)
                a += k
            print(a)
        else:
            print(i)


def main():
    f = open('Day12.txt')
    landscape = f.readlines()
    f.close()
    la = [[0 for i in range(70)] for j in range(41)]
    visited = [[0 for i in range(70)] for j in range(41)]
    for i in range(41):
        for j in range(70):
            la[i][j] = ord(landscape[i][j]) - 96
            visited[i][j] = 0
            if landscape[i][j] == 'S':
                start = (i, j)
                la[i][j] = 1
            if landscape[i][j] == 'E':
                end = (i, j)
                la[i][j] = 26
    # gprint(visited)
    groups = {0: [[0, 0]]}
    # print(start,end) #20,0 20,46

    done = 0
    checklist = [end]
    newcheck = []
    pathdict = {end: ''}
    spath = ()
    while done == 0:
        for k in checklist:
            l = k[0]
            m = k[1]
            path = pathdict[(l,m)]
            v = la[l][m]  # thiscell
            if m > 0:
                w = la[l][m - 1]  # left
                if (w == v or w == (v - 1) or w > v) and visited[l][m - 1] == 0:  # check left
                    if w == 1:
                        spath = (l,m-1)
                    pathdict[(l, m - 1)] = path + 'L'
                    visited[l][m - 1] = 1
                    newcheck.append((l, m - 1))
                    # print('checkleft', newcheck)
            if m < 69:
                x = la[l][m + 1]  # right
                if (x == v or x == (v - 1) or x > v) and visited[l][m + 1] == 0:  # check right
                    if x == 1:
                        spath = (l, m+1)
                    pathdict[(l, m + 1)] = path + 'R'
                    visited[l][m + 1] = 1
                    newcheck.append((l, m + 1))
                    # print('checkright', newcheck)
            if l > 0:
                y = la[l - 1][m]  # up
                if (y == v or y == (v - 1) or y > v) and visited[l - 1][m] == 0:  # check up
                    if y == 1:
                        spath = (l-1, m)
                    pathdict[(l - 1, m)] = path + 'U'
                    visited[l - 1][m] = 1
                    newcheck.append((l - 1, m))
                    # print('checkup', newcheck)
            if l < 40:
                z = la[l + 1][m]  # down
                if (z == v or z == (v - 1) or z > v) and visited[l + 1][m] == 0:  # check down
                    if z == 1:
                        spath = (l+1, m)
                    pathdict[(l + 1, m)] = path + 'D'
                    visited[l + 1][m] = 1
                    newcheck.append((l + 1, m))
                    # print('checkdown', newcheck)
                    # print(la[1][5], la[l + 1][m], la[l][m])
        checklist = newcheck
        #if start in checklist:
            #print('path:', pathdict[start])
            #print(len(pathdict[start]))
        if spath:
            print('path:', pathdict[spath])
            print(len(pathdict[spath]))
            done = 1
        newcheck = []

    gprint(visited)

    modi=end[0]
    modj=end[1]
    #for a in pathdict[start]:
    for a in pathdict[spath]:
        if a == 'L':
            #text = 'abcdefg'
            #text = text[:1] + 'Z' + text[2:]
            landscape[modi] = landscape[modi][:modj] + '<' + landscape[modi][(modj+1):]
            modi,modj = [modi, modj - 1]
        elif a == 'R':
            landscape[modi] = landscape[modi][:modj] + '>' + landscape[modi][(modj+1):]
            modi,modj = [modi, modj + 1]
        elif a == 'U':
            landscape[modi] = landscape[modi][:modj] + '^' + landscape[modi][(modj+1):]
            modi,modj = [modi - 1, modj]
        elif a == 'D':
            landscape[modi] = landscape[modi][:modj] + 'v' + landscape[modi][(modj+1):]
            modi,modj = [modi + 1, modj]
    for i in landscape:
        print(i)
    # print(groups, '-----')
    # gprint(visited)


if __name__ == '__main__':
    main()
