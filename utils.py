#
# utils.py
# - Utilities
#
import sys

class ProgressBar:
    '''
    The progress bar.

    Args:
        total (int): Total amount of iteration.
        format (str): Style of the progress bar. Default is `'{progress} {percent}'`.
        size (int): Width of the progress bar. Default is 20.
        bar (str): Character used as bar in the progress bar. Default is '#'.
        update (int): The period of progress bar update. Default is 1.
    
    Note:
        This progress bar is not thread-safe. Use with caution.
    '''

    def __init__(self, total, format='{progress} {percent}', size=20, bar='#', update=1):
        self.__index = 0
        self.__size = size
        self.__bar = bar
        self.__format = format
        self.__total = total
        self.__update = update
    
    def update(self):
        '''
        Update progress bar.
        '''
        should_print = self.__index % self.__update == 0
        self.__index += 1

        percent = self.__index / self.__total
        fill_chars = int(self.__size * percent)
        bar = '[{0}{1}]'.format(self.__bar * fill_chars, ' ' * (self.__size - fill_chars))

        if (should_print or self.__index >= self.__total):
            sys.stderr.write('\r' + self.__format.format(percent="{0:.2f}%".format(percent*100), progress=bar))

        if (self.__index >= self.__total):
            sys.stderr.write('\n')