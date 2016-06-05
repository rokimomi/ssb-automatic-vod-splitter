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
    test_vid = 'C:/Users/amine/Desktop/ssb-automatic-vod-splitter/main/vods-to-split/character-screen-to-stage-screen.mp4'
    cap = cv2.VideoCapture(test_vid)

    if cap.isOpened():
    	print "Video Opened\n"
    else:
    	print "Failed to open video\n"

    ##### 



    while(cap.isOpened()):
    	ret, frame = cap.read()
    	# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    	cv2.imshow('frame',frame)
    	if cv2.waitKey(1) & 0xFF == ord('q'):
    		break
    		
    #####



    cap.release()
    cv2.destroyAllWindows()

	





def placeholder_function(url):
    """Return somethin or other"""
    pass


if __name__ == '__main__':
    sys.exit(main())