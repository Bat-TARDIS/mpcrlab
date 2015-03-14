import numpy as np
import cv2
cap = cv2.VideoCapture()
cap.open("http://192.168.1.100/")

while(1):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2GRAY)

    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()