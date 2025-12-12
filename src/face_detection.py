import cv2
face_object=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
webcam=cv2.VideoCapture(0)
while True:
    _,img=webcam.read()
    
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_object.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow("Face detection",img)
    key=cv2.waitKey(10)
    if key==81 or key==113:
        break
webcam.release()
cv2.destroyAllWindows()
