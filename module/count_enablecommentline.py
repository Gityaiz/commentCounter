import re

'''
    [DESCRIPTION]
        Classify types of argument's line enable or comment 
    [PRECONDITION]
        Python 3.7.0
    [RETURN VALUE]
        NORMAL
            file_dictionary = {'allLine': integer, 'enableLine': integer, 'commentLine': integer, 'currentStatus': integer}
        FAILURE
            -1  :   argument NowEnableOrComment is not 0 and 1
'''


def classify_C_enable_or_comment(enable_or_comment, analyzed_line):
    ENABLE = 0
    COMMENT = 1

    # 辞書型オブジェクトの生成
    line_status = {'allLine': 0, 'enableLine': 0, 'commentLine': 0, 'currentStatus': ENABLE}

    # 引数チェック
    if enable_or_comment != ENABLE and enable_or_comment != COMMENT:
        return -1

    if enable_or_comment == ENABLE:

        # at the beginning "//"
        if re.match("\s*\/\/", analyzed_line):
            line_status['allLine'] = 1
            line_status['enableLine'] = 0
            line_status['commentLine'] = 1
            line_status['currentStatus'] = ENABLE
            return line_status

        # [0 or more spaces] /* [0 or more any] */ [0 or more spaces] // [0 or more any]
        elif re.match("\s*\/\*.*\*\/\s*\/\/.*", analyzed_line):
            line_status['allLine'] = 1
            line_status['enableLine'] = 0
            line_status['commentLine'] = 1
            line_status['currentStatus'] = ENABLE
            return line_status

        # [0 or more spaces] /* [0 or more any] */ [0 or more spaces][one or more other than spaces][0 or more spaces] // [0 or more any]
        elif re.match("\s*\/\*.*\*\/\s*\S+\s*\/\/.*", analyzed_line):
            line_status['allLine'] = 1
            line_status['enableLine'] = 1
            line_status['commentLine'] = 1
            line_status['currentStatus'] = ENABLE
            return line_status

        # [0 or more spaces] /* [0 or more any] * / [0 or more spaces][one or more other than spaces][0 or more spaces]
        elif re.match("\s*\/\*.*\*\/.+", analyzed_line):
            line_status['allLine'] = 1
            line_status['enableLine'] = 1
            line_status['commentLine'] = 1
            line_status['currentStatus'] = ENABLE
            return line_status

        # [0 or more spaces] /* [0 or more any] */
        elif re.match("\s*\/\*.*\*\/", analyzed_line):
            line_status['allLine'] = 1
            line_status['enableLine'] = 0
            line_status['commentLine'] = 1
            line_status['currentStatus'] = ENABLE
            return line_status

        # [0 or more spaces] /* [0 or more any]
        elif re.match("\s*\/\*.*", analyzed_line):
            line_status['allLine'] = 1
            line_status['enableLine'] = 0
            line_status['commentLine'] = 1
            line_status['currentStatus'] = COMMENT
            return line_status

        # [0 or more spaces][one or more other than spaces][0 or more spaces] /* [0 or more any] */
        elif re.match("\s*\S+\s*\/\*.*\*\/", analyzed_line):
            line_status['allLine'] = 1
            line_status['enableLine'] = 1
            line_status['commentLine'] = 1
            line_status['currentStatus'] = ENABLE
            return line_status

        # [0 or more spaces][one or more other than spaces][0 or more spaces] /* [0 or more any]
        elif re.match("\s*\S+\s*\/\*.*", analyzed_line):
            line_status['allLine'] = 1
            line_status['enableLine'] = 1
            line_status['commentLine'] = 1
            line_status['currentStatus'] = COMMENT
            return line_status

        # [0 or more spaces][one or more other than spaces][0 or more spaces] // [0 or more any]
        elif re.match("\s*\S+\s*\/\/.*", analyzed_line):
            line_status['allLine'] = 1
            line_status['enableLine'] = 1
            line_status['commentLine'] = 1
            line_status['currentStatus'] = ENABLE
            return line_status

        # [0 or more spaces] EOL
        elif re.match("\s*\Z", analyzed_line):
            line_status['allLine'] = 1
            line_status['enableLine'] = 0
            line_status['commentLine'] = 0
            line_status['currentStatus'] = ENABLE
            return line_status

        # anything else
        else:
            line_status['allLine'] = 1
            line_status['enableLine'] = 1
            line_status['commentLine'] = 0
            line_status['currentStatus'] = ENABLE
            return line_status

    elif enable_or_comment == COMMENT:
        # [0 or more any] */ [0 or more spaces] // [0 or more any]
        if re.match(".*\*\/\s*\/\/.*", analyzed_line):
            line_status['allLine'] = 1
            line_status['enableLine'] = 0
            line_status['commentLine'] = 1
            line_status['currentStatus'] = ENABLE
            return line_status

        # [0 or more any] */ [0 or more spaces][one or more other than spaces][0 or more spaces]
        elif re.match(".*\*\/\s*\S+\s*", analyzed_line):
            line_status['allLine'] = 1
            line_status['enableLine'] = 1
            line_status['commentLine'] = 1
            line_status['currentStatus'] = ENABLE
            return line_status
        # [0 or more any] */ [0 or more spaces]
        elif re.match(".*\*\/\s*", analyzed_line):
            line_status['allLine'] = 1
            line_status['enableLine'] = 0
            line_status['commentLine'] = 1
            line_status['currentStatus'] = ENABLE
            return line_status
        # anything else
        else:
            line_status['allLine'] = 1
            line_status['enableLine'] = 0
            line_status['commentLine'] = 1
            line_status['currentStatus'] = COMMENT
            return line_status
