import os
import shelve
import shutil
import send2trash

#print(os.getcwd())
#os.chdir('H:\\DEV\\pystuff\\pystuff\\New Python') # change working directory
print(os.getcwd())
myData = open('Automation\\files\\data.txt')
content = myData.read()
print(content)
myData.close()

myDat2a = open('Automation\\files\\data2.txt', 'w')
myDat2a.write('my broo')
myDat2a.close()

#shelf files are binary can store different data like lists

shelfFile = shelve.open('Automation\\files\\myshelf')
shelfFile['cats'] = ['kitty','sophie','ginja']
shelfFile.close()

shelfFile = shelve.open('Automation\\files\\myshelf')
print(shelfFile['cats'])
shelfFile.close()

shelfFile = shelve.open('Automation\\files\\myshelf')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()

#shutil copy move files

#shutil.copy(' data2.txt',' data2222.txt') # copy a file

#shutil.copytree('New Python', 'New Python Backup') # copy a tree or directory

#shutil.move('') move file to a different directory. used to rename files if you move it to the same directory

#os.unlink('New Python/data2.txt') old way to delete a file
#os.rmdir() delete a directory must be empty

#shutil.rmtree('H:\\DEV\\pystuff\\pystuff\\New Python Backup') permanently delete tree

#send2trash.send2trash(' data2.txt') added module send2trash pip.exe install send2trash, imported it and run send2trash, this sends file to recycle bin

for folderName, subfolders, filenames in os.walk('Automation\\files\\test'): #perform actions on all folders and files in a directory
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))
    print()
    
    for subfolder in subfolders:
        if 'huh' in subfolder:
            print('YEPPP')
            
    for file in filenames:
        if file.endswith('.txt'):
            print('GOTT EMM')