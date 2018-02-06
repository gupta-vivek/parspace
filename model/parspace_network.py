# -*- coding: utf-8 -*-
"""
@created on: 6/2/18,
@author: Vivek A Gupta,
@version: v0.0.1

Description:

Sphinx Documentation Status:

..todo::

"""
import tensorflow as tf

# Learning rate.
learning_rate = 0.01

# Epochs.
epochs = 10

# Display step.
display_step = 5

# Batch size.
batch_size = 1

# Read data.
# Todo read data from pickle file

# Input placeholder
x = tf.placeholder(tf.float32, [None, 56, 56, 3], name="Input")

# Output placeholder
y = tf.placeholder(tf.float32, [None, 3], name="Output")


# Convolution.
def conv2d(x, weights, biases, strides = 1):
    x = tf.nn.conv2d(x, weights, biases, strides=[1, strides, strides, 1], padding='SAME')
    x = tf.nn.bias_add(x, biases)

    return tf.nn.relu(x)


# Max Pooling.
def maxpool2d(x, k=2):
    return tf.nn.max_pool(x, ksize=[1, k, k, 1], strides=[1, k, k, 1], padding='SAME')

# Weights.
weights = {
    # 5 x 5 filter, 1 input, 32 outputs.
    'wc1': tf.Variable(tf.random_normal([5, 5, 1, 32])),
    # 5 x 5 filter, 32 inputs, 64 outputs.
    'wc2': tf.Variable(tf.random_normal([5, 5, 32, 64])),
    # Fully connected, 7 x 7 x 64 inputs, 1024 outputs.
    'wf1': tf.Variable(tf.random_normal([7*7*64, 1024])),
    # 1024 inputs, 10 outputs.
    'out': tf.Variable(tf.random_normal([1024, 3]))
}

# Biases.
biases = {
    'bc1': tf.Variable(tf.random_normal([32])),
    'bc2': tf.Variable(tf.random_normal([64])),
    'bf1': tf.Variable(tf.random_normal([1024])),
    'out': tf.Variable(tf.random_normal([1024, 3]))
}


# Model.
def model(x, weights, biases):

    # Layer 1.
    conv1 = conv2d(x, weights['wc1'], biases['bc1'])
    conv1 = maxpool2d(conv1, k=2)

    # Layer 2.
    conv2 = conv2d(conv1, weights['wc2'], biases['bc1'])
    conv2 = maxpool2d(conv2, k =2)

    # Fully connected layer.
    intermediate = tf.reshape(conv2, shape=[-1, 7*7*64])
    intermediate = tf.matmul(intermediate, weights['wf1'])
    intermediate = tf.add(intermediate, biases['bf1'])
    intermediate = tf.nn.relu(intermediate)

    # Output layer.
    out = tf.add(tf.matmul(intermediate, weights['out'], biases['out']))

    return out

y_ = model(x, weights, biases)

# Prediction.
pred = tf.nn.softmax(y_)

# Cost.
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y_, y))

# Optimizer.
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)

# Correct prediction.
correct_pred = tf.equal(tf.argmax(y, 1), tf.argmax(pred, 1))

# Accuracy.
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32)) * 100

# Initialize the variables.
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    for i in range(epochs):
        print("Epoch - ", i + 1)
        count = 0
        for train_data_input, train_label_input in zip(train_x, train_y):
            _, cost = sess.run([optimizer, cost], feed_dict = {x: train_data_input, y: train_label_input})

            if count % display_step == 0:
                print("Cost - ", c)
            count += 1

        for i in test_data:
            prediction = sess.run(pred, feed_dict = {x: [i]})