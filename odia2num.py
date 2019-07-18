ODIA_NUM_DICT = {
    '୦': '0',
    '୧': '1',
    '୨': '2',
    '୩': '3',
    '୪': '4',
    '୫': '5',
    '୬': '6',
    '୭': '7',
    '୮': '8',
    '୯': '9',
}

def convert(odia_num):

    o = ""

    for s in odia_num:
        if (s == ','):
            pass
        elif (s not in ODIA_NUM_DICT):
            return None
        else:
            o += ODIA_NUM_DICT[s]
    o = int(o)
    return o
