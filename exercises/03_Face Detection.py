"""
Exercise 3:
- Apply haar cascades for finding faces
- Track face with object tracking API from opencv
"""

import cv2


def init_detector():
    """
    Initialize the detector for our application
    """


def detect_face():
    """
    Transform the image to grayscale
    Run the detector on the image
    Visualize all detected faces
    """


def main():
    cam = cv2.VideoCapture(0)

    # initialize face detector
    init_detector()

    while True:
        ret, frame = cam.read()

        # run face detection with the detector
        detect_face()

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
