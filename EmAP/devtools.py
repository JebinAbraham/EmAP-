import json
import os
def getfunctionoutput(path,object):
    #check if path exists
    #create till the folder not the file 
    folderpath = path.split("\\")
    folderpath = "\\".join(folderpath[:-1])
    if os.path.exists(path):
        #if not exists, create the path
        os.makedirs(path)
    with open(path, 'w') as outfile:
     json.dump(object, outfile)