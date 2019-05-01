import time


MAX_WAIT = 5


def wait_for(cond):
    """
    Continuing calling `cond`, a function that takes no argments. at one-second
    intervals, until it returns True.
    """
    start = time.time()
    while not cond():
        if time.time() - start > MAX_WAIT:
            raise Exception("exceeded max wait of {} second(s)".format(MAX_WAIT))
        time.sleep(0.1)
