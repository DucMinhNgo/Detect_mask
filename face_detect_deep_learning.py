import cv2
from mtcnn.mtcnn import MTCNN

# detect_faces use to detect face in the picture
detector = MTCNN()
image_input = cv2.imread("abba.png")
image = cv2.resize(image_input, (960, 540))
result = detector.detect_faces(image)
print (result)
for person in result:
    print (person)
    bounding_box = person['box']
    keypoints = person['keypoints']

    cv2.rectangle(image,
                  (bounding_box[0], bounding_box[1]),
                  (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
                  (0,255,0),
                  2)
    
    cv2.circle(image,(keypoints['left_eye']), 2, (0,255,0), 2)
    cv2.circle(image,(keypoints['right_eye']), 2, (0,255,0), 2)
    cv2.circle(image,(keypoints['nose']), 2, (0,255,0), 2)
    cv2.circle(image,(keypoints['mouth_left']), 2, (0,255,0), 2)
    cv2.circle(image,(keypoints['mouth_right']), 2, (0,255,0), 2)

cv2.imshow("image",image)
cv2.waitKey(0)
