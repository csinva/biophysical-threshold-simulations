import os
import os.path
from py_util.config import *
from py_util import config, load
import numpy as np
import csv


def thresh_stats(dir, thresh_def=0):
    print("calculating threshes...")
    # calc threshes
    threshes = {}
    for fname in os.listdir(dir):
        if fname.endswith('v.dat'):
            data = load.load_dict(os.path.join(dir, fname))
            v = data['ais9']
            intensity = data['intensity']
            if max(v) < 0:  # didn't fire
                if not intensity in threshes:
                    threshes[intensity] = []
                threshes[intensity].append(max(v))
    for intensity in threshes:
        threshes[intensity] = np.median(threshes[intensity])
    print('\tthreshes:', threshes)

    # save out data
    print("saving data...")
    key_list = sorted(data.keys())
    key_list.remove('intensity')
    key_list.remove('delay')
    key_list.remove('dur')
    headers = ['intensity', 'thresh', 'delay', 'dur'] + key_list

    outname = '/thresh_stats.csv'
    if not thresh_def == 0:
        outname = '/thresh_stats_' + thresh_def + '.csv'
    with open(dir + outname, 'w') as f_out:
        writer = csv.writer(f_out, delimiter=",")
        writer.writerow(headers)
        for fname in os.listdir(dir):
            if fname.endswith('v.dat'):
                data = load.load_dict(os.path.join(dir, fname))
                v = data['ais9']
                thresh = threshes[data['intensity']]
                arg = 0
                if max(v) > 0:
                    arg = calc_arg(data['t'], v, thresh, thresh_def)
                if max(v) < 0:
                    arg = np.argmax(v)
                vals = []
                for key in key_list:
                    vals.append(data[key][arg])
                vals = [data['intensity'], thresh, data['delay'], data['dur']] + vals
                writer.writerow(vals)


def calc_arg(t, v, thresh, thresh_def):
    if thresh_def == 0:
        for i in range(len(v)):
            if v[i] >= thresh:
                arg = i
                break
    elif thresh_def == 'max':
        arg = np.argmax(v)
    elif thresh_def == 'deriv1':
        v1 = list(v)
        dt = t[-1] - t[-2]
        for i in range(3, len(v) - 4):
            v1[i] = (v[i-2] - 8*v[i-1] + 8*v[i+1]-v[i+2]) / (12*dt)
        arg = np.argmax(v1)
    elif thresh_def == 'deriv2':
        v2 = list(v)
        dt = t[-1] - t[-2]
        for i in range(3, len(v) - 4):
            v2[i] = (-v[i - 2] + 16 * v[i - 1] - 30 * v[i] + 16 * v[i + 1] - v[i + 2]) / (12 * dt * dt)
        arg = np.argmax(v2)
    elif thresh_def == 'deriv3':
        v3 = list(v)
        dt = t[-1] - t[-2]
        for i in range(3, len(v) - 4):
            v3[i] = (v[i - 3] - 8 * v[i - 2] + 13 * v[i - 1] - 13 * v[i + 1] + 8 * v[i + 2] - v[i + 3]) / (
                8 * dt * dt * dt)
        arg = np.argmax(v3)
    return arg


# folder = 'Jul_02_15:39:57_simple_titrate'
folder = 'May_19_14:39:12_0.7nA_1000_traces'
dir = path_to_data + 'traces/' + folder
print('threshold voltage def')
thresh_stats(dir)
print('max voltage def')
thresh_stats(dir, thresh_def='max')
print('deriv1 def')
thresh_stats(dir, thresh_def='deriv1')
print('deriv2 def')
thresh_stats(dir, thresh_def='deriv2')
print('deriv3 def')
thresh_stats(dir, thresh_def='deriv3')
