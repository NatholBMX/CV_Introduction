import face_recognition
import cv2
import os


def learn_faces():
    """
    Learn all the faces specified in the path
    """


def recognize_learned_faces():
    """
    Recognize and visualize all the faces in an unkown image with the know faces
    """


def main():
    # run the algorithm to learn the faces
    learn_faces()

    # load up a test image
    test_image = cv2.imread("../testing/01.jpg")

    # recognize all the faces from the test image
    recognize_learned_faces()

    # visualize the result
    cv2.imshow("Result", test_image)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
