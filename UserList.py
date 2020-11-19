class UserList:
    def create_UserList(self, UserName):
    ## the title is set to user and name of image of spectrogram is listed
        with open('UserListCSV/UserList.csv','a') as fd:
            fd.write(UserName + '\n')