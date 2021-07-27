from numpy.core.fromnumeric import squeeze
from scipy import io
import numpy as np
# savemat(filename, mdict, do_compression)
# loadmat(filename)
arr = np.arange(10)
# Export
io.savemat('arr.mat', {"vec": arr})
# Import
mydata = io.loadmat('arr.mat')
print(mydata)
print(mydata['vec'])
mydata = io.loadmat('arr.mat', squeeze_me=True)
print(mydata['vec'])