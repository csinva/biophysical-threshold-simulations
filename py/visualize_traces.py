from py_util import config, load
from py_util.config import *
import matplotlib.pyplot as plt

filename = path_to_data + 'traces/3_stoch_1.00000_v.dat'

data = load.load_dict(filename)
print(data.keys())
# plt.plot(data['t'], data['soma_km'])
# plt.plot(data['t'], data['k9'])
# plt.plot(data['t'], data['k1'])
# plt.plot(data['t'], data['soma_kca'])
plt.plot(data['t'], data['ik0_s'])

plt.xlim(data['delay'], plt.xlim()[1])
plt.show()
