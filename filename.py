# filename.py
import os
dir = 'slide/'
files = os.listdir(dir)
for file in files:
    if file.count('_') == 2:
        new = file.split('_')[2]
        os.rename(dir+file, dir+new)
        print(file, new)
    else:
        print('skip')
