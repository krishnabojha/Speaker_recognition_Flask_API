#Importing bunch of libraries.
import cv2
import os
import librosa
import librosa.display
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.models import load_model

class Check_Voice:

    def match_voice(self, filename):
        model=load_model('SpeakerID_best.hdf5')
        data = pd.read_csv("UserListCSV/UserList.csv")
        # remember the first row of CSV file is header 
        all_files_list= list(data.iloc[:, 0])
        score_list=[]
        img1=cv2.imread('Generated_test_image/'+filename)
        img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
        img1=cv2.resize(img1,(150,150))
        img1=img1/255
        for i in range(len(all_files_list)):
            
            img2=cv2.imread('Generated_images/'+all_files_list[i])
            img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
            img2=cv2.resize(img2,(150,150))
            img2=img2/255
            X=[np.zeros((1,150,150,3)) for i in range(2)]
            Y=[np.zeros(1,)]
            X[0][0,:,:,:]=img1
            X[1][0,:,:,:]=img2
            score_list.append(model.predict(X))
        score_list=np.array(score_list)
        idx=np.argmax(score_list)
        return all_files_list[idx],score_list[idx]
