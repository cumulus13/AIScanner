import cv2
import numpy as np
import face_recognition




img_rkamil = face_recognition.load_image_file('images/rkamil_1.jpg')
img_mark = face_recognition.load_image_file('images/mark_1.jpg')
img_jackma = face_recognition.load_image_file('images/jackma_1.jpg')
img_jokowi = face_recognition.load_image_file('images/jokowi_1.jpg')
img_juwoto = face_recognition.load_image_file('images/juwoto_1.jpg')
img_tera = face_recognition.load_image_file('images/tera_1.jpeg')

img_rkamil_test = face_recognition.load_image_file('images/rkamil_2.jpg')
img_mark_test = face_recognition.load_image_file('images/mark_2.jpg')
img_jackma_test = face_recognition.load_image_file('images/jackma_2.jpg')
img_jokowi_test = face_recognition.load_image_file('images/jokowi_2.jpg')
img_juwoto_test = face_recognition.load_image_file('images/juwoto_2.jpg')
img_tera_test = face_recognition.load_image_file('images/tera_3.jpg')

img_rkamil = cv2.cvtColor(img_rkamil, cv2.COLOR_BGR2RGB)
img_mark = cv2.cvtColor(img_mark, cv2.COLOR_BGR2RGB)
img_jackma = cv2.cvtColor(img_jackma, cv2.COLOR_BGR2RGB)
img_jokowi = cv2.cvtColor(img_jokowi, cv2.COLOR_BGR2RGB)
img_juwoto = cv2.cvtColor(img_juwoto, cv2.COLOR_BGR2RGB)
img_tera = cv2.cvtColor(img_tera, cv2.COLOR_BGR2RGB)

img_rkamil_test = cv2.cvtColor(img_rkamil_test, cv2.COLOR_BGR2RGB)
img_mark_test = cv2.cvtColor(img_mark_test, cv2.COLOR_BGR2RGB)
img_jackma_test = cv2.cvtColor(img_jackma_test, cv2.COLOR_BGR2RGB)
img_jokowi_test = cv2.cvtColor(img_jokowi_test, cv2.COLOR_BGR2RGB)
img_juwoto_test = cv2.cvtColor(img_juwoto_test, cv2.COLOR_BGR2RGB)
img_tera_test = cv2.cvtColor(img_tera_test, cv2.COLOR_BGR2RGB)

tera_loc = face_recognition.face_locations(img_tera)[0]
encodeTera = face_recognition.face_encodings(img_tera)[0]
cv2.rectangle(img_tera, (tera_loc[3], tera_loc[0]), (tera_loc[1], tera_loc[2]), (255, 0, 255), 2)

tera_loc_test = face_recognition.face_locations(img_tera_test)[0]
encodeTera_test = face_recognition.face_encodings(img_tera_test)[0]
cv2.rectangle(img_tera_test, (tera_loc_test[3], tera_loc_test[0]), (tera_loc_test[1], tera_loc_test[2]), (255, 0, 255), 2)

#cv2.imshow('Ridwan Kamil', img_rkamil)
#cv2.imshow('Mark Zuckerberg', img_mark)
#cv2.imshow('Jack Ma', img_jackma)
#cv2.imshow('Jokowi', img_jokowi)
#cv2.imshow('Juwoto', img_juwoto)
cv2.imshow('Tera Marlina', img_tera)
cv2.imshow('Tera Marlina test', img_tera_test)

result_tera = face_recognition.compare_faces([encodeTera], encodeTera_test)
print("result =", result_tera)

cv2.waitKey(0)
