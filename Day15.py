import re
import timeit
from itertools import islice
import collections

# def cant_be_beacon(x, y, x_s, y_s, dist):
#
#     return impossible_beacon




def x_at_distance(x_s,y_s,dist,y): # farthest right x at specified y at distance
    x = x_s + dist - abs(y - y_s)
    return x


def distance(x1, y1, x2, y2):
    return (abs(x2 - x1) + abs(y2 - y1))


def main():

    f = open('Day15.txt')
    beacons = f.readlines()
    f.close()

    x_s = [] # sensor x range: 157988 3999769
    y_s = [] # sensor y range: 257848 3985671
    x_b = [] # beacon x range: -1236383 3691788
    y_b = [] # beacon y range: -741777 3218536
    dist = []
    diamonds = {}
    j = 0
    for i in beacons:
        b_pos = re.findall(r'(\-*\d+), y=(\-*\d+): c.+=(\-*\d+), y=(\-*\d+)', i)
        x_s.append(int(b_pos[0][0]))
        y_s.append(int(b_pos[0][1]))
        x_b.append(int(b_pos[0][2]))
        y_b.append(int(b_pos[0][3]))
        dist.append(distance(x_s[j], y_s[j], x_b[j], y_b[j]))
        j += 1

    s = []
    items = range(4000001)
    starttime = timeit.default_timer()
    for i in items:
        pass
    print("Time :", timeit.default_timer() - starttime)
        # for j in range(len(beacons)):
        #     s.append(tuple([x_s[j] + (dist[j] - abs(i - y_s[j])), x_s[j] - (dist[j] - abs(i - y_s[j]))]))
        # diamonds[i] = s
    answer = -1
    i_s = iter(range(0, 4000001))
    starttime = timeit.default_timer()
    for i in i_s:
        for j in range(len(beacons)):
            if distance(i, 2000000, x_s[j], y_s[j]) <= dist[j]:
                next_x = x_at_distance(x_s[j], y_s[j], dist[j], 2000000)
                skip_n = next_x - i
                next(islice(i_s, skip_n, skip_n), None)
                answer += skip_n + 1
                break
    print(answer)
    print("Time :", timeit.default_timer() - starttime)


if __name__ == '__main__':
    main()
    # 74.380
    # 3.975

    #--- 0-4mil:
    .056796

    #--- iter only


    # for i in i_s:
    #     for j in range(len(beacons)):
    #         if distance(i, 2000000, x_s[j], y_s[j]) <= dist[j]:
    #             next_x = x_at_distance(x_s[j], y_s[j], dist[j], 2000000)
    #             skip_n = next_x - i
    #             next(islice(i_s, skip_n, skip_n), None)
    #             answer += skip_n + 1
    #             break