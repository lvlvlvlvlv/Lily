# -*- coding: utf-8 -*-



import scipy.io as scio
import numpy as np
import matplotlib.pyplot as plt


#def downSampling():


def main():

    matfilepath = "C:\Users\lvxub\Desktop\data 2\data\patient1_interictal\Patient_1_interictal_segment_0001.mat"
    data = scio.loadmat(matfilepath)

    print data.viewkeys()
    y = data['data'][1,:]
    x = np.arange(0,300000)
    plt.plot(x,y)
    plt.show()
    print data


if __name__ == "__main__":
    main()
