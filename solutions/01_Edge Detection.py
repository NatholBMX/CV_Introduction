"""
Exercise 1:
- Grab the input from your webcam
- Transform the image to grayscale
- Apply a threshold to it
- Apply edge detection to it
"""

import cv2
import numpy


def run_threshold(image, lower_boundary, upper_boundary, threshold_index=0):
    threshold_list = [cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV, cv2.THRESH_TRUNC, cv2.THRESH_TOZERO,
                      cv2.THRESH_TOZERO_INV]

    if threshold_index < 0 or threshold_index > 4:
        raise Exception("Threshold index out of bounds")

    retVal, thresh = cv2.threshold(image, lower_boundary, upper_boundary, threshold_list[threshold_index])

    return thresh


def run_edge_detection(image, detector_index=0):
    if detector_index < 0 or detector_index > 4:
        raise Exception("Detector index out of bounds")

    # Canny detector
    if detector_index == 0:
        # sigma parametr for Canny
        sigma = 0.33
        # compute the median of the single channel pixel intensities
        pixel_median = numpy.median(image)

        # apply automatic Canny edge detection using the computed median
        lower_bound = int(max(0, (1.0 - sigma) * pixel_median))
        upper_bound = int(min(255, (1.0 + sigma) * pixel_median))

        edge_image = cv2.Canny(image, lower_bound, upper_bound)

    # Laplacian edge detection
    elif detector_index == 1:
        edge_image = cv2.Laplacian(image, cv2.CV_64F)

    # Sobel edge detector in x-direction
    elif detector_index == 2:
        edge_image = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)

    # Sobel edge detector in y-direction
    elif detector_index == 3:
        edge_image = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)

    return edge_image


def main():
    cam = cv2.VideoCapture(0)

    while True:
        ret, frame = cam.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # apply the threshold
        thresh = run_threshold(gray, 120, 255, 4)

        edge = run_edge_detection(thresh, detector_index=3)

        cv2.imshow('frame', edge)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
