# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:04:27 2020

@author: lenovouser
"""

import threading
import time
from queue import Queue

def job(l,q):
    for i in range(len(l)):
        l[i] = l[i]**2
    q.append(l)

def multithreading():
    q = []
    threads = []
    data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    results = []
    for _ in range(4):
          results.append(q[-1])
    print(q)

if __name__ == '__main__':
    multithreading()