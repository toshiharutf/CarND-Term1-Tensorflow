# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 01:22:03 2017

@author: Toshiharu
"""

# Solution is available in the other "solution.py" tab
import tensorflow as tf


def run():
    output = None
    logit_data = [2.0, 1.0, 0.1]
    logits = tf.placeholder(tf.float32)
    #logits = tf.multiply(logit_data,10)
    logits = tf.div(logit_data,10)
    
    # TODO: Calculate the softmax of the logits
    # softmax =     
    softmax = tf.nn.softmax(logits)
    with tf.Session() as sess:
        # TODO: Feed in the logit data
        # output = sess.run(softmax,    )
        output = sess.run(softmax)
    return output

print(run())