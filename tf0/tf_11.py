# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:41:59 2020

@author: lenovouser
"""

import tensorflow as tf

c = tf.Variable(0, name="counter")
a = tf.constant(1)

new = tf.add(c, a)

update = tf.assign(c, new)

init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        print(c.name)
        sess.run(update)
        print(sess.run(c))
