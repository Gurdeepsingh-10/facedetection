import cv2
from mtcnn import MTCNN

cap = cv2.VideoCapture(0)
detector = MTCNN()

while True :
    ret,frame = cap.read()
    output = detector.detect_faces(frame)

    for single_output in output:
        x,y,w,h = single_output['box']
    
        l_eyeX , l_eyeY = single_output['keypoints']['left_eye']
        r_eyeX , r_eyeY = single_output['keypoints']['right_eye']
        noseX , noseY = single_output['keypoints']['nose']
        l_mouthX , l_mouthY = single_output['keypoints']['mouth_left']
        r_mouthX , r_mouthY = single_output['keypoints']['mouth_right']

        cv2.circle(frame,center = (l_eyeX,l_eyeY),color = (233,123,56),thickness = 2 , radius = 1)
        cv2.circle(frame,center = (r_eyeX,r_eyeY),color = (233,123,56),thickness = 2 , radius = 1)
        cv2.circle(frame,center = (noseX,noseY),color = (233,123,56),thickness = 2 , radius = 1)
        cv2.circle(frame,center = (l_mouthX,l_mouthY),color = (233,123,56),thickness = 2 , radius = 1)
        cv2.circle(frame,center = (r_mouthX,r_mouthY),color = (233,123,56),thickness = 2 , radius = 1)

        cv2.rectangle(frame,pt1= (x,y) , pt2 = (x+w , y+h) , color = (233,123,56),thickness = 3)
    cv2.imshow('Window',frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()