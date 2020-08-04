# This script will detect faces via your webcam.
# Tested with OpenCV3

import cv2
from mtcnn.mtcnn import MTCNN
import torch
torch.cuda.is_available()

detector = MTCNN()
cap = cv2.VideoCapture(0)


while(True):
    # Capture frame-by-frame
    ret,frame = cap.read()
    # print (frame)
    #Use MTCNN to detect faces
    result = detector.detect_faces(frame)
    for person in result:
        bounding_box = person['box']
        keypoints = person['keypoints']

        cv2.rectangle(frame,
                  (bounding_box[0], bounding_box[1]),
                  (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
                  (0,155,255), 2)
        cv2.circle(frame,(keypoints['left_eye']), 2, (0,155,255), 2)
        cv2.circle(frame,(keypoints['right_eye']), 2, (0,155,255), 2)
        cv2.circle(frame,(keypoints['nose']), 2, (0,155,255), 2)
        cv2.circle(frame,(keypoints['mouth_left']), 2, (0,155,255), 2)
        cv2.circle(frame,(keypoints['mouth_right']), 2, (0,155,255), 2)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()