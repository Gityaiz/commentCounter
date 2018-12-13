import unicodedata


'''
    [DESCRIPTION]
        Adjust string digit with padding additional space
    [PRECONDITION]
        Python 3.7.0
    [RETURN VALUE]
        NORMAL
            padded argument string

'''

def left(digit, msg):
    for c in msg:
        if unicodedata.east_asian_width(c) in ('F', 'W', 'A'):
            digit -= 2
        else:
            digit -= 1
    return msg + ' '*digit


def right(digit, msg):
    for c in msg:
        if unicodedata.east_asian_width(c) in ('F', 'W', 'A'):
            digit -= 2
        else:
            digit -= 1
    return ' '*digit + msg
