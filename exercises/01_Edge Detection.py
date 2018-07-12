"""
Exercise 1:
- Grab the input from your webcam
- Transform the image to grayscale
- Apply a threshold to it
- Apply edge detection to it
"""

import cv2
import numpy


def run_threshold():
    """
    Run a threshold on the image
    """


def run_edge_detection():
    """
    Detect edges on the image
    """


def main():
    cam = cv2.VideoCapture(0)

    while True:
        ret, frame = cam.read()

        # apply grayscale transformation here

        # run a threshold here
        run_threshold()

        # apply edge detection here
        run_edge_detection()

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
