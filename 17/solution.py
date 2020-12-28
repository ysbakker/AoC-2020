def neighbors(cubes, z, y, x, w):
    c = 0
    for dw in (-1, 0, 1):
        for dz in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dz == dy == dx == dw == 0: continue
                    if (z + dz, y + dy, x + dx, w + dw) in cubes:
                        c += 1
    return c


def grow(part, bounds, z, y, x, w):
    bounds[0][0] = min(z - 1, bounds[0][0])
    bounds[0][1] = max(z + 1, bounds[0][1])
    bounds[1][0] = min(y - 1, bounds[1][0])
    bounds[1][1] = max(y + 1, bounds[1][1])
    bounds[2][0] = min(x - 1, bounds[2][0])
    bounds[2][1] = max(x + 1, bounds[2][1])
    if part == 2:
        bounds[3][0] = min(w - 1, bounds[3][0])
        bounds[3][1] = max(w + 1, bounds[3][1])


def solve(part, inp):
    cubes = set()
    bounds = ([-1, 1], [0, 0], [0, 0], [0, 0])  # z,y,x,w -> (min, max)
    if part == 2:
        bounds[3][0] = -1
        bounds[3][1] = 1

    for y, yv in enumerate(inp.split('\n')):
        for x, xv in enumerate(yv):
            if xv == '#':
                cubes.add((0, y, x, 0))
                bounds[1][0] = min(y - 1, bounds[1][0])
                bounds[1][1] = max(y + 1, bounds[1][1])
                bounds[2][0] = min(x - 1, bounds[2][0])
                bounds[2][1] = max(x + 1, bounds[2][1])

    for _ in range(6):
        pcubes = cubes.copy()
        for w in range(bounds[3][0], bounds[3][1] + 1):
            for z in range(bounds[0][0], bounds[0][1] + 1):
                for y in range(bounds[1][0], bounds[1][1] + 1):
                    for x in range(bounds[2][0], bounds[2][1] + 1):
                        nb = neighbors(pcubes, z, y, x, w)
                        cur = (z, y, x, w)
                        if nb == 3 and cur not in pcubes:
                            cubes.add(cur)
                            grow(part, bounds, z, y, x, w)
                        if nb not in (2, 3) and cur in pcubes:
                            cubes.discard(cur)
    print(len(cubes))


with open('17/input') as f:
    inp = f.read().strip()
    solve(1, inp)
    solve(2, inp)