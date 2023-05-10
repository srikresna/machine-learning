import math
import time

import cv2 as cv
import mediapipe as mp


class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        # mode: static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        # Hand Tracking Module
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20] # Thumb, Index, Middle, Ring, Pinky

    def findHands(self, img, draw=True):
        # Convert to RGB
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        # Process the image
        self.results = self.hands.process(imgRGB)
        #print(results.multi_hand_landmarks)
        # Check if there is any hand in the image
        if self.results.multi_hand_landmarks:
            # For each hand
            for handLms in self.results.multi_hand_landmarks:
                # Draw the hand
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img
    
    def findPosition(self, img, handNo=0, draw=True):
        xList = []
        yList = []
        bbox = []
        # List of all hands
        self.lmList = []
        # Check if there is any hand in the image
        if self.results.multi_hand_landmarks:
            # Get the hand
            myHand = self.results.multi_hand_landmarks[handNo]
            # For each hand
            for id, lm in enumerate(myHand.landmark):
                #print(id, lm)
                # Get the pixel value of the landmark
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                #print(id, cx, cy)
                xList.append(cx)
                yList.append(cy)
                # Add the landmark to the list
                self.lmList.append([id, cx, cy])
                # Draw the landmarks
                if draw:
                    cv.circle(img, (cx, cy), 5, (255, 0, 255), cv.FILLED)
            # Get the bounding box
            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            bbox = xmin, ymin, xmax, ymax
            
            if draw:
                cv2.rectangle(img, (bbox[0]-20, bbox[1]-20),
                (bbox[2]+20, bbox[3]+20), (0, 255, 0), 2)

        return self.lmList, bbox

    def fingersUp(self):
        fingers = []
        # Thumb
        if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        # Other fingers
        for id in range(1, 5):
            # If the landmark is above the previous one
            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers
    
    def findDistance(self, p1, p2, img, draw=True, r=15, t=3):
        # Get the landmarks
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        # Get the center of the line
        cx, cy = (x1+x2)//2, (y1+y2)//2
        # Draw the line
        if draw:
            cv.line(img, (x1, y1), (x2, y2), (255, 0, 255), t)
            # Draw the points
            cv.circle(img, (x1, y1), r, (255, 0, 255), cv.FILLED)
            cv.circle(img, (x2, y2), r, (255, 0, 255), cv.FILLED)
            # Draw the center
            cv.circle(img, (cx, cy), r, (255, 0, 255), cv.FILLED)
        # Get the length of the line
        length = math.hypot(x2-x1, y2-y1)
        return length, img, [x1, y1, x2, y2, cx, cy]
    
def main():
    # Camera
    cap = cv.VideoCapture(0)
    # Time
    pTime = 0
    cTime = 0
    # Detector
    detector = handDetector()
    while True:
        # Get the image
        success, img = cap.read()
        # Find the hands
        img = detector.findHands(img)
        # Find the landmarks
        lmList, bbox = detector.findPosition(img)
        # Print the landmarks
        if len(lmList) != 0:
            print(lmList[4])
        # Calculate the FPS
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        # Show the FPS
        cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3,
        (255, 0, 255), 3)
        # Show the image
        cv.imshow("Image", img)
        # Wait for a key
        cv.waitKey(1)

#main

if __name__ == "__main__":
    main()

# End of file



