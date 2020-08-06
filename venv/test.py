import numpy as np

with open("./arranged_dataset/drive01/drive01m.mat") as file:
    for line in file:
        for digit in line.split():
            print(float(digit))

import scipy.io
import  numpy as np
data = scipy.io.loadmat('./arranged_dataset/drive01/drive01m.mat')
for i in data:
	if '__' not in i and 'readme' not in i:
		np.savetxt(("./"+i+".csv"),data[i],delimiter=',')
