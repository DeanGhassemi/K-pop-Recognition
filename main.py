import cv2 # labelling and rectangles
import face_recognition # for recognizing faces
import os # iterate dir
import numpy as np

# Constants
KNOWN_FACES_DIR = "known_faces"
UNKNOWN_FACES_DIR = "unknown_faces"
TOLERANCE = 0.35
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
                    # Turns into Numpy Array
                    image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{name}/{filename}", mode="RGB")
                    encoding = face_recognition.face_encodings(image)[0]
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
        #print(results)
        match = None
        if True in results:
            trueArr = []
            matchMap = {}
            '''
            Checking for matches and counting the matches.
            That way, I can use the value of the key to see
            which member the unknown face resembles the most.

            and in the unlikely case that a member resembles two faces,
            it will go with the member that is not used yet
            '''
            for index in range(len(results)-1):
                if results[index] == np.True_:
                    trueArr.append(known_names[index])
                    if known_names[index] in matchMap:
                        matchMap[known_names[index]] += 1
                    else:
                        matchMap[known_names[index]] = 1
            for name in range(len(matchMap) - 1 ):
                if name in used_names:
                    del matchMap[name]
            
            match = max(matchMap, key=matchMap.get)
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
        if not filename.startswith('.'):  # Skip hidden files
            print("RAHHHH === " + filename)
            image = face_recognition.load_image_file(f"{UNKNOWN_FACES_DIR}/{filename}")
            image, used_names = label_faces(image, known_faces, known_names)
            cv2.imshow(filename, image)
            cv2.waitKey(0)
            cv2.destroyWindow(filename)