import time
from concurrent.futures import ProcessPoolExecutor


def fa(a):
    return a * a


def fb(b):
    return b * b


p = ProcessPoolExecutor(5)


def fc(c):
    return c * c


p.submit(fa, 1)
p.submit(fb, 2)
p.submit(fc, 3)


time.sleep(5)