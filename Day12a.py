

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


'''           
def gtest(la,i,j):
    #print(la)
    if la[i][j-1]==la[i][j] and j!=0:
            input()
            #print(la[i][j-1])
            #print('y',i,j-1)
            return 'y',i,j-1
    elif la[i-1][j]==la[i][j] and i!=0:
            print(la[i-1][j],la[i][j])
            return 'y',i-1,j
    return 'n',i,j


    '''


def expandgroup(i, j, la, ingroup, groups, a):
    done = []
    checklist = [[i, j]]
    newcheck = []
    while len(done) == 0:
        for k in checklist:
            #print('k, checklist: ', k, checklist)
            done.append(1)
            l = k[0]
            m = k[1]
            if m > 0:
                if la[l][m - 1] == la[l][m] and ingroup[l][m - 1] == -1:  # check left
                    ingroup[l][m - 1] = ingroup[l][m]
                    groups[a].append([l, m - 1])
                    newcheck.append([l, m - 1])
                    done[-1] = 0
                    #print('checkleft', newcheck)
            if m < 69:
                if la[l][m + 1] == la[l][m] and ingroup[l][m + 1] == -1:  # check right
                    ingroup[l][m + 1] = ingroup[l][m]
                    groups[a].append([l, m + 1])
                    newcheck.append([l, m + 1])
                    done[-1] = 0
                    #print('checkright', newcheck)
            if l > 0:
                if la[l - 1][m] == la[l][m] and ingroup[l - 1][m] == -1:  # check up
                    ingroup[l - 1][m] = ingroup[l][m]
                    groups[a].append([l - 1, m])
                    newcheck.append([l - 1, m])
                    done[-1] = 0
                    #print('checkup', newcheck)
            if l < 40:
                if la[l + 1][m] == la[l][m] and ingroup[l + 1][m] == -1:  # check down
                    ingroup[l + 1][m] = ingroup[l][m]
                    groups[a].append([l + 1, m])
                    newcheck.append([l + 1, m])
                    done[-1] = 0
                    #print('checkdown', newcheck)
                    #print(la[1][5], la[l + 1][m], la[l][m])
        checklist = newcheck
        if sum(done) < len(done):
            done = []
        else:
            done = [1]
        #print('newcheck: ', newcheck)
        #print('groups: ', groups[a])
        #print('la15', la[1][5])
        #gprint(ingroup)
        newcheck = []

    return ingroup, groups


def main():
    f = open('Day12.txt')
    landscape = f.readlines()
    f.close()
    la = [[0 for i in range(70)] for j in range(41)]
    ingroup = [[0 for i in range(70)] for j in range(41)]
    for i in range(41):
        for j in range(70):
            la[i][j] = ord(landscape[i][j]) - 96
            ingroup[i][j] = -1
            if landscape[i][j] == 'S':
                start = [i, j]
                la[i][j] = 1
            if landscape[i][j] == 'E':
                end = [i, j]
                la[i][j] = 26
    # gprint(ingroup)
    groups = {0: [[0, 0]]}

    for i in range(41):
        for j in range(70):

            if ingroup[i][j] == -1:
                if i == 0 and j == 0:
                    ingroup[i][j] = 0
                    a = 0
                    ingroup, groups = expandgroup(i, j, la, ingroup, groups, a)
                else:
                    a = len(groups)
                    ingroup[i][j] = a
                    groups[a] = [[i, j]]
                    ingroup, groups = expandgroup(i, j, la, ingroup, groups, a)
                    #print(groups)

    gprint(ingroup)


    # print(groups, '-----')
    # gprint(ingroup)


if __name__ == '__main__':
    main()
