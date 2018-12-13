# import count_enablecommentline as ce
from . import count_enablecommentline as ce

'''
    [DESCRIPTION]
        execute "classify_C_enable_or_comment" to all lines of "filename"
    [PRECONDITION]
        Python 3.7.0
    [RETURN VALUE]
        NORMAL
            line_counter = {'allLine': 0, 'enableLine': 0, 'commentLine': 0}
        FAILURE
            -1  :   argument NowEnableOrComment is not 0 and 1
'''


def readlines(filename):
    ENABLE = 0
    line_counter = {'allLine': 0, 'enableLine': 0, 'commentLine': 0, 'currentStatus': ENABLE}

    f = open(filename, 'r')
    
    for analyzedline in f.readlines():
        temp_counter = ce.classify_C_enable_or_comment(line_counter['currentStatus'], analyzedline)

        # add every element except 'currentStatus'
        line_counter['allLine'] += temp_counter['allLine']
        line_counter['enableLine'] += temp_counter['enableLine']
        line_counter['commentLine'] += temp_counter['commentLine']

        # substitute
        line_counter['currentStatus'] = temp_counter['currentStatus']

        # logging for debug
        # print(sys._getframe(1).f_locals)
        # print(temp_counter, end="")
        # print(line_Counter, end="")
        # print(analyzedline, end="")

    f.close()

    # 'currentStatus' element is not needed for caller
    del(line_counter['currentStatus'])

    return line_counter
