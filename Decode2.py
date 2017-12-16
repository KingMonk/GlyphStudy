import os, json


def reorder(orig: list):
    temp = str(orig[0]) + ','
    temp = temp + str(orig[1]) + ','
    temp = temp + str(orig[2]) + ','
    temp = temp + str(orig[3]) + ','
    temp = temp + str(orig[6]) + ','
    temp = temp + str(orig[4]) + ','
    temp = temp + str(orig[5]) + ','
    temp = temp + str(orig[7]) + ','
    temp = temp + str(orig[10]) + ','
    temp = temp + str(orig[8]) + ','
    temp = temp + str(orig[9]) + ','
    temp = temp + str(orig[11]) + ','
    temp = temp + str(orig[14]) + ','
    temp = temp + str(orig[12]) + ','
    temp = temp + str(orig[13]) + ','
    temp = temp + str(orig[15]) + ','
    temp = temp + str(orig[18]) + ','
    temp = temp + str(orig[16]) + ','
    temp = temp + str(orig[17]) + ','
    temp = temp + str(orig[19]) + ','
    temp = temp + str(orig[22]) + ','
    temp = temp + str(orig[20]) + ','
    temp = temp + str(orig[21]) + ','
    temp = temp + str(orig[23]) + ','
    temp = temp + str(orig[26]) + ','
    temp = temp + str(orig[24]) + ','
    temp = temp + str(orig[25]) + ','
    temp = temp + str(orig[27]) + ','
    temp = temp + str(orig[30]) + ','
    temp = temp + str(orig[28]) + ','
    temp = temp + str(orig[29]) + ','
    temp = temp + str(orig[31]) + ','
    temp = temp + str(orig[32]) + ','
    temp = temp + str(orig[33]) + ','
    temp = temp + str(orig[34]) + ','
    temp = temp + str(orig[35]) + ','
    return temp

def _launch():
    cwd = os.getcwd()
    file = os.path.join(cwd, 'obelisk.json')

    data = json.load(open(file))
    state = 'IDX,'

    for idx in range(0, 36):
        state = state + 'T' + str(idx) + ','

    for idx in range(0, 36):
        state = state + 'M' + str(idx) + ','

    for idx in range(0, 36):
        state = state + 'B' + str(idx) + ','

    state = state + '\n'

    for idx, one_state in enumerate(data):
        state = state + str(idx) + ','
        state = state + reorder(one_state['triangles']['top'])
        state = state + reorder(one_state['triangles']['middle'])
        state = state + reorder(one_state['triangles']['bottom'])
        state = state + '\n'

    csv_file = os.path.join(cwd, 'Full_Glyph_States') + '.csv'

    with open(csv_file, mode='w') as fl:
        fl.write(state)

    return


if __name__ == '__main__':
    _launch()