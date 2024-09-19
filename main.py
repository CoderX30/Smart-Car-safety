import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot
import time

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)
plotY = LivePlot(640, 360, [20, 50])

idList = [22, 23, 24, 26, 110, 157, 158, 159, 160, 161, 130, 243]
ratioList = []
blinkCounter = 0
blinkDetected = False

while True:
    success, img = cap.read()
    
    img, faces = detector.findFaceMesh(img, draw=False)
    
    if faces:
        face = faces[0]
        # for id in idList:
        #     cv2.circle(img, face[id], 5, (255, 255, 0), cv2.FILLED)

        leftup, leftdown, leftLeft, leftRight = [face[i] for i in [159, 23, 130, 243]]

        lengthVer, _ = detector.findDistance(leftup, leftdown)
        lengthHor, _ = detector.findDistance(leftLeft, leftRight)

        # cv2.line(img, leftup, leftdown, (0, 200, 0), 3)
        # cv2.line(img, leftLeft, leftRight, (0, 200, 0), 3)

        ratio = int((lengthVer / lengthHor) * 100)
        ratioList.append(ratio)
        ratioList = ratioList[-10:]                 # Keep only the last 10 elements
        ratioAvg = sum(ratioList) / len(ratioList)

        # Check if the ratio indicates closed eyes
        if ratioAvg < 28:
            if not blinkDetected:  # If the eyes were not already detected as closed
                blinkCounter += 1
                blinkDetected = True
                blinkStartTime = time.time()  # Record the time when the eyes were first detected as closed
            else:
                # Check if the eyes have been closed for more than 2 seconds
                if time.time() - blinkStartTime > 0.3:
                    cvzone.putTextRect(img, "ALERT!!!", (50, 150), scale=2, thickness=2, colorR=(0, 0, 255))

        else:
            blinkDetected = False  # Eyes are open again

        # cvzone.putTextRect(img, f'Blink Count: {blinkCounter}', (50, 100))

        imgplot = plotY.update(ratioAvg)
        imgstack = cv2.resize(img, (640, 360))
        combined_img = cvzone.stackImages([imgstack, imgplot], 1, 1)
    else:
        imgstack = cv2.resize(img, (640, 360))
        combined_img = cvzone.stackImages([imgstack, imgstack], 1, 1)

    cv2.imshow("Image", combined_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
