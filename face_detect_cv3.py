import cv2
import sys

# Get user supplied values
imagePath = sys.argv[1]

cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
input_image = cv2.imread(imagePath)
image = cv2.resize(input_image, (703, 373))
# image = cv2.resize(input_image, (960, 540))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(960, 540)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
)
# print (faces)
print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
