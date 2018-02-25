import os
from py_util.config import *
import csv
import operator


def combine_dir(dir):
    with open(dir + 'durs.csv', 'w') as f_out:
        f_out.write('intensity,target,spike_count,spike_target\n')
        for fname in os.listdir(dir):
            if fname.endswith('.out'):
                with open(dir + fname) as f:
                    lines = f.readlines()
                    f_out.write(lines[1])


def sort_csv(dir):
    fname = dir + 'durs.csv'
    with open(fname) as f:
        print(fname)
    reader = csv.reader(open(fname), delimiter=",")
    sortedlist = sorted(reader, key=operator.itemgetter(0))
    fname_out = dir + 'durs_sorted.csv'
    with open(fname_out, 'w') as f_out:
        writer = csv.writer(f_out, delimiter=",")
        writer.writerows(sortedlist)


dir = path_to_data + 'titrate/'
combine_dir(dir)
sort_csv(dir)
os.system('rm ' + dir + '/*.out')
