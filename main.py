# -*- coding: utf-8 -*-



import scipy.io as scio
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

#def downSampling():
def Gen_dataset_sample(filepath,dataset_type):

    if dataset_type == "Train":
        filelist = list()
        folderpath_pos = "C:\Users\lvxub\Desktop\data 2\data\patient1_preictal"
        folderpath_neg = "C:\Users\lvxub\Desktop\data 2\data\patient1_interictal"

        data = scio.loadmat(filepath)
        data_name = filepath.split("\\")[-1]
        data_name_sub = data_name.split("_")
        data_name_applied = data_name_sub[2] + '_' + data_name_sub[3] + '_' + str(int(data_name_sub[4].split(".")[0]))
        print data_name_applied
        y = data[data_name_applied]['data'][0][0]
        rows = y.shape[0]
        cols = y.shape[1]
        matList = list()
        for i in range(0, cols, 5000):
            matList.append(y[:, i:i + 5000])
        pca = PCA()
        for i in range(len(matList)):
            matList[i] = pca.fit_transform(matList[i])
        matList_conatenate = np.concatenate(matList, axis=1)

def main():
    P_Train_folder = "C:\Users\lvxub\Desktop\data 2\data\patient1_preictal"
    N_Train_folder = "C:\Users\lvxub\Desktop\data 2\data\patient1_interictal"
    matfilepath = "C:\Users\lvxub\Desktop\data 2\data\patient1_interictal\Patient_1_interictal_segment_0001.mat"
    data = scio.loadmat(matfilepath)

    print data.viewkeys()
    y = data['interictal_segment_1']['data'][0][0]
    print y.shape[0]
    rows = y.shape[0]
    cols = y.shape[1]
    matList = list()
    for i in range(0,cols,5000):

        matList.append(y[:,i:i+5000])

    # matList are un-PCAed data
    print len(matList)

    pca = PCA()
    for i in range(len(matList)):
        matList[i] = pca.fit_transform(matList[i])


    # Now matList are PCAed data  15*15

    matList_conatenate = np.concatenate(matList, axis=1)

    print matList_conatenate.shape
    #print matList[i].shape
    '''y = data['data'][1,:]
    x = np.arange(0,300000)
    plt.plot(x,y)
    plt.show()
    print data'''


if __name__ == "__main__":
    #main()
    Gen_Train_dataset_sample("C:\Users\lvxub\Desktop\data 2\data\patient1_interictal\Patient_1_interictal_segment_0001.mat")