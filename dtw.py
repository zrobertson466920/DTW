import numpy as np

# sim is a matrix where the elements are measures of distance or (dis)-similarity
# between the i-th and j-th elements of the list being compared
def sim_to_path(sim):

    ylen = np.size(sim,axis = 0)
    xlen = np.size(sim,axis = 1)

    dist = np.arange(xlen*ylen).reshape((ylen,xlen))
    pred = [[0 for xx in range(xlen)] for yx in range(ylen)]
    dist[0][0] = sim[0][0]

    for y in range(ylen):
        for x in range(xlen):

            if (x == 0) & (y == 0):
                continue

            val = []
            if 0 <= y-1 < ylen:
                val.append(((y-1,x),dist[y-1][x]+sim[y][x]))
            if (0 <= (y-1) < ylen) & (0 <= (x-1) < xlen):
                val.append(((y-1,x-1),dist[y-1][x-1]+sim[y][x]))
            if 0 <= (x-1) < xlen:
                val.append(((y,x-1),dist[y][x-1]+sim[y][x]))

            val.sort(key=lambda nd: nd[1])

            dist[y][x] = val[0][1]
            pred[y][x] = val[0][0]

    path = []
    pos = (ylen-1,xlen-1)

    while pos != (0,0):
        path.append(pos)
        pos = pred[pos[0]][pos[1]]

    return dist, reversed(path)
