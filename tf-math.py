# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 00:53:53 2017

@author: Toshiharu
"""

# Solution is available in the other "solution.py" tab
import tensorflow as tf

# TODO: Convert the following to TensorFlow:
x = tf.constant(10.0)
y = tf.constant(2.0)
a = tf.constant(1.0)

b =  tf.divide(x,y)

z = tf.subtract(b,a)

with tf.Session() as sess:
    output = sess.run(z)
    print(output)
# TODO: Print z from a session