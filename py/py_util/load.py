import numpy as np
import os
from .config import *


def load_dict(filename):
    f = open(filename, 'r')
    headers = f.readline().split()
    delay = float(f.readline().split()[1])
    intensity = float(f.readline().split()[1])
    dur = float(f.readline().split()[1])
    rows, cols = f.readline().split()
    rows, cols = int(rows), int(cols)
    mat = np.zeros((rows, cols))
    row = 0
    for line in f:
        mat[row, :] = line.split()
        row += 1
    data = {}

    data_chans = {}
    try:
        data_chans = load_dict_chans(filename)
    except:
        pass
    for key in data_chans:
        data[key] = data_chans[key]

    for i in range(len(headers)):
        data[headers[i]] = mat[:, i]
    data['delay'] = delay
    data['intensity'] = intensity
    data['dur'] = dur
    return data


# only for use above
def load_dict_chans(filename):
    f = open(filename[:-5] + 'chans.dat', 'r')
    headers = f.readline().split()
    dt, delay = f.readline().split()
    rows, cols = f.readline().split()
    rows, cols = int(rows), int(cols)
    mat = np.zeros((rows, cols))
    row = 0
    for line in f:
        mat[row, :] = line.split()
        row += 1
    data_chans = {}
    for i in range(len(headers)):
        data_chans[headers[i]] = mat[:, i]
    return data_chans
