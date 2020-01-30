import math
import collections

if __name__ == "__main__":
    a_map = open("10.dat", "r").readlines()
    a_map = list(map(lambda s: s.strip(), a_map))
    a_map = list(map(list, a_map))
    w = len(a_map[0])
    h = len(a_map)
    m = 0
    m_c = None
    for o_y in range(w):
        for o_x in range(h):
            if a_map[o_y][o_x] == ".":
                continue
            sl = set()
            for s_y in range(w):
                for s_x in range(h):
                    if s_y == o_y and s_x == o_x:
                        continue
                    if a_map[s_y][s_x] == ".":
                        continue
                    dy = s_y - o_y
                    dx = s_x - o_x
                    g = math.gcd(dx, dy)
                    dy = int(dy / g)
                    dx = int(dx / g)
                    sl.add((dx, dy))
                    #print(f"{(o_x, o_y)} {(s_x, s_y)} {(dx, dy)}")
            if len(sl) > m:
                m = len(sl)
                m_c = (o_x, o_y)
            #print(f"{(o_x, o_y)} {len(sl)}")
    print(m)
    print(m_c)
    o_x, o_y = m_c
    s_map = {}
    for s_y in range(w):
        for s_x in range(h):
            if s_y == o_y and s_x == o_x:
                continue
            if a_map[s_y][s_x] == ".":
                continue
            dy = s_y - o_y
            dx = s_x - o_x
            g = math.gcd(dx, dy)
            dy = int(dy / g)
            dx = int(dx / g)

            dr = (math.atan2(dy, dx) * 180/math.pi + 90) % 360
            if dr not in s_map:
                s_map[dr] = []
            s_map[dr].append((s_x - o_x, s_y - o_y))

    i = 1
    for item in sorted(s_map.items()):
        dr = item[0]
        a_l = item[1]
        dists = list(map(lambda a: ((a[0] ** 2 + a[1] ** 2) ** 0.5, a), a_l))

        m_a = min(dists)
        a_l.remove(m_a[1])
        coords = (m_a[1][0] + o_x, m_a[1][1] + o_y)
        print(f"{i} {coords} {dr} {m_a}")
        i += 1
