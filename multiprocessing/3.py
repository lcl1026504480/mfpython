# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 18:27:21 2020

@author: lenovouser
"""

import multiprocessing as mp

def job(x):
    return x*x

def multicore():
    pool = mp.Pool()
    res = pool.map(job, range(10))
    print(res)
    res = pool.apply_async(job, (2,))
    print(res.get())
    multi_res =[pool.apply_async(job, (i,)) for i in range(10)]
    print([res.get() for res in multi_res])


if __name__ == '__main__':
    multicore()