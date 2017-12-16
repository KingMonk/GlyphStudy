import os
import json

cwd = os.getcwd()

file = os.path.join(cwd, 'obelisk.json')

data = json.load(open(file))

glyphs = list()

for one_state in data:
    top = one_state['triangles']['top']
    middle = one_state['triangles']['middle']
    bottom = one_state['triangles']['bottom']
    if top not in glyphs:
        glyphs.append(top)
    if middle not in glyphs:
        glyphs.append(middle)
    if bottom not in glyphs:
        glyphs.append(bottom)

print('Total glyphs = ' + str(len(glyphs)))


def total_diff(occ: list, ord: list):
    diffr = 0

    for idx in range(0, 36):
        if occ[idx] != ord[idx]:
            diffr = diffr + 1

    return diffr


def to_int(values: list):
    value = 0
    for idx in range(0, 36):
        value = value + (values[idx] * pow(2, 35 - idx))

    return value


hdr = list(range(0, 36))
bin_csv = ',' + ','.join(str(x) for x in hdr) + ',\n'

for idx, glyph in enumerate(glyphs):
    bin_csv = bin_csv + str(idx) + ',' + ','.join(str(x) for x in glyph) + ',\n'

csv_file = os.path.join(cwd, 'Glyphs') + '.csv'

with open(csv_file, mode='w') as fl:
    fl.write(bin_csv)

for glyph in glyphs:
    glyph.append(to_int(glyph))

ordered = list()

while len(glyphs) > 1:
    single = glyphs[0]
    for glyph in glyphs:
        if glyph[-1] < single[-1]:
            single = glyph
    glyphs.remove(single)
    ordered.append(single)

ordered.append(glyphs[0])

seth = True

hdr = list(range(0, 36))
bin_csv = ',' + ','.join(str(x) for x in hdr) + ',\n'

for idx, glyph in enumerate(ordered):
    glyph.pop(-1)
    bin_csv = bin_csv + str(idx) + ',' + ','.join(str(x) for x in glyph) + ',\n'

csv_file = os.path.join(cwd, 'Ordered') + '.csv'

with open(csv_file, mode='w') as fl:
    fl.write(bin_csv)


def find_index(lst: list):
    for idx, glyph in enumerate(ordered):
        if lst == glyph:
            return idx
    return None

glyph_list = list()


def are_equal(first: list, next: list):
    if first == next:
        return True
    else:
        return False


for frame in data:
    top = find_index(frame['triangles']['top'])
    middle = find_index(frame['triangles']['middle'])
    bottom = find_index(frame['triangles']['bottom'])
    glyph_list.append([0, top, middle, bottom])

for idx, thing in enumerate(glyph_list):
    next = idx + 1
    if next < len(glyph_list):
        if are_equal(thing[1:], glyph_list[idx + 1][1:]):
            glyph_list[idx + 1][0] = thing[0] + 1

for thing in glyph_list:
    thing[0] = thing[0] + 1

bin_csv = 'Count,Top,Middle,Bottom,\n'

for idx, glyph in enumerate(glyph_list):
    bin_csv = bin_csv + ','.join(str(x) for x in glyph) + ',\n'

csv_file = os.path.join(cwd, 'State_Count') + '.csv'

with open(csv_file, mode='w') as fl:
    fl.write(bin_csv)

glyph_count = list()

for idx in range(0, 122):
    glyph_count.append([idx, 0])

for glyph in glyph_list[:][1:]:
    glyph_count[glyph[1]][1] = glyph_count[glyph[1]][1] + 1
    glyph_count[glyph[2]][1] = glyph_count[glyph[2]][1] + 1
    glyph_count[glyph[3]][1] = glyph_count[glyph[3]][1] + 1

bin_csv = 'Glyph,Count,\n'

for idx, glyph in enumerate(glyph_count):
    bin_csv = bin_csv + ','.join(str(x) for x in glyph) + ',\n'

csv_file = os.path.join(cwd, 'Glyph_Count') + '.csv'

with open(csv_file, mode='w') as fl:
    fl.write(bin_csv)

glyph_state_count = list()

for idx in range(0, 122):
    glyph_state_count.append([idx, 0, 0, 0])

for glyph in glyph_list[:][1:]:
    glyph_state_count[glyph[1]][1] = glyph_state_count[glyph[1]][1] + 1
    glyph_state_count[glyph[2]][2] = glyph_state_count[glyph[2]][2] + 1
    glyph_state_count[glyph[3]][3] = glyph_state_count[glyph[3]][3] + 1

bin_csv = 'Glyph,Count,,,\n'

for idx, glyph in enumerate(glyph_state_count):
    bin_csv = bin_csv + ','.join(str(x) for x in glyph) + ',\n'

csv_file = os.path.join(cwd, 'Glyph_State_Count') + '.csv'

with open(csv_file, mode='w') as fl:
    fl.write(bin_csv)


seth = True
