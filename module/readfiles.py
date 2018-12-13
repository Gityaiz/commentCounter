#!/usr/bin/env python3
import glob
import os
import re
from . import readlines as rl
# import readlines as rl


'''
    [DESCRIPTION]
        Count the comment lines of all files in the "argument's directory"
        target  1   :   C 
                2   :   cshtml
    [PRECONDITION]
        Python 3.7.0
    [RETURN VALUE]
        NORMAL
            file_dictionary = [{'allLine': integer, 'enableLine': integer, 'commentLine': integer, 'filename': char}..]
        FAILURE
            -1  :   scanning_directory is not exist
'''


def readfiles(scanning_directory, target):

    if not os.path.isdir(scanning_directory):
        # scanning_directory is not exist
        return -1

    # dictionary list of all files in the "scanning_directory"
    file_dictionary = []

    # glob.glob(filename, options...)
    # "recursive=True" corresponds flag whether scanning sub directory or not
    for file in glob.glob(scanning_directory + '/**', recursive=True):
        ext = os.path.splitext(file)
        if target == 1:
            if re.match('.*\..*', ext[1]):
                line_dictionary = rl.readlines(file)
                line_dictionary['filename'] = file
                file_dictionary.append(line_dictionary.copy())

    return file_dictionary

