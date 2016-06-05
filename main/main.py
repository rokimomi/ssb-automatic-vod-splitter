"""Script to gather IMDB keywords from 2013's top grossing movies."""
import sys
import math
import numpy
import cv2

def main():
    """Main entry point for the script."""

    FPS = 30
    DIFF_METHOD = 'cv2.TM_CCOEFF_NORMED'
    DIFF_THRESHOLD = 0.9

    # test_vid = 'character-ss-to-stage-ss.mp4'
    test_vid = 'C:/Users/amine/Desktop/ssb-automatic-vod-splitter/main/vods-to-split/character-ss-to-stage-ss.mp4'
    cap = cv2.VideoCapture(test_vid)

    if cap.isOpened():
    	print "Device Opened\n"
    else:
    	print "Failed to open video\n"

    # 

    # print cap
    # ret, frame = cap.read()
    # print ret 
    # print frame
    # print cap.read()

    #

    cap.release()
    cv2.destroyAllWindows()

	





def placeholder_function(url):
    """Return somethin or other"""
    pass


if __name__ == '__main__':
    sys.exit(main())