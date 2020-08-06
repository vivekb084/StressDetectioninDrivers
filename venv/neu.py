

from sklearn.neural_network import MLPClassifier
import numpy as np
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
    test=test.reshape((-1,1))
    test=np.transpose(test)
    test=scaler.transform(test)
    clf = MLPClassifier(solver='lbfgs', alpha=5, hidden_layer_sizes=(10,), random_state=3, warm_start=True,max_iter=1000)
    clf.fit(train,targetTrain)
    
    #with open('Saved_classifier.pkl', 'wb') as fid:
    #    pickle.dump(clf, fid)

    c[i][0]=clf.predict(test[:])
    print(c[i][0])