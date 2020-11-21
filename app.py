from flask import Flask
from flask import request
from GenerateSpectrogram import Train_Voice
from TestVoice import Check_Voice
from UserList import UserList
import json
import os

app = Flask(__name__)
@app.route('/test', methods=['GET', 'POST'])
def checkVoice():
    if request.method == 'POST':
        file = request.files['file']
        file.save('Check_audio_file/'+file.filename)
        train_obj = Train_Voice()
        train_obj.create_spectrogram(file.filename, 'test')
        obj = Check_Voice()
        name,score=obj.match_voice((file.filename.split('.')[0])+'.jpg')
        predicted_user = name.split("_")

        print("this is name of predicted user")
        print(predicted_user)
        os.remove('Check_audio_file/'+file.filename)
        os.remove('Generated_test_image/'+file.filename.split('.')[0]+'.jpg')
        # if (name.split('.')[0] == (file.filename.split('.')[0])):
        #     status = {'status' : 'true'}
        # else:
        #     status = {'status' : 'false'}
        # return json.dumps(status)
        return predicted_user[0] + '_' + predicted_user[1]
    else:
        return "file is not saved"  

@app.route('/train', methods =['GET','POST'])
def trainVoice():
    if request.method == 'POST':
        file = request.files['file']
        file.save('Test_audio_files/'+file.filename)
        train_obj = Train_Voice()
        user_obj = UserList()
        train_obj.create_spectrogram(file.filename, 'train')
        user_obj.create_UserList((file.filename).split('.')[0]+".jpg")
        return "200"
    else:
        return "file is not saved" 
    # return "This is user check of user"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)

