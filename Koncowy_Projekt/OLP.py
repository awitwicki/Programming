import tensorflow as tf
import cv2
import numpy as np

def run(image_path):
    X = tf.placeholder(tf.float32, [None, 784])
    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))
    init = tf.global_variables_initializer()

    #prediction
    predict = tf.matmul(X, W) + b

    Y = tf.nn.softmax(tf.matmul(X, W) + b)
    Y_ = tf.placeholder(tf.float32, [None, 10])

    # init tensorflow variables
    sess = tf.Session()
    sess.run(init)

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
