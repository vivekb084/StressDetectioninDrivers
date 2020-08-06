15# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 14:18:58 2020

@author: Vivek Bindal
"""



from sklearn import svm
import numpy as np
#import pickle
from sklearn.preprocessing import StandardScaler

total = np.loadtxt('feat_mat_peaks111.txt', delimiter=",")
result=np.loadtxt('result.txt',delimiter="\t") 

size=np.shape(total)



c=np.zeros(shape=(size[0],1))
for i in range(0,size[0]):
    train=np.delete(total,(i),axis=0)
    targetTrain=np.delete(result,(i),axis=0)
    test=total[i,:]
    scaler=StandardScaler()
    scaler.fit(train)
    train=scaler.transform(train)
    test = test.reshape((-1, 1))
    test=np.transpose(test)
    test=scaler.transform(test)
    clf = svm.SVC(gamma=0.0005, C=100)
    clf.fit(train,targetTrain)
    
    #with open('Saved_classifier.pkl', 'wb') as fid:
    #    pickle.dump(clf, fid)

    c[i][0]=clf.predict(test[:])
    print(c[i][0])
