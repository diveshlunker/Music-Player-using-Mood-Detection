import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

def detect(gray, frame):
    
    faces=face_cascade.detectMultiScale(gray, 1.3 , 5)
    
    for(x,y,w,h) in faces:
        
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0),2)  
        roi_gray = gray[y:y+h,x:x+w]
        roi_frame = frame[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray,1.3,10)
        smile=smile_cascade.detectMultiScale(roi_gray,1.7,15)
        
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_frame, (ex,ey), (ex+ew,ey+eh), (0,0,255),2)
        
        for(sx,sy,sw,sh) in smile:
            cv2.rectangle(roi_frame, (sx,sy), (sx+sw,sy+sh), (0,255,0),2)
            
    return frame

vid_cap = cv2.VideoCapture(0)

while(True):
    _,frame = vid_cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canvas=detect(gray,frame)
    cv2.imshow('Video',canvas)

    if(cv2.waitKey(1)& 0xFF==ord('q')):
        break
    
vid_cap.release()
cv2.destroyAllWindows()


"""

import cv2

def findmouth(img):

    haarFace = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    haarMouth = cv2.CascadeClassifier('haarcascade_mouth.xml')
    detectedFace = HaarFace.detectMultiScale(gray, 1.3 , 5)
    detectedMouth = cv2detectMultiScale(gray, 1.3 , 5)
    
      
    maxFaceSize = 0
    maxFace = 0
    if detectedFace:
        for face in detectedFace:
            if face[0][3]* face[0][2] > maxFaceSize:
                maxFaceSize = face[0][3]* face[0][2]
                maxFace = face
      
    if maxFace == 0:
        return 2
    
    def mouth_in_lower_face(mouth,face):
        if (mouth[0][1] > face[0][1] + face[0][3] * 3 / float(5) and mouth[0][1] + mouth[0][3] < face[0][1] + face[0][3] and abs((mouth[0][0] + mouth[0][2] / float(2)) - (face[0][0] + face[0][2] / float(2))) < face[0][2] / float(10)):
            return True
        else:
            return False
    
    filteredMouth = []
    if detectedMouth:
        for mouth in detectedMouth:
            if mouth_in_lower_face(mouth,maxFace):
                filteredMouth.append(mouth) 
      
    maxMouthSize = 0
    for mouth in filteredMouth:
        if mouth[0][3]* mouth[0][2] > maxMouthSize:
            maxMouthSize = mouth[0][3]* mouth[0][2]
            maxMouth = mouth
          
    try:
        return maxMouth
    except UnboundLocalError:
        return 2x

"""
