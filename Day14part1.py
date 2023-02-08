import re
import subprocess

def gprint(array):
    for i in array:
        print(i[420:510])

def sand_simulator(grid):
    sand_pos = 0
    n = 0
    while sand_pos < 160:
        n += 1
        print('particle', n)
        x_sand = 500
        y_sand = 0
        resting = 0
        while resting == 0:
            if grid[y_sand + 1][x_sand] == '.':
                y_sand += 1
                continue
            elif grid[y_sand + 1][x_sand - 1] == '.':
                y_sand += 1
                x_sand -= 1
                continue
            elif grid[y_sand + 1][x_sand + 1] == '.':
                y_sand += 1
                x_sand += 1
                continue
            else:
                grid[y_sand][x_sand] = 'o'
                resting = 1
                sand_pos = y_sand
    return n - 1, grid



def rocks_on_grid(rock_points, grid):
    grid[0][500] = 'v'
    for i in rock_points:
        x = i[0]
        y = i[1]
        grid[y][x] = '#'
    return grid

def draw_rocks(x_y, grid):
    rock_points = []
    for i in x_y:
        r = x_y[i]
        j = 0
        for xy in r:
            x = xy[0]
            y = xy[1]
            if j == 0:
                rock_points.append(xy)
            else:
                xy_inc = last_xy
                if x == last_xy[0]:
                    y_sign = int((y - last_xy[1]) / abs((y - last_xy[1])))
                    while xy_inc != xy:
                        xy_inc = (xy_inc[0], xy_inc[1] + y_sign)
                        rock_points.append(xy_inc)
                else:
                    x_sign = int((x - last_xy[0]) / abs((x - last_xy[0])))
                    while xy_inc != xy:
                        xy_inc = (xy_inc[0] + x_sign, xy_inc[1])
                        rock_points.append(xy_inc)
            last_xy = xy
            j += 1
    return rocks_on_grid(rock_points, grid)

def main():
    f = open('Day14.txt')
    rocks = f.readlines() # x: 426 506, y: 13 158
    f.close()

    x_y = {}
    i = 0
    for r in rocks:
        x_strings = re.findall(r'(\d+),', r)
        x = list(map(int, x_strings))
        y_strings = re.findall(r',(\d+)', r)
        y = list(map(int, y_strings))
        x_y[i] = list(zip(x,y))
        i += 1
    x_y[i] = [(420, 165), (510, 165)]
    grid = [['.' for i in range(600)] for j in range(166)]
    grid_rocks = draw_rocks(x_y, grid)
    # gprint(grid_rocks)
    sand, grid = sand_simulator(grid_rocks)
    print(sand)
    gprint(grid)



if __name__ == '__main__':
    main()