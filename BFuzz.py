import os
import signal
import subprocess
import sys
from time import sleep

def runWebTest():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print("Enter the browser type:  \n 1: Chrome \n 2: Firefox")
    browserType = input('>>')
    if browserType not in [1,2]:
        print("Incorrect option!!")
        sys.exit(0)
    for root, folders, fileNames in os.walk("recurve"):
        for fileName in fileNames:
            if not fileName.endswith('.html'):
                continue
            if browserType == 1:
                processCommand = 'chrome '
            elif browserType == 2:
                processCommand = ['firefox','--new-instance']
            filePath = os.path.join(dir_path,root,fileName)
            filePath = "file://"+filePath
            print filePath
            processCommand.append(filePath)
            print processCommand
            process = subprocess.Popen(processCommand)
            sleep(12)
            process.kill()
            sleep(3)


if __name__ == '__main__':
    runWebTest()
