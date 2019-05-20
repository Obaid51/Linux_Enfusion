# creating folder
# importing date and time
from datetime import date

import os
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)
today = date.today()
print("Today's date:", today)
name = input("Enter your name : ")
data = (name+today)
createFolder('./today + name/')
images = [np.random.randn(8, 12) for _ in range(50)]
stacked =  np.stack(images, axis=0)
print(stacked.shape)