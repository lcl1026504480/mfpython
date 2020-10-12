# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:24:13 2020

@author: lenovouser
"""

import threading

# def main():
#    print(threading.active_count())
#    print(threading.enumerate()) # see the thread list
#    print(threading.current_thread())


def thread_job():
    print(threading.active_count())
    print('This is a thread of %s' % threading.current_thread())


def main():
    print(threading.active_count())
    print()
    print(threading.enumerate())  # see the thread list
    print()
    print(threading.current_thread())

    thread = threading.Thread(target=thread_job,)
    thread.start()


if __name__ == '__main__':
    main()
