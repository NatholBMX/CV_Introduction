"""
Exercise 2:
- Different color spaces: RGB, YCrCb, HSV
- Transform image to corresponding color space
- Apply skin detection to the input image

"""

import cv2
import numpy


def detect_skin(image, color_space_index=0, preprocess=False):
    if color_space_index < 0 or color_space_index > 2:
        raise Exception("Color Space index out of bounds")

    color_space_list = ["rgb", "ycc", "hsv"]
    if color_space_index == 0:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # constants for finding range of skin color in RGB
        lower_boundary = numpy.array([131, 85, 36], numpy.uint8)
        upper_boundary = numpy.array([255, 205, 150], numpy.uint8)
    elif color_space_index == 1:
        # convert image to YCC:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)
        # Constants for finding range of skin color in YCrCb
        lower_boundary = numpy.array([80, 150, 77], numpy.uint8)
        upper_boundary = numpy.array([255, 173, 127], numpy.uint8)
    elif color_space_index == 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # intensities to be considered 'skin'
        lower_boundary = numpy.array([0, 48, 80], dtype="uint8")
        upper_boundary = numpy.array([20, 255, 255], dtype="uint8")

    # Find region with skin tone in YCrCb image
    skinRegion = cv2.inRange(image, lower_boundary, upper_boundary)

    if preprocess:
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
        skinRegion = cv2.erode(skinRegion, kernel, iterations=2)
        skinRegion = cv2.dilate(skinRegion, kernel, iterations=2)

    skin = cv2.bitwise_and(image, image, mask=skinRegion)
    if color_space_index == 0:
        resultImage = cv2.cvtColor(skin, cv2.COLOR_RGB2BGR)
    elif color_space_index == 1:
        resultImage = cv2.cvtColor(skin, cv2.COLOR_YCrCb2BGR)
    elif color_space_index == 2:
        resultImage = cv2.cvtColor(skin, cv2.COLOR_HSV2BGR)

    return resultImage


def main():
    cam = cv2.VideoCapture(0)

    while True:
        ret, frame = cam.read()

        skin = detect_skin(frame, color_space_index=2, preprocess=True)
        cv2.imshow('frame', skin)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
