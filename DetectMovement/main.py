# Movement detection
import cv2

cap = cv2.VideoCapture(1) # change 1 to 0 to use your default webcam

while True:
	_, frame1 = cap.read()
	_, frame2 = cap.read()

	dst = cv2.absdiff(frame1, frame2)
	dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)

	blur = cv2.GaussianBlur(dst, (5, 5), 0)
	_, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

	contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	for contour in contours:
		area = cv2.contourArea(contour)
		if area > 4000:
			x, y, w, h = cv2.boundingRect(contour)
			cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 0, 255), 2)

	cv2.imshow('frame', frame1)

	if cv2.waitKey(1) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()