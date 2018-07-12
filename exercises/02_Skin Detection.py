"""
Exercise 2:
- Different color spaces: RGB, YCrCb, HSV
- Transform image to corresponding color space
- Apply skin detection to the input image

"""

import cv2
import numpy


def detect_skin():
    """
    Detect the skin from the image
    Transform the image to a different color space
    Define ranges in which skin detection is to be applied
    Apply a skin mask to the input image
    """


def main():
    cam = cv2.VideoCapture(0)

    while True:
        ret, frame = cam.read()

        # run the skin detection
        detect_skin()

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
