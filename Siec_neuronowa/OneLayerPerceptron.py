from __future__ import print_function

import tensorflow as tf
import cv2
import numpy as np
from matplotlib import pyplot as plt

import os

# Import MNIST data
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

imageSize = 28, 28

show_weights = False
show_training_weights = False
save_weight_images = False
show_plots = False
jpeg_image = False
random_images = False
save_trained_model = True

batch_size = 20  #  1..N
num_epochs = 1000 #  1..N
step = 0.001     #  0..1

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

for i in range(num_epochs):
    #show weights in real time
    if show_training_weights:
        img_weight = sess.run(W)[:,2]
        img_weight = img_weight.reshape([28, 28])
                
        img_weight = cv2.resize(img_weight,(256,256))
        img_weight = np.multiply(img_weight,255)
        cv2.imshow("weight", img_weight);

        #write images on disk
        if save_weight_images:
            img_weight*=255

            directory = "output_imgs/"

            if not os.path.exists(directory):
                os.makedirs(directory)
            cv2.imwrite((directory + "{0}.jpg").format(i), img_weight)   

        cv2.waitKey(30);

    # load batch of images and correct answer
    bacth_X, batch_Y = mnist.train.next_batch(batch_size)
    train_data = {X: bacth_X, Y_: batch_Y}

    # load test batch of images and correct answer
    _bacth_X, _batch_Y = mnist.test.next_batch(int(batch_size/5))
    test_data = {X: _bacth_X, Y_: _batch_Y}
    
    # train
    sess.run(train_step, feed_dict=train_data)
    
    # find accuracy and cross entropy on current data
    a, c = sess.run([accuracy, cross_entropy], feed_dict=train_data)
    acc_train_li.append(a)
    cross_train_li.append(c)
    
    # find accuracy and cross entropy on test data
    a, c = sess.run([accuracy, cross_entropy], feed_dict=test_data)
    acc_test_li.append(a)
    cross_test_li.append(c)


print('Train Set Accuracy: '+str(acc_train_li[-1])+' \t Train Set cross-entropy Loss: '+str(cross_train_li[-1]))
print('Test Set Accuracy: '+str(acc_test_li[-1])+ '\t Test Set cross-entropy Loss: '+str(cross_test_li[-1]))

#save model weights
if save_trained_model is True:
    print("Saving OLP model.")
    saver = tf.train.Saver()
    directory = "model/olp_model.ckpt"

    if not os.path.exists(directory):
        os.makedirs(directory)

    # Save model weights to disk
    save_path = saver.save(sess, directory)
    print("Model saved in file: %s" % save_path)

    print("saved model: %s" % save_path)

#show Accuracy and cross entropy
if show_plots:
    plt.figure(1)
    plt.subplot(211)
    plt.plot(acc_train_li)
    plt.title('Accuracy: '+str(acc_train_li[-1]))

    plt.subplot(212)
    plt.plot(acc_train_li)
    plt.title('Cross entropy: '+str(cross_train_li[-1]))
    plt.show()


#show weights as images
if show_weights:
    for i in range(10):
        plt.subplot(3, 4, i+1)
        weight = sess.run(W)[:,i]
        plt.title(i)
        plt.imshow(weight.reshape([28, 28]))
        frame1 = plt.gca()

    plt.show()

#Run on test image  
if jpeg_image:
    cv2_image = 'img/examples/3.jpg' #  (0,1,3,5,9).jpg

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

    #show image and predicted label
    plt.title("Predicted class:"+ str(classification[0]))

    plt.imshow(image)
    plt.show()


#Run on random images 
if random_images: 
    for i in range(9):
        #load random image from dataset
        import random
        index = random.randint(0, 1000)
        _image = mnist.test.images[index]
        image = _image.reshape([28,28])

        #prediction
        classification = sess.run(tf.argmax(predict, 1), feed_dict={X: [_image]})

        predicted_class = str(classification[0])

        #show image and predicted label
        plt.subplot(3, 3, i+1)
        plt.title(predicted_class)
        plt.imshow(image)
        frame1 = plt.gca()

    plt.show()