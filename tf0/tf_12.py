# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:50:21 2020

@author: lenovouser
"""

import tensorflow as tf

a=tf.placeholder(tf.float16)
b=tf.placeholder(tf.float16)

c=tf.multiply(a,b)

with tf.Session() as sess:
        for i in range(2):
                print(sess.run(c,
                               feed_dict={a:[float(i)],
                                          b:[float(i+1)]
                                               }))
        