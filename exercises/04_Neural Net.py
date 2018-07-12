"""
Exercise 1:
- Grab the input from your webcam
- Transform the image to grayscale
- Apply a threshold to it
- Apply edge detection to it
"""

import face_recognition
import cv2


def recognize_face():
    """
    Run the face recognition with the API
    Visualize all found faces
    """


def main():
    cam = cv2.VideoCapture(0)

    while True:
        ret, frame = cam.read()

        # run the face recognition
        recognize_face()

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
