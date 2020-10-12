import tensorflow as tf
import numpy as np

x_data = np.random.rand(100).astype(np.float16)
W=tf.Variable(tf.random_uniform([1],-1,1))
B=tf.Variable(tf.zeros([1]))
k=3
b=1
y_data=x_data*k+b
y=W*x_data+B

loss=tf.reduce_mean(tf.square(y_data-y))

opt=tf.train.GradientDescentOptimizer(0.5)
train=opt.minimize(loss)

init=tf.initialize_all_variables()
sess=tf.Session()
sess.run(init)
for it in range(201):
        sess.run(train)
        if not it % 20:
                print(it,sess.run(W),sess.run(B))
                
