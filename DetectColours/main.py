# Colour identification
import cv2
import numpy as np

cap = cv2.VideoCapture(1) # change 1 to 0 to use your default webcam
mode = 'b'
while True:
	ret, frame = cap.read()

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_blue = np.array([110, 50, 50])
	upper_blue = np.array([130, 255, 255])

	lower_yellow = np.array([20, 50, 50])
	upper_yellow = np.array([40, 255, 255])

	lower_green = np.array([50, 50, 50])
	upper_green = np.array([70, 255, 255])

	if mode == 'b':
		mask = cv2.inRange(hsv, lower_blue, upper_blue)
	elif mode == 'y':
		mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
	elif mode == 'g':
		mask = cv2.inRange(hsv, lower_green, upper_green)

	contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	for contour in contours:
		area = cv2.contourArea(contour)
		if area > 500:
			x, y, w, h = cv2.boundingRect(contour)
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

	cv2.imshow('frame', frame)

	key = cv2.waitKey(1)

	if key == ord('q'):
		break
	if key == ord('b'):
		mode = 'b'
	elif key == ord('y'):
		mode = 'y'
	elif key == ord('g'):
		mode = 'g'

cap.release()
cv2.destroyAllWindows()