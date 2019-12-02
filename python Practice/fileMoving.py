import os
import shutil

their_root = '/Users/shahrozimtiaz/Desktop/cats_dogs_128x128'
my_root = '/Users/shahrozimtiaz/Desktop/mycats_dogs_128x128'

#training
setDir = '/trainset'
os.chdir(their_root+setDir)
files = os.listdir()
for f in files:
    if f.startswith("dog"):
        old_filename = str(f)
        new_filename = old_filename.split('.')
        new_filename = new_filename[1]+'.'+new_filename[2]
        filePath = os.path.join(their_root+setDir, f)
        os.rename(filePath,their_root+setDir+'/'+new_filename)
        filePath = their_root+setDir+'/'+new_filename
        shutil.move(filePath, my_root+setDir+'/dog')
    elif f.startswith("cat"):
        old_filename = str(f)
        new_filename = old_filename.split('.')
        new_filename = new_filename[1]+'.'+new_filename[2]
        filePath = os.path.join(their_root+setDir, f)
        os.rename(filePath,their_root+setDir+'/'+new_filename)
        filePath = their_root+setDir+'/'+new_filename
        shutil.move(filePath, my_root+setDir+'/cat')
    else:
        print('error: ', files)

#validation
#training
setDir = '/valset'
os.chdir(their_root+setDir)
files = os.listdir()
for f in files:
    if f.startswith("dog"):
        old_filename = str(f)
        new_filename = old_filename.split('.')
        new_filename = new_filename[1]+'.'+new_filename[2]
        filePath = os.path.join(their_root+setDir, f)
        os.rename(filePath,their_root+setDir+'/'+new_filename)
        filePath = their_root+setDir+'/'+new_filename
        shutil.copy(filePath, my_root+setDir+'/dog')
    elif f.startswith("cat"):
        old_filename = str(f)
        new_filename = old_filename.split('.')
        new_filename = new_filename[1]+'.'+new_filename[2]
        filePath = os.path.join(their_root+setDir, f)
        os.rename(filePath,their_root+setDir+'/'+new_filename)
        filePath = their_root+setDir+'/'+new_filename
        shutil.move(filePath, my_root+setDir+'/cat')
    else:
        print('error: ', f)
