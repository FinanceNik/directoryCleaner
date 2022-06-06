#! /usr/bin/python

from time import sleep  # letting the script wait a predefined time before running again
from os import system  # for using the system command to execute bash commands
from os import listdir  # listing the files and subdirectories in a directory
from os.path import isfile, join  # to determine if a file is a file or a directory
from pathlib import Path  # to make the folder directory dynamic


def main():
    """
    Description:
    ________________________________________________________________________________
    This little script has been created in order to automate the process of
    cleaning up the Download and Document folders. The script will re-run
    every 10 minutes and clean up the folders.

    The folders are constructed as follows:
        For every file type within a directory, the script will create a new
        folder. Therefore, all files types are grouped in the aptly named
        folders.

    """

    # Setting the path to the Download and Document folders
    paths = ["Downloads", "Documents"]
    for path in paths:
        path = str(Path.home() / path)+"/"
        all_files = [f for f in listdir(path) if isfile(join(path, f))]
        all_file_types = [i.split(".")[-1] for i in all_files]  # getting the file types
        unique_file_types = []  # initiating empty list of unique file types
        for i in all_file_types:
            if i not in unique_file_types:
                unique_file_types.append(i)

        # Creating the folders
        for file_type in unique_file_types:
            if '#' not in file_type:  # excluding lock files or corrupted files
                system(f'mkdir -p "{path}{file_type}"')

        # Moving the files to the folders
        for file_type in unique_file_types:
            if '#' not in file_type:  # excluding lock files or corrupted files
                system(f'mv {path}*.{file_type} {path}{file_type}')

    sleep(60*10)  # 10 minutes, aka 600 seconds


if __name__ == "__main__":
    main()