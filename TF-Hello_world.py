# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 20:15:00 2017

@author: Toshiharu
"""

import tensorflow as tf

# Create TensorFlow object called tensor
hello_constant = tf.constant('Hello World!')

with tf.Session() as sess:
    # Run the tf.constant operation in the session
    output = sess.run(hello_constant)
    print(output)