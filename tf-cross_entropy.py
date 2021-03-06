# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 01:32:01 2017

@author: Toshiharu
"""

# Solution is available in the other "solution.py" tab
import tensorflow as tf

softmax_data = [0.7, 0.2, 0.1]
one_hot_data = [1.0, 0.0, 0.0]

softmax = tf.placeholder(tf.float32)
one_hot = tf.placeholder(tf.float32)

# TODO: Print cross entropy from session

summands = tf.multiply(one_hot,tf.log(softmax))
cross_entropy = tf.reduce_sum(-summands)

with tf.Session() as sess:
    output = sess.run(cross_entropy, feed_dict={softmax: softmax_data, one_hot: one_hot_data} )

print(output)