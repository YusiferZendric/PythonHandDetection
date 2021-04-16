import cv2
import time
import os
import HandTrackingModule as htm
for i in range(1, 6):
    with open(f'FingerImages/{i}.txt', 'w') as f:
        f.write('False')

cap = cv2.VideoCapture(0)
ptime = 0

detector = htm.handDetector(detectionCon=0.75)
tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw=False)
    # print(lmlist)

    if len(lmlist) != 0:
        fingers = []
        score = 0
        for id in range(0, 5):
            if lmlist[tipIds[id]][2] < lmlist[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        if fingers[0] == 0:
            score = 0
            for j in fingers:
                score+=j


        elif fingers[0] == 1:
            temp_list = []
            for j in fingers:
                if j == 0:
                    temp_list.append(j)
            if len(temp_list) == 4:
                score = 6
            elif len(temp_list) == 0:
                score = 5
        print(score)
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv2.putText(img, f"FPS: {int(fps)}", (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

