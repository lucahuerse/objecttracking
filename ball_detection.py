import cv2
import numpy as np

cap = cv2.VideoCapture("table_soccer_yellow.mp4")
# cap = cv2.VideoCapture(0)


def detect_ball():
    while True:
        ret, frame = cap.read()
        width = int(cap.get(3))
        height = int(cap.get(4))

        roi = frame[0:height, int(width/3)+30:int(2*width/3)+80]

        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)  # hue, saturation, lightness
        lower_yellow = np.array([14, 130, 20])
        upper_yellow = np.array([24, 255, 255])

        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

        result = cv2.bitwise_and(roi, roi, mask=mask)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        coords = []

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 30:
                c, r = cv2.minEnclosingCircle(cnt)
                cx, cy = int(c[0]), int(c[1])
                cv2.circle(result, (cx, cy), int(r), (0, 255, 0), 2)
                cv2.circle(result, (cx, cy), 3, (0, 0, 255), cv2.FILLED)
                coords = coords + [cx, cy]
                print(coords)

        cv2.imshow("Region of Interest", roi)
        cv2.imshow("Result", result)

        key = cv2.waitKey(30)
        if key == ord('q'):
            break
    return coords

detect_ball()
cap.release()
cv2.destroyAllWindows()
