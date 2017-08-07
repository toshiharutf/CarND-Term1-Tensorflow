# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 20:45:21 2017

@author: Toshiharu
"""
import tensorflow as tf


def run():
    output = None
    x = tf.placeholder(tf.string)
    y = tf.placeholder(tf.int32)

    with tf.Session() as sess:
        # TODO: Feed the x tensor 123
        output = sess.run(x, feed_dict={x:'Hello world', y: 123})

    return output

print(run())