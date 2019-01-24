# Utility to copy datasets to the AIF360 data folder
# By running this script, you acknowledge the responsibility for reading 
# and abiding by any copyright/usage rules and restrictions for each dataset.
# These are available in the installation guide.

import sys
import os
import shutil

import aif360

aifpath = os.path.split(aif360.__file__)[0]

dirnames = os.listdir('data')

for dirname in dirnames:
    fulldir = os.path.join('data', dirname)
    
    if os.path.isdir(fulldir):
        files = os.listdir(fulldir)
        
        for file in files:
            fulldirf = os.path.join(fulldir, file)
            if os.path.isfile(fulldirf):
                shutil.copy(fulldirf, os.path.join(aifpath, 'data', 'raw', dirname))
                print('Copied %s to the directory %s' % (fulldirf, os.path.join(aifpath, 'data', 'raw', dirname)))

