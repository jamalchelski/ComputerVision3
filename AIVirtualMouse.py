import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy


camH, camW = 640, 480
frameR = 50

cap = cv2.VideoCapture(0)
cap.set(3,camH)
cap.set(4,camW)
pTime = 0

detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()
# print(wScr,hScr)
while True:
    success, img =cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    if len(lmList)!=0:

        cv2.rectangle(img,(frameR,frameR),(camW-frameR, camH-frameR),
                      (255,0,255),2)
        x1,y1 =lmList[8][1:]
        x2,y2 =lmList[12][1:]
        # print(x1,y1,x2,y2)

        fingers = detector.fingersUp()
        # print(finger)

        if(fingers[1]==1 and fingers[2] ==0 ):
            x3 = np.interp(x1,(0,camW),(0,wScr))
            y3 = np.interp(y1,(0,camH),(0,hScr))

            autopy.mouse.move(wScr-x3,y3)
            cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime =cTime
    cv2.putText(img,str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,
                (255,0,0 ),3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
