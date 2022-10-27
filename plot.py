import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio




#dect = {'mapi2t_list': mapi2t_list, 'mapt2i_list': mapt2i_list, 'LossI2T_list': LossI2T_list,
#                'LossT2I_list': LossT2I_list}


result = np.load('./plot.npz')
mapi2t = result['mapi2t_list'] # image query
mapt2i = result['mapt2i_list'] # text query
lossi2t = result['LossI2T_list'] # image retrieval
losst2i = result['LossT2I_list'] # text retrieval

x1 = range(0, 50)
x2 = range(0, 50)
y1 = lossi2t
y2 = mapi2t
plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'o-')
plt.title('Test accuracy Vs. epoches')
plt.ylabel('Test accsracy')
plt.subplot(2, 1, 2)
plt.plot(x2, y2, '.-')
plt.xlabel('Test loss vs. epoches')
plt.savefig('map.png')