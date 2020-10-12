# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 19:56:09 2020

@author: lenovouser
"""

import tensorflow as tf
a=tf.constant([[2,2]])
b=tf.constant([[1],
               [1]])
c=tf.matmul(a,b)
with tf.Session() as sess:
        print(sess.run(c))