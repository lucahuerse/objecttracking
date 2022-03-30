import cv2
import numpy as np
import csv

cap = cv2.VideoCapture("table_soccer_yellow.mp4")


def detect_ball():
    coords = []
    while True:
        ret, frame = cap.read()
        width = int(cap.get(3))
        height = int(cap.get(4))

        roi = frame[0:height, int(width/3)+30:int(2*width/3)+80]

        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)  # hue, saturation, value
        yellow_min = np.array([14, 130, 20])
        yellow_max = np.array([24, 255, 255])

        mask = cv2.inRange(hsv, yellow_min, yellow_max)

        result = cv2.bitwise_and(roi, roi, mask=mask)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(result, contours, -1, (0,255,0), 2)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area >= 30:
                c, r = cv2.minEnclosingCircle(cnt)
                cx, cy = int(c[0]), int(c[1])                                       
                cv2.circle(result, (cx, cy), int(r), (0, 255, 0), 2)
                cv2.circle(result, (cx, cy), 3, (0, 0, 255), cv2.FILLED)
                coords = coords + [(cx, cy)] 

                
        combo_image = cv2.addWeighted(roi, 0.8, result, 1, 1)


        cv2.imshow("region of interest", combo_image)


        key = cv2.waitKey(30)
        if key == ord('q'):
            break
    print(np.shape(frame))
    print(np.shape(frame[0]))
    print(np.shape(frame[0][0]))

    return coords


data = detect_ball()
cap.release()
cv2.destroyAllWindows()

header = ['x', 'y']

# with open('data.csv', 'w', encoding='UTF8', newline='\n') as f:
#     writer = csv.writer(f)

#     # write the header
#     writer.writerow(header)

#     # write multiple rows
#     writer.writerows(data)

