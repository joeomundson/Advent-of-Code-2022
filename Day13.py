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

def compareint(l, r):
    if l > r:
        return 0
    elif l < r:
        return 1
    else:
        return -1


def compare(l, r):
    if (type(l) is int) and (type(r) is int):
        return compareint(l, r)
    elif (type(l) is int) and (type(r) is list):
        return compare([l], r)
    elif (type(l) is list) and (type(r) is int):
        return compare(l, [r])
    elif (type(l) is list) and (type(r) is list):
        for ll, rr in zip(l, r):
            ordered = compare(ll, rr)
            if ordered != -1:
                return ordered
        return compare(len(l),len(r))


def main():
    f = open('Day13.txt')
    comps = f.readlines()
    f.close()

    lines = []
    j = 0
    for i in comps:
        if i !='\n':
            lines.append(eval(i))
            j+=1
    out_lines = [[[2]], [[6]]]
    for line in lines:
        out_index = 0
        for out_line in out_lines:
            if compare(line, out_line):
                break
            else:
                out_index += 1
        out_lines.insert(out_index,line)
    code_1 = out_lines.index([[2]]) + 1
    code_2 = out_lines.index([[6]]) + 1
    print('Answer =', code_1 * code_2)

    #     l = eval(comps[i * 3])
    #     r = eval(comps[i * 3 + 1])
    #     print(compare(l,r))
    #     if compare(l, r):
    #         answer += i + 1
    # print('answer =', answer)



if __name__ == '__main__':
    main()