import unittest
import requests

class VoiceTrainTest(unittest.TestCase):

# testing of audio upload and prediction of user 
    def test_successful_AudioUpload(self):
        user_test_voice_url = 'http://localhost:5000/test'
        test_audio_file = open('tests/0_jackson_20.wav', 'rb')
        send_files = {'file': ('0_jackson_20.wav', test_audio_file, 'audio/mpeg')}
        r = requests.post(user_test_voice_url, files=send_files)
        self.assertEqual(200, r.status_code)

# Converting train audio file to spectrogram and save as image
    def test_Train_Audio_data(self):
        user_train_voice_url = 'http://localhost:5000/train'
        train_audio_file = open('tests/0_jackson_46.wav', 'rb')
        send_files = {'file': ('0_jackson_46.wav', train_audio_file, 'audio/mpeg')}
        response = requests.post(user_train_voice_url, files=send_files)
        self.assertEqual(200, response.status_code)
