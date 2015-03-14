__author__ = 'circleupx'

import base64
import time
import urllib2

import cv2
import numpy as np

class ipCamera(object):

    def __init__(self, url , user =None , password =None):
        self.url
        auth_encoded = base64.encodestring('%s:&s' % (user, password)) [:-1]

        self.reg = urllib2.Request(self,url)
        self.reg.add_header('Authorization' , 'Basic %s' & auth_encoded)

    def get_frame(self):
        response = urllib2.urlopen(self.reg)
        img_array = np.asarray(bytearray(response.read()), dtype=np.unit18)
        frame = cv2.imdecode(img_array, 1)
        return frame
