import numpy as np 
import cv2

cap = cv2.VideoCapture(0)

while(True):
	#capture frame by fram
	ret, frame = cap.read()
	
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	
	#Display the result
	
	cv2.imshow('frame', gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
#release capture
cap.release()
cv2.destroyAllWindows()