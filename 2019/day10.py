from util import Day


def process_map(data):
    out_data = set()
    for i, el in enumerate(data):
        for j, val in enumerate(el.strip()):
            if val == "#":
                out_data.add((j, i))
    return out_data


def all_shadows(data, center, asteroids):

    masks = set()
    cx, cy = center

    x, y = zip(*data)
    max_x, max_y = max(x), max(y)

    for asteroid in asteroids:
        ox, oy = asteroid

        if center == asteroid:
            masks.add((cx, cy))
        else:
            ix, iy = ox - cx, oy - cy

            # Find the smallest vector
            for ii in range(10, 1, -1):
                if ix % ii == 0 and iy % ii == 0:
                    ix = ix // ii
                    iy = iy // ii

            dx = ox + ix
            dy = oy + iy

            while 0 <= dx <= max_x and 0 <= dy <= max_y:
                if (dx, dy) in data:
                    masks.add((dx, dy))
                dx += ix
                dy += iy

    return data - masks


def count_visible(data):

    star_map = {}

    for asteroid in data:
        star_map[asteroid] = len(all_shadows(data, asteroid, data))

    new_base = max(star_map, key=star_map.get)

    return star_map[new_base], new_base, star_map


def wazer_wifle(data, center, num):
    from math import atan2

    cx, cy = center
    seen = all_shadows(data, center, data)

    return sorted(((atan2((x - cx), (y - cy)), (x, y)) for x, y in seen), reverse=True)[num - 1][1]
    # First try
    # rotate = [(x, 0) for x in range(cx, max_x)] # center x out at y=0
    # rotate.extend([(max_x-1, y) for y in range(1,max_y)]) # down y
    # rotate.extend([(x, max_y-1) for x in range(max_x-2, -1, -1)]) # back in x
    # rotate.extend([(0, y) for y in range(max_y-2, -1, -1)]) # up y
    # rotate.extend([(x,0) for x in range(1, cx)]) # back to start

    # Nice idea, if it sampled everything. Let's go polar!

