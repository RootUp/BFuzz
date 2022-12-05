#!/usr/bin/python

import os
import subprocess
import sys
from time import sleep


def run_web_test():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print("Enter the browser type:  \n 1: Chrome \n 2: Firefox")
    try:
        browser_type = int(input('>>'))
        timeout = int(input("Duration the browser process should wait before stopping(>=15 seconds to ensure full load of page):"))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    check_valid_browser_type(browser_type)

    for root, folders, file_names in os.walk("recurve"):
        for file_name in file_names:
            if not file_name.endswith('.html'):
                continue
            process_command = get_browser_application(browser_type)
            if process_command is not None:
                setup_exploit(dir_path, file_name, process_command, root)
                run_exploit(process_command, timeout)
            else:
                print "Invalid Browser Type"


def run_exploit(process_command, timeout):
    print "Executing Command: " + " ".join(process_command)
    process = subprocess.Popen(process_command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    sleep(timeout)
    # print "Killing browser process.... bye bye"
    sleep(3)


def setup_exploit(dir_path, file_name, process_command, root):
    file_path = os.path.join(dir_path, root, file_name)
    file_path = "file://" + file_path
    print "Testing with exploit:" + file_path
    process_command.append(file_path)


def get_browser_application(browser_type):
    if browser_type == 1:
        process_command = ['google-chrome']
    elif browser_type == 2:
        process_command = ['firefox', '-new-tab']
    else:
        process_command = None
    return process_command


def check_valid_browser_type(browser_type):
    if browser_type not in [1, 2]:
        print("Incorrect option!!")
        sys.exit(0)


def main():
    run_web_test()


if __name__ == '__main__':
    main()
