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

# Example
createFolder('./data/')