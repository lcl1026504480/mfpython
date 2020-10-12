# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:15:07 2020

@author: lenovouser
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 10:02:38 2020

@author: lenovouser
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib auto

def add_layer(inputs, in_size, out_size, n,acfun=None):
        layername="layer%s" % n
        with tf.name_scope("layer"):
                W = tf.Variable(tf.random_normal([in_size, out_size]),name="W")
                B = tf.Variable(tf.random_normal([1, out_size]),name="B")
                tf.summary.histogram(layername+"\W",W)
                tf.summary.histogram(layername+"\B",B)
                W_B = tf.matmul(inputs, W) + B
        if not acfun:
                outputs = W_B
        else:
                outputs = acfun(W_B)
        tf.summary.histogram(layername+"\output",outputs)
        return outputs


x_data = np.linspace(-1, 1, 1000)[:, np.newaxis]
noise = np.random.normal(0, 0.1, x_data.shape)
y_data = x_data**2 + 1 + noise
with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, [None, 1], name='x_input')
    ys = tf.placeholder(tf.float32, [None, 1], name='y_input')

layer1 = add_layer(xs, 1, 10,1, tf.nn.relu)
predict = add_layer(layer1, 10, 1,2)
with tf.name_scope("loss"):
        loss = tf.reduce_mean(
            tf.reduce_sum(
                tf.square(ys - predict), 1))
tf.summary.scalar("loss",loss)
with tf.name_scope("train"):
        train = tf.train.AdamOptimizer(0.1).minimize(loss)
fig, ax = plt.subplots()
ax.scatter(x_data, y_data)
plt.ion()
plt.show()
init = tf.initialize_all_variables()

with tf.Session() as sess:
        merged=tf.summary.merge_all()
        writer=tf.summary.FileWriter("./",sess.graph)
        sess.run(init)
        
        for epoch in range(1000):
                if not epoch % 10:
                        sess.run(train, feed_dict={xs: x_data, ys: y_data})
#                        print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
                        predict_value = sess.run(predict, feed_dict={xs: x_data})
                        lines = ax.plot(x_data, predict_value, "r", lw=5)
                        plt.pause(0.1)
                        ax.lines.remove(lines[0])
                        result = sess.run(merged,
                          feed_dict={xs: x_data, ys: y_data})
                        writer.add_summary(result, epoch)
