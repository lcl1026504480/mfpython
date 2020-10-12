# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 10:02:38 2020

@author: lenovouser
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib auto


def add_layer(inputs, in_size, out_size, acfun=None):
        W = tf.Variable(tf.random_normal([in_size, out_size]))
        B = tf.Variable(tf.random_normal([1, out_size]))
        W_B = tf.matmul(inputs, W) + B
        if not acfun:
                outputs = W_B
        else:
                outputs = acfun(W_B)

        return outputs


x_data = np.linspace(-1, 1, 1000)[:, np.newaxis]
noise = np.random.normal(0, 0.1, x_data.shape)
y_data = x_data**2 + 1 + noise
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])

layer1 = add_layer(xs, 1, 10, tf.nn.relu)
predict = add_layer(layer1, 10, 1)
loss = tf.reduce_mean(
    tf.reduce_sum(
        tf.square(ys - predict), 1))
train = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
fig, ax = plt.subplots()
ax.scatter(x_data, y_data)
plt.ion()
plt.show()
init = tf.initialize_all_variables()
with tf.Session() as sess:
        sess.run(init)
        for epoch in range(1000):
                if not epoch % 10:
                        sess.run(train, feed_dict={xs: x_data, ys: y_data})
#                        print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
                        predict_value = sess.run(predict, feed_dict={xs: x_data})
                        lines = ax.plot(x_data, predict_value, "r", lw=5)
                        plt.pause(0.1)
                        ax.lines.remove(lines[0])
