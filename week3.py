import cv2
import numpy as np
import sys
length = len(sys.argv)
print("If you want to see live video do (-live) or if you want to see a photo do (-pic)".str(sys.argv[1])
if sys.argv[1]=="-live":
	cv2.NamedWindow("-live", cv2.CV_WINDOW_AUTOSIZE)
	capture = cv2.CaptureFromCAM(0)
	While True:
		frame = cv2.QueryFrame(capture)
		cv2.ShowImage("Camera Feed",frame)
		key = cv2.waitKey(10)
		if key == 27:
			break
	cv2.destroyWindow("preview")
	else:
		print("Error")

elif sys.argv[1]=="-pic"
	fileLocation = "https://www.nasa.gov/sites/default/files/moon_and_earth_lroearthrise_frame_0.jpg"
	img =cv2.imread(fileLocation)
	cv2.imshow("Cool photo", img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

