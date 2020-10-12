# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 18:37:59 2020

@author: lenovouser
"""

import multiprocessing as mp
import time

v = 0


def job(v, num, l):
    l.acquire()
    for _ in range(10):
        time.sleep(0.1)
        v += num
        print(v)
    l.release()


def multicore():
    l = mp.Lock()
    # v = mp.Value('i', 0)
    global v
    p1 = mp.Process(target=job, args=(v, 1, l))
    p2 = mp.Process(target=job, args=(v, 3, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    multicore()
