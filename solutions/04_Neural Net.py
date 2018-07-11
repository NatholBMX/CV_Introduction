"""
Exercise 1:
- Grab the input from your webcam
- Transform the image to grayscale
- Apply a threshold to it
- Apply edge detection to it
"""

import face_recognition
import cv2
import numpy


def recognize_face(img):
    face_locations = face_recognition.face_locations(img, number_of_times_to_upsample=0, model="cnn")

    for face_location in face_locations:
        # Print the location of each face in this image
        top, right, bottom, left = face_location
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)

    return img

def main():
    cam = cv2.VideoCapture(0)

    while True:
        ret, frame = cam.read()
        recognize_face(frame)


        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
