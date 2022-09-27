import cv2
import numpy as np
import face_recognition
import os
from pydebugger.debug import debug


path_base = 'images_base'
path = "images"
images = []
classNames = []
list_image = os.listdir(path_base)
debug(list_image = list_image, debug = True)
for i in list_image:
    curImg = cv2.imread(f'{path_base}/{i}')
    images.append(curImg)
    classNames.append(os.path.splitext(i)[0])
    
def find_encoding(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encoding_list = find_encoding(images)
#debug(encoding_list = encoding_list, debug = True)
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
count = 0

while 1:
    success, img = cap.read()
    #print("success =", success)
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    
    face = face_recognition.face_locations(imgS)
    encoding = face_recognition.face_encodings(imgS, face)
    
    for encodingFace, faceLoc in zip(encoding, face):
        matches = face_recognition.compare_faces(encoding_list, encodingFace)
        faceDis = face_recognition.face_distance(encoding_list, encodingFace)
        
        matchIndex = np.argmin(faceDis)
        
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2 - 35), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            
    cv2.imshow('Webcam', img)
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        #cv2.imwrite("Resources/Scanned/NoPlate_"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,
                    2,(0,0,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count +=1    