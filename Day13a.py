import ast


def depth(li):
    i = 0
    if li:
        while li and type(li) is list:
            i += 1
            li = li[0]
    return i


def leveldown(lev):
    levr = []
    resolved = 0
    if lev[0]:
        if type(lev[0]) is int:
            resolved = 1
            levr = lev
        else:
            levr = lev[0]
            if type(levr[0]) is int:
                resolved = 1
    else:
        resolved = 1
    return levr, resolved


def compare(l, r):
    if not l and not r:
        return -1
    if l and not r:
        return 0
    elif r and not l:
        return 1
    elif l and r:
        if (type(l[0]) is int) and (type(r[0]) is int):
            for i in range(min(len(l), len(r))):
                try:
                    if l[i] < r[i]:
                        return 1
                    elif l[i] > r[i]:
                        return 0
                    elif l[i] == r[i]:
                        continue
                except:
                    return -1
            if len(r) > len(l):
                return 1
            if len(l) > len(r):
                return 0
            else:
                if (type(l[0]) is int) and (type(r[0]) is list):
                    rr = r
                    while type(rr[0]) is list:
                        rr = rr[0]
                    for j in l:




def main():
    f = open('Day13.txt')
    comps = f.readlines()
    f.close()

    for i in range(150):
        l = eval(comps[i * 3])
        r = eval(comps[i * 3 + 1])
        m = depth(l)
        n = depth(r)
        o = min(m,n)
        print(l)
        print(r)
        print('ldepth:', depth(l))
        print('l' + '[0]' * (o - 1))
        l1 = eval('l' + '[0]' * (o - 1))
        print('rdepth:', depth(r))
        print('r' + '[0]' * (o - 1))
        r1 = eval('r' + '[0]' * (o - 1))
        print('l1:', l1)
        print('r1:', r1)

        ordered = compare(l1, r1)
        print('Pair ' + str(i + 1) + ':', ordered)


        # o = min(m, n)
        # bl = len(l)
        # br = len(r)
        # for i in range(max(bl,br)):
        #     ordered = compare(l,r)
        #     print('pair', str(i) + ':', ordered)
            # if ordered == -1:
            #     for j in range
        # if bl == 0:
        #     ordered = 1
        # elif br == 1:
        #     ordered = 0
        # else:
        #     for j in range(max(bl,br)):



        # llevel = 0
        # rlevel = 0
        # resolved = 0
        # ll = l
        # rr = r
        # while resolved == 0:
        #     if l:
        #         ll, resolved = leveldown(ll)
        #     else:
        #         resolved = 1
        #     llevel = llevel + 1
        # resolved = 0
        # while resolved == 0:
        #     if r:
        #         rr, resolved = leveldown(rr)
        #     else:
        #         resolved = 1
        #     rlevel = rlevel + 1

        # print(ll,rr,llevel,rlevel)
        # for i in range(max(bl, br)):
        # print(l)
        # print(r)
        # ordered = compare(ll, rr)
        # print('Pair ' + str(i + 1) + ':', ordered)


if __name__ == '__main__':
    main()

# print('l:', l, l[0])
        # print(depth(l))
        # l1 = eval('l' + '[0]' * o)
        # print('r:', r)
        # print(depth(r))
        # r1 = eval('r' + '[0]' * o)
        # print('l1:', l1)
        # print('r1:', r1)