import os

print(os.listdir())
for dirName, subDirList, fileList in os.walk('.'):
    print(dirName, subDirList, fileList)
# os.rename('./Frequency.json', 'frequency.json')
# os.mkdir('1')

os.rmdir('1')