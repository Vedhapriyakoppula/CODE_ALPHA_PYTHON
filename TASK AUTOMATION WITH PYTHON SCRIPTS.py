import os
import shutil

path = input("Enter Path:")
files = os.listdir(path)

for file in files:
    filename,extension = os.path.splittext(file)
    extension = extension[1:]

    if os.path.exists(path+'/'+extension):
        shutil.mov(path+'/'+file,path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
        