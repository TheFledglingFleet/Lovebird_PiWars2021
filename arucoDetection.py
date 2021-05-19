from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import sys

# define names of each possible ArUco tag OpenCV supports

arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_ARUCO_ORIGINAL)
arucoParams = cv2.aruco.DetectorParameters_create()

vs = VideoStream(src=0).start()
time.sleep(2.0)

while True:
  frame = vs.read()
  frame = imutils.resize(frame, width=1000)
  (corners, ids, rejected) = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams)
  if len(corners) > 0:
    ids = ids.flatten()
        
    for (markerCorner, markerID) in zip(corners, ids):
      corners = markerCorner.reshape((4, 2))
      (topLeft, topRight, bottomRight, bottomLeft) = corners
      topRight = (int(topRight[0]), int(topRight[1]))
      bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
      bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
      topLeft = (int(topLeft[0]), int(topLeft[1]))
      
      cv2.line(frame, topLeft, topRight, (0, 255, 0), 2)
      cv2.line(frame, topRight, bottomRight, (0, 255, 0), 2)
      cv2.line(frame, bottomRight, bottomLeft, (0, 255, 0), 2)
      cv2.line(frame, bottomLeft, topLeft, (0, 255, 0), 2)
      
      cX = int((topLeft[0] + bottomRight[0]) / 2.0)
      cY = int((topLeft[1] + bottomRight[1]) / 2.0)
      cv2.circle(frame, (cX, cY), 4, (0, 0, 255), -1)
      
      cv2.putText(frame, str(markerID),
	    (topLeft[0], topLeft[1] - 15),
		cv2.FONT_HERSHEY_SIMPLEX,
		0.5, (0, 255, 0), 2)
  cv2.namedWindow(frameName, cv2.WINDOW_NORMAL)
  cv2.imshow('Frame', frame)
  key = cv2.waitKey(1) & 0xFF # if the `q` key was pressed, break from the loop
  if key == ord("q"):
    break
        
cv2.destroyAllWindows()
vs.stop()