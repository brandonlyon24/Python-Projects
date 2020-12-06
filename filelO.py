

import os
import time

##fName = 'Hello.txt'

##fPath = 'C:\\A\\'

##abPath = os.path.join(fPath, fName)
##print(abPath)

#Assignment step 180

fName = "blank.py"
path = "C:\python_projectsV2"
dir_list = os.listdir(path)
#print(dir_list)

abPath = os.path.join(path,fName)
print(abPath)



#getmtime() latest date

abDate = os.path.getmtime(abPath)
print(abDate)


#Your script will need to print each file ending with a “.txt” file extension and its corresponding mtime to the console.
#Finish this 
