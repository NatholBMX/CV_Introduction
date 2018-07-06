"""
Simple script for testing Tensorflow installation.
"""

import tensorflow


def main():
    hello = tensorflow.constant('Hello, TensorFlow!')
    sess = tensorflow.Session()
    print(sess.run(hello))


if __name__ == '__main__':
    main()
