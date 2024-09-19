import cv2 # labelling and rectangles
import face_recognition # for recognizing faces
import os # iterate dir
import numpy as np

# Constants
KNOWN_FACES_DIR = "known_faces"
UNKNOWN_FACES_DIR = "unknown_faces"
TOLERANCE = 0.37
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = 'hog'


known_faces = []
known_names = []

def load_knownFaces():
    for name in os.listdir(KNOWN_FACES_DIR):
        if not name.startswith('.'):
            for filename in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
                if not filename.startswith('.'):
                    image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{name}/{filename}")
                    image_arr = np.array(image)
                    encoding = face_recognition.face_encodings(image_arr)[0]
                    known_faces.append(encoding)
                    known_names.append(name)

def label_faces(image, known_faces, known_names):
    locations = face_recognition.face_locations(image, model=MODEL)
    encodings = face_recognition.face_encodings(image, locations)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) 

    # Prevent Duplicate Recognition
    used_names = set()
    for face_encoding, face_location in zip(encodings, locations):
        results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
        match = None
        if True in results:
            match = known_names[results.index(True)]
            if match not in used_names:
                match = known_names[results.index(True)]
                print(f"Match Found: {match}")
                # Drawing a rectangle on the face
                top_left = (face_location[3], face_location[0])
                bottom_right = (face_location[1], face_location[2])
                color = [0, 255, 0]
                cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)
                top_left = (face_location[3], face_location[2])
                bottom_right = (face_location[1], face_location[2]+22)
                cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)

                # Text
                cv2.putText(image, match, (face_location[3]+10, face_location[2]+15), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,0,255), FONT_THICKNESS)
                used_names.add(match)  # Add used name to set

    return image, used_names

if __name__ == "__main__":
    # Just seperating from the other stuff in terminal so it looks cleaner
    print("=========")
    # Checking file path
    print(os.getcwd())
    print("loading known faces")
    load_knownFaces()
    print("processing unknown faces")
    for filename in os.listdir(UNKNOWN_FACES_DIR):
        print(filename)
        if not filename.startswith('.'):  # Skip hidden files
            image = face_recognition.load_image_file(f"{UNKNOWN_FACES_DIR}/{filename}")
            image, used_names = label_faces(image, known_faces, known_names)

        cv2.imshow(filename, image)
        cv2.waitKey(0)
        cv2.destroyWindow(filename)