from math import floor

w, h = [int(i) for i in input().split()]
n = int(input())
x0, y0 = [int(i) for i in input().split()]

interval_x, interval_y = [0, w-1], [0, h-1]

op = ''
count = 0
NBRE = 0

while True:
    bomb_dir = input().lower()

    if len(set(['u','d']).intersection(bomb_dir)) > 0:
        if 'u' in bomb_dir:
            interval_y = [interval_y[0], y0-1]
        else:
           interval_y = [y0+1,interval_y[1]]
        median = sum(interval_y)/2
        y0 = floor(median)

    if len(set(['l','r']).intersection(bomb_dir)) > 0:
        if 'l' in bomb_dir:
            interval_x = [interval_x[0], x0-1]
        else:
           interval_x = [x0+1,interval_x[1]]
        median = sum(interval_x)/2
        x0 = floor(median)

    print(f'{x0} {y0}')
    op = bomb_dir
    


