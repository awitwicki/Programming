from __future__ import print_function

import tensorflow as tf
import cv2
import numpy as np
from matplotlib import pyplot as plt

import os

zmienna = "lalala"

def run(image_path):
    imageSize = 28, 28

    show_weights = True
    show_training_weights = True
    save_weight_images = False
    show_plots = True
    jpeg_image = True
    random_images = True
    save_trained_model = False

    batch_size = 20  #  1..N
    num_epochs = 10 #  1..N
    step = 0.005     #  0..1

    X = tf.placeholder(tf.float32, [None, 784])
    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))
    init = tf.global_variables_initializer()

    #prediction
    predict = tf.matmul(X, W) + b

    Y = tf.nn.softmax(tf.matmul(X, W) + b)
    Y_ = tf.placeholder(tf.float32, [None, 10])

    cross_entropy = -tf.reduce_sum(Y_ * tf.log(Y))

    is_correct = tf.equal(tf.arg_max(Y_, 1), tf.arg_max(Y, 1))
    accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))

    optimizer = tf.train.GradientDescentOptimizer(step)
    train_step = optimizer.minimize(cross_entropy)

    # init tensorflow variables
    sess = tf.Session()
    sess.run(init)

    # lists to hold train accuracy and cross-entropy
    acc_train_li = []
    cross_train_li = []

    # lists to hold test accuracy and cross-entropy
    acc_test_li = []
    cross_test_li = []

    saver = tf.train.Saver()
    # Restore model weights from previously saved model
    save_path = 'model/olp_model.ckpt'
    saver.restore(sess, save_path)
    print("Model restored from file: %s" % save_path)

    #Run on image  
    cv2_image = image_path 

    _image = cv2.imread(cv2_image)
    _image = cv2.resize(_image, (28,28)) #resize to 28x28 for neuron input compatibility
    _image = cv2.cvtColor(_image, cv2.COLOR_BGR2GRAY) #grayscale
    _image = _image.reshape([784])
    _image = np.multiply(_image, 1.0 / 255.0)
    image = _image.reshape([28,28])

    # print all 10 neurons output as array
    data_p = sess.run(predict, feed_dict={X: [_image]})
    print(data_p)

    #prediction
    classification = sess.run(tf.argmax(predict, 1), feed_dict={X: [_image]})

    return [data_p, classification]

r,d = run('img/photo.jpg')