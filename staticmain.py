from mtcnn import MTCNN
import cv2
detector = MTCNN()

img = cv2.imread(r"facedetection/5.jpg")
# img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
output = detector.detect_faces(img)

 

print(output)

for i in range(len(output)):

    x,y,w,h = output[i]['box']
    
    l_eyeX , l_eyeY = output[i]['keypoints']['left_eye']
    r_eyeX , r_eyeY = output[i]['keypoints']['right_eye']
    noseX , noseY = output[i]['keypoints']['nose']
    l_mouthX , l_mouthY = output[i]['keypoints']['mouth_left']
    r_mouthX , r_mouthY = output[i]['keypoints']['mouth_right']

    cv2.circle(img,center = (l_eyeX,l_eyeY),color = (233,123,56),thickness = 2 , radius = 1)
    cv2.circle(img,center = (r_eyeX,r_eyeY),color = (233,123,56),thickness = 2 , radius = 1)
    cv2.circle(img,center = (noseX,noseY),color = (233,123,56),thickness = 2 , radius = 1)
    cv2.circle(img,center = (l_mouthX,l_mouthY),color = (233,123,56),thickness = 2 , radius = 1)
    cv2.circle(img,center = (r_mouthX,r_mouthY),color = (233,123,56),thickness = 2 , radius = 1)

    cv2.rectangle(img,pt1= (x,y) , pt2 = (x+w , y+h) , color = (233,123,56),thickness = 3)


cv2.imshow('window',img)
cv2.waitKey(0)
