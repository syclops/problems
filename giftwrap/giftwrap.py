import fileinput
import math

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (r[1] - q[1]) * (q[0] - p[0])
    if val == 0:
        return val
    else:
        return -val / abs(val)

def closer(ref, cand1, cand2):
    dist1 =  math.sqrt((cand1[0] - ref[0])**2 + (cand1[1] - ref[1])**2)
    dist2 =  math.sqrt((cand2[0] - ref[0])**2 + (cand2[1] - ref[1])**2)
    return dist1 < dist2

def giftwrap(pts):
    min_pt = pts[0]
    for pt in pts:
        if pt[0] <= min_pt[0] and pt[1] <= min_pt[1]:
            min_pt = pt
    hull = [min_pt]
    while len(hull) == 1 or hull[0] != hull[-1]:
        cur_pt = hull[-1]
        next_pt = pts[0]
        for pt in pts:
            if next_pt == pt or cur_pt == pt:
                continue
            elif cur_pt == next_pt:
                next_pt = pt
            elif orientation(cur_pt, next_pt, pt) == 1:
                next_pt = pt
            elif orientation(cur_pt, next_pt, pt) == 0 and closer(cur_pt, pt,
                                                                  next_pt):
                next_pt = pt
        hull.append(next_pt)
        pts.remove(next_pt)
    return hull[:-1]

def main():
    pts = []
    for line in fileinput.input():
        [x, y] = map(int, line.strip().split())
        pts.append((x, y))
    hull = giftwrap(pts)
    for pt in hull:
        print('{} {}'.format(pt[0], pt[1]))

if __name__ == '__main__':
    main()
