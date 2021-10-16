# Python 3

import os
import pprint


name = '29_'

for files in os.walk(os.getcwd()):
    for x in files[2]:
        if x.startswith(name):
            new = x[3:]
            os.renames(f'{x}', f'{new}')
            
    


