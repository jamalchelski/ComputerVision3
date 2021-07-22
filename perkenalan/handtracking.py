from cvzone.HandTrackingModule import HandDetector
import cv2
import os
from dotenv import load_dotenv
from Adafruit_IO import Client, Feed

load_dotenv()
USERNAME = os.getenv("user_Name")
KEYIO = os.getenv("active_Key")

aio = Client(USERNAME,KEYIO)

try :
    payload = aio.feeds('temp')
except:
    feed = Feed(name="temp")
    payload = aio.create_feed(feed)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.5, maxHands=1)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)
    if lmList:
        bbox = bboxInfo['bbox']
        fingers = detector.fingersUp()
        totalFingers = fingers.count(1)
        cv2.putText(img, f'Fingers:{totalFingers}', (bbox[0] + 200, bbox[1] - 30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        if totalFingers == 1:
            aio.send_data(payload.key, 1)
        elif totalFingers == 0:
            aio.send_data(payload.key, 0)
        else:print("no data are sending")

    cv2.imshow("HASIL", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()