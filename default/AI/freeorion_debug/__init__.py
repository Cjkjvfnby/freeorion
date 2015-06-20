"""
This module will store all tool for debug and testing.
"""

from timers import Timer
import inspect


def print_stack():
    """
    Print stack for current call in simple way
    """
    prevs = inspect.getouterframes(inspect.currentframe(), 3)
    print "Current stack"
    for x in prevs:
        path = x[1]
        line = x[2]
        name = x[3]
        if name != 'wrapper':
            print '    %s:%s %s' % (os.path.basename(path), line, name)
