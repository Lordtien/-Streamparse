from __future__ import absolute_import, print_function, unicode_literals
from pprint import pprint
import cv2
# import imutils
from datetime import datetime
import time
import os
import itertools
from streamparse.spout import Spout

class Motion_Spout(Spout):
 	def initialize(self, stormconf, context):
		# URLs = "rtsp://admin:zencam123@192.168.1.202:554/videoMain"
		URLs = []
		os.chdir("/media/shivji/Mind Fresh/Entertainment/song")
		for fn in os.listdir('.'):
			URLs.append("/media/shivji/Mind Fresh/Entertainment/song/"+str(fn))
 		# pprint(URLs)
 		# input()
 		self.x = itertools.cycle(URLs)

 	def next_tuple(self):
 		URL = next(self.x)
 		self.emit([URL])

# if __name__=="__main__":
# 	Motion_Spout().initialize(1,2)