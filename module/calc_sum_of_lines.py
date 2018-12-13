#!/usr/bin/env python3

'''
    [DESCRIPTION]
        calculate the sum of all kind of lines  " list of argument's directory"
    [PRECONDITION]
        Python 3.7.0
    [RETURN VALUE]
        NORMAL
            list = [sum of allLine, sum of enableLine, sum of commentLine]

'''

def calc_sum_of_lines(directory_list):
    # Calculate the sum of allline
    sum_of_allline = [int(d.get('allLine')) for d in directory_list]
    sum_of_allline = sum(int(i) for i in sum_of_allline)
    # Calculate the sum of enableline
    sum_of_enableline = [int(d.get('enableLine')) for d in directory_list]
    sum_of_enableline = sum(int(i) for i in sum_of_enableline)
    # Calculate the sum of commentline
    sum_of_commentline = [int(d.get('commentLine')) for d in directory_list]
    sum_of_commentline = sum(int(i) for i in sum_of_commentline)

    return sum_of_allline, sum_of_enableline, sum_of_commentline

