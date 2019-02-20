
# import the necessary packages
from imutils.video import VideoStream
from imutils import face_utils

import pygame,dlib,time,cv2,os
pygame.init()

shape_predictor="shape_predictor_68_face_landmarks.dat" 

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(shape_predictor)


vs = VideoStream(src=0).start()


j=0
dist_smilo=0
dist_leyeo=0
dist_reyeo=0
dist_ango=0
dup1,dup2=0,0
diff_chx,diff_chy=0,0
pid=0
count_smile,count_eact,count_be,count_ang=0,0,0,0

while True:
        
        
        frame = vs.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        rects = detector(gray, 0)
        diff_smile=0
        diff_ang=0
        diff_leye=0
        diff_eye=0
        diff_reye=0
        diff_up=0
        diff_change=0
        
        
        cv2.imshow("Frame", frame)
        x49=0
        y49=0
        x52=0
        y52=0
        x58=0
        y58=0
        x23=0
        y23=0
        x22=0
        y22=0
        x38=0
        y38=0
        x41=0
        y41=0
        x44=0
        y44=0
        x47=0
        y47=0
        x65=0
        y65=0
        print('Suprise,count_smile,count_be,Anger',count_eact,count_smile,count_be,count_ang)
        if count_smile>4:
                pygame.mixer.music.load('Smile.mp3')
                pygame.mixer.music.play(0,4)
        if count_ang>2:
                pygame.mixer.music.load('Anger.mp3')
                pygame.mixer.music.play(0,0)            
        elif count_be>15:
                pygame.mixer.music.load('Neutral.mp3')
                pygame.mixer.music.play(0,52)
        
        elif count_eact>4:
                pygame.mixer.music.load('Suprise.mp3')
                pygame.mixer.music.play(0,0)
                
        e,s,le,a,re,be=0,0,0,0,0,0
        for rect in rects:
                


                shape = predictor(gray, rect)
                shape = face_utils.shape_to_np(shape)

             
                i=1
                print('iter'+str(j))
                x1,y1=0,0
                j=j+1
                for (x, y) in shape:
                        #print(i)
                        cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)

                        #print(x,y)
                        if(i):
                                cv2.putText(frame, str(i), (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0,255,0), 1)
                        #if j==1:
                        if i==1:
                                x1=x
                                y1=y
                                
                                
                                if j%2!=0:
                                        dup1=x1
                                        dup2=y1
                                        print('dup',dup1,dup2)
                                        diff_chx,diff_chy=0,0
                                else:
                                        diff_chx=dup1-x1
                                        print(dup1)
                                        
                                        print('change',diff_chx)
                                        diff_chy=dup2-y1
                                        print(dup2)
                                        
                                        print('change',diff_chy)

                        elif i==20:
                                if j%2!=0:
                                        y_20=y-y1
                                        print(y_20)
                                else:
                                        y20=y-y1
                                        diff_up=y_20-y20
                                        print(y20,diff_up)
                                        
                                                   
                                                       
                        elif(i==49):
                                x49=x
                                y49=y
                                                  
                        elif(i==65):
                                x65=x
                                y65=y

                                dist_smile=((x49-x65)**2+(y49-y65)**2)**0.5
                                print('dist-smile',dist_smile)
                                diff_smile=(dist_smile)-dist_smilo
                                if diff_smile<0:
                                        diff_smile*=-1

                                print('diff-smile',diff_smile)
                                
                                print('dist-smilo',dist_smilo)
                                if j==1 or diff_smile>15:
                                        dist_smilo=dist_smile
                                        
                                        
                                if diff_smile<6:
                                        dist_smilo=(dist_smilo+dist_smile)//2

                        elif(i==38):
                                x38=x
                                y38=y
                        elif(i==41):
                                x41=x
                                y41=y
                                dist_leye=((x38-x41)**2+(y38-y41)**2)**0.5
                                print('dist-lefteye',dist_leye)
                                diff_leye=(dist_leye)-dist_leyeo

                                if diff_leye<0:
                                        diff_leye=diff_leye*-1

                                print('diff-leye',diff_leye)
                                
                                print('dist-leyeo',dist_leyeo)
                                if j==1 or diff_leye>2:
                                        dist_leyeo=dist_leye
                                        
                                        
                                if diff_leye<1:
                                        dist_leyeo=(dist_leyeo+dist_leye)//2                                
                        elif(i==44):
                                x44=x
                                y44=y
                        elif(i==47):
                                x47=x
                                y47=y
                                dist_reye=((x44-x47)**2+(y44-y47)**2)**0.5
                                print('dist-reye',dist_reye)
                                diff_reye=(dist_reye)-dist_reyeo

                                if diff_reye<0:
                                        diff_reye=diff_reye*-1

                                print('diff-reye',diff_reye)
                                
                                print('dist-reyeo',dist_reyeo)
                                if j==1 or diff_reye>2:
                                        dist_reyeo=dist_reye
                                print('check both')
                                print(diff_leye,diff_reye)
                                diff=(dist_reye-dist_leye)-(dist_reyeo-dist_leyeo)
                                if diff<0:
                                        diff=diff*-1
                                if diff_leye+diff_reye>2 and diff_leye+diff_reye<4 and (diff<0.5):
                                        print('check both')
                                        diff_eye=1
                                        
                                if diff_leye>2.5 and diff_reye>2.5 and j!=1:
                                        print('check both')
                                        print(diff_leye,diff_reye)
                                        
                                if diff_reye<1:
                                        dist_reyeo=(dist_reyeo+dist_reye)//2   
        
                        elif(i==22):
                                x22=x
                                y22=y
                        elif(i==23):
                                x23=x
                                y23=y
                                dist_ang=((x22-x23)**2+(y22-y23)**2)**0.5
                                print('dist-ang',dist_ang)
                                diff_ang=(dist_ang)-dist_ango
                                if diff_ang<0:
                                        diff_ang*=-1
                                print('diff-ang',diff_ang)
                                
                                print('dist-ango',dist_ango)
                                if j==1:
                                        dist_ango=dist_ang
                                        
                                        
                                if diff_ang<=5:
                                        dist_ango=(dist_ango+dist_ang)//2
                       
                        if diff_chx<10 and diff_chy<10:
                                
                                if diff_smile>10 and diff_smile<50 and j!=1:
                                        s=1
                                        cv2.imshow("smiling", frame)
                                        cv2.putText(frame,'Smile', (50, 50),cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 1)
                                
                                elif diff_ang>4 and j!=1:
                                        a=1
                                        cv2.putText(frame,'Anger', (50, 50),cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 1)
                                        cv2.imshow("Angry",frame)
                                        
                                        print('Anger')

                                elif diff_up>3:
                                        cv2.imshow("Suprise",frame)
                                        cv2.putText(frame,'Suprise', (50, 50),cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 1)
                                        e=1

                                elif diff_eye==1: 
                                        print('Neutral')
                                        cv2.imshow("Neutral",frame)
                                        cv2.putText(frame,'Neutral', (50, 50),cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 1)
                                        be=1
                                        
                                        

                        i=i+1
        if s:
                pygame.mixer.music.load('Smile.mp3')
                pygame.mixer.music.play(0,4)                
                print('Smile')
                count_smile=count_smile+1
        elif a:
                pygame.mixer.music.load('Anger.mp3')
                pygame.mixer.music.play(0,0)                
                print('Anger')
                count_ang=count_ang+1
        elif e:
                print('Suprise')
                count_eact=count_eact+1
        
        elif be:
                print('Neutral')
                count_be=count_be+1
               
        cv2.imshow("Frame", frame)
       
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord("q"):
            break
        
 
VideoStream(src=0).stop()

cv2.destroyAllWindows()
