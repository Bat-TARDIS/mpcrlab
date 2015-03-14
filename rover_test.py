from rover import Rover20

import time
import pygame
import sys
import signal
import cv2

class roverMain(Rover20):

    def __init__(self):
        Rover20.__init__()
        self.window_name = "Rover 2.0 Hit Esc to Quit"
        self.quit = False

        try:
            if cv2:
                cv2.namedWindow(self.window_name, cv2.CV_WINDOW_AUTOSIZE)
            else:
                pass
        except:
            pass

    def video(self, jpegbytes, timestamp_10msec):
        image = cv2.VideoCapture(0)

        if cv2.waitKey(1) & 0xFF ==27 :
            self.quit = True







