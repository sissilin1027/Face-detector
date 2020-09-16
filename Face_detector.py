import cv2


# import trained algorithm
trained_face_data = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml')

img = cv2.imread("avb.png")

# caputre from webcam
# webcam = cv2.VideoCapture(0)
# while True:
#     successful_frame_read, frame = webcam.read()
#     grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     for (x, y, w, h) in face_coordinates:
#         cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

#     cv2.imshow("Detective Baby Yoda, grayscaled_img")
#     cv2.waitKey(1)

# greyscale
greyscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect face
face_coordinates = trained_face_data.detectMultiScale(greyscaled_img)

for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Detective baby yoda", img)
cv2.waitKey()

print("hello by")
