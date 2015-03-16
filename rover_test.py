import cv2
import StringIO
from rover import Rover20

class Tank(Rover20):
        def processVideo(self, jpegbytes):

            if cv2:
                image = StringIO.StringIO(jpegbytes)
                wname = 'Rover 2.0'
                cv2.NamedWindow(wname, cv2.CV_WINDOW_AUTOSIZE )
                cv2.ShowImage(wname, image )
                return image
                cv.WaitKey(5)
            else:
                pass

