import face_recognition
import cv2
import os


def learn_faces(path="../training/"):
    face_encodings = []
    face_names = []
    fileList = os.listdir(path)
    for fileName in fileList:
        face_image = face_recognition.load_image_file(path + fileName)
        encoding = face_recognition.face_encodings(face_image)[0]
        face_encodings.append(encoding)
        face_names.append(fileName.split(".")[0])

    return face_encodings, face_names


def recognize_learned_faces(img, known_face_encodings, known_face_names):
    # Find all the faces and face encodings in the unknown image
    face_locations = face_recognition.face_locations(img)
    face_encodings = face_recognition.face_encodings(img, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a box around the face
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)

        # Draw a label with a name below the face
        text_width, text_height = 500, 10
        cv2.rectangle(img, (left, bottom - text_height - 10), (right, bottom), (0, 255, 0), -1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, name, (left, bottom), font, 1, (120, 255, 120), 1, cv2.LINE_AA)

    return img


def main():
    known_encodings, know_names = learn_faces()
    test_image = cv2.imread("../testing/01.jpg")
    recognize_learned_faces(test_image, known_encodings, know_names)
    cv2.imshow("Result", test_image)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
