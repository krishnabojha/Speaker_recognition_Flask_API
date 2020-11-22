#Importing bunch of libraries.
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

class Train_Voice:
    #Converts the audio into spectrogram.
    # where mode determine that the created spectrogram is of test or train audio file
    def create_spectrogram(self, filename, mode):
        if mode == 'train':
            filepath='Test_audio_files/'+filename
            new_name=filename.split('.')[0]
            save_path='Generated_images/'+new_name+'.jpg'
        else:
            filepath='Check_audio_file/'+filename
            new_name=filename.split('.')[0]
            save_path='Generated_test_image/'+new_name+'.jpg'

        plt.interactive(False)
        clip,sample_rate=librosa.load(filepath,sr=None)
        fig=plt.figure(figsize=[0.72,0.72])
        ax=fig.add_subplot(111)
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        ax.set_frame_on(False)
        S=librosa.feature.melspectrogram(y=clip,sr=sample_rate)
        librosa.display.specshow(librosa.power_to_db(S,ref=np.max))
        fig.savefig(save_path,dpi=400,bbox_inches='tight',pad_inches=0)
        plt.close()
        fig.clf()
        plt.close(fig)
        plt.close('all')
        del filepath,save_path,clip,sample_rate,fig,ax,S