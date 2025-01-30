import math
import heapq
import random
import numpy as np
from PIL import Image


def nu_frag(a, b, flag_r, seed):
    filled = [[0 for _ in range(b)] for _ in range(a)]
    squares = []
    min_heap = []

    if seed != -1:
        random.seed(seed)

    heapq.heappush(min_heap, (0, (0,0)))
    count = 0

    while min_heap :
        q = heapq.heappop(min_heap)
        # print("AAA: ", q)
        x1, y1 = q[1]
        bound = min(a-x1, b-y1)
        for i in range(0, bound):
            if filled[x1+i][y1] == 1:
                bound = i
                break

        if flag_r == 0:
            r = random.randint(min(25, bound * bound), bound * bound)
            k1 = bound + 1 - math.floor(math.sqrt(r))
            k1 = min(k1, 35)
            if y1 == 0:
                k1 = min(k1, 10)
                k1 = random.randint(1, k1)

            k1 = min(k1, 25)

        elif flag_r == 1:
            r = random.randint(1, bound*bound)
            k1 = bound+1-math.floor(math.sqrt(r))

        elif flag_r == 2:
            r = random.randint(min(25, bound*bound), bound*bound)
            k1 = bound+1-math.floor(math.sqrt(r))

        elif flag_r == 3:
            r = random.randint(1, bound*bound)
            k1 = bound+1-math.floor(math.sqrt(r))
            if y1 == 0:
                k1 = min(k1, 10)
                k1 = random.randint(1, k1)

        else:
            k1 = random.randint(1, bound)

        if y1+k1<b and (x1 == 0 or filled[x1-1][y1+k1] == 1):
            heapq.heappush(min_heap, (y1+k1-x1, (x1, y1+k1)))

        if x1+k1 < a:
            for i in range(k1):
                if filled[x1+k1][y1+i] == 0:
                    heapq.heappush(min_heap, (y1+i-x1-k1, (x1+k1, y1+i)))
                    break

        squares.append((x1,y1,k1, count))
        count += 1
        for i in range(k1):
            for j in range(k1):
                filled[x1+i][y1+j]  = 1
        # print(x1,y1,k1)
    return squares

def sq_print(squares,a,b):
    save_path =  "batch3/doc5.bmp"
    out = [[[0 for _ in range(3)] for _ in range(b)] for  _ in range(a)]
    print("filled:")
    red = 0
    gre = 0
    blu = 0
    for s in squares:
        x,y,k,n = s
        red = random.randint(0,255)
        gre = random.randint(0,255)
        blu = random.randint(0,255)

        # red = (red + 25) % 256
        for i in range(k):
            for j in range(k):
                out[x + i][y + j][0] = red
                out[x + i][y + j][1] = gre
                out[x + i][y + j][2] = blu
    out = np.array(out)
    Image.fromarray(out.astype('uint8'),mode='RGB').save(save_path)


# a = 78
# b = 78
# A = nu_frag(a,b,3,-1)
# print(A)
# sq_print(A)
#





