#!/usr/bin/python

import os
import subprocess
import sys
from time import sleep


def runWebTest():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print("Enter the browser type:  \n 1: Chrome \n 2: Firefox")
    browserType = input('>>')
    timeout = input(
        "Duration the browser process should wait before stopping(>=15 seconds to ensure full load of page):")
    checkValidBrowserType(browserType)
    for root, folders, fileNames in os.walk("recurve"):
        for fileName in fileNames:
            if not fileName.endswith('.html'):
                continue
            processCommand = getBrowserApplication(browserType)
            if processCommand is not None:
                setupExploit(dir_path, fileName, processCommand, root)
                runExploit(processCommand, timeout)
            else:
                print "Invalid Browser Type"


def runExploit(processCommand, timeout):
    print "Executing Command: " + " ".join(processCommand)
    process = subprocess.Popen(processCommand)
    sleep(timeout)
    # print "Killing browser process.... bye bye"
    sleep(3)


def setupExploit(dir_path, fileName, processCommand, root):
    filePath = os.path.join(dir_path, root, fileName)
    filePath = "file://" + filePath
    print "Testing with exploit:" + filePath
    processCommand.append(filePath)


def getBrowserApplication(browserType):
    if browserType == 1:
        processCommand = ['google-chrome']
    elif browserType == 2:
        processCommand = ['firefox', '-new-tab']
    else:
        processCommand = None
    return processCommand


def checkValidBrowserType(browserType):
    if browserType not in [1, 2]:
        print("Incorrect option!!")
        sys.exit(0)


if __name__ == '__main__':
    runWebTest()
