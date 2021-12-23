import os
import dropbox

fileFrom = "\Project - 101\Minecraft_ 1.16.3 - Singleplayer 2020-09-29 15-15-51"
fileTo = input('enter the path to upload: ')
class TransferData():
    def __init__(self, accessToken):
        self.accessToken = accessToken
    def uploadFile(self):
        for dirs, root , files in os.walk(fileFrom):
           pass
    os.path.relpath()
