"""
Exercise 1:
- Apply haar cascades for finding faces
- Track face with object tracking API from opencv
"""

import cv2


# absolute path needed for cascade classifier


def init_detector(detector_index=0):
    if detector_index < 0 or detector_index > 1:
        raise Exception("Detector index out of bounds")

    if detector_index == 0:
        detector_path = "C:\\Users\\nwaller\\Documents\\CV_Introduction\\exercises\\detector\\haarcascade_frontalface_default.xml"
        classifier = cv2.CascadeClassifier(detector_path)
    elif detector_index == 1:
        detector_path = "C:\\Users\\nwaller\\Documents\\CV_Introduction\\exercises\\detector\\lbpcascade_frontalface.xml"
        classifier = cv2.CascadeClassifier(detector_path)
    return classifier


def detect_face(classifier, image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = classifier.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)


def main():
    cam = cv2.VideoCapture(0)

    # initialize classifier
    classifier = init_detector(detector_index=1)

    while True:
        ret, frame = cam.read()

        detect_face(classifier, frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
