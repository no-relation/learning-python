#! python3
# selectiveCopy.py - copies files with only a certain file extension 
# to a new folder

import os, shutil

def verifyInput(prompt, default):
    incorrect = True
    while incorrect:
        print(prompt + ' (Enter for ' + default + ')')
        userInput = input()
        if len(userInput) == 0:
            userInput = default
        print('You said "' + userInput + '"\n' + 'Is that correct? (yes/no)')
        verify = input()
        if verify and verify[0].lower() == 'y':
            incorrect = False
    return userInput

sourcePath = verifyInput("Input folder path to copy", os.getcwd())
extension = verifyInput("Input extension of file type to copy, not including the period", 'jpg')
parentDir, sourceFolder = os.path.split(sourcePath)
destPath = verifyInput("Input destination folder", parentDir + '/' + sourceFolder + extension + 'copy')
if not os.path.exists(destPath):
    os.mkdir(destPath)

count = 0
# only want top-level directory, not the whole tree down. It's a feature, not a bug.
root, dirs, files = os.walk(sourcePath)[0]

for file in files:
    if file[-4:] == extension:
        print('Copying %s' % (file))
        shutil.copy(root + '/' + file, destPath)
        count += 1

print('Copied %s files' % (str(count)))
