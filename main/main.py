"""Script to gather IMDB keywords from 2013's top grossing movies."""
import os
import sys
import math
import numpy
import cv2

def main():
    """Main entry point for the script."""

    ## INIT

    FPS = 30
    DIFF_METHOD = 'cv2.TM_CCOEFF_NORMED'
    DIFF_THRESHOLD = 0.9
    
    go_template = cv2.imread('image-assets/go.png', 1)
    game_template = cv2.imread('image-assets/game.png', 1)

    cv2.imshow('Go', go_template)
    cv2.imshow('Game', game_template)
    cv2.waitKey(1)


    ## GET CAPTURE

    vod_path = 'vods-to-split/fox-puff-game.mp4'

    cap = cv2.VideoCapture(vod_path)

    if cap.isOpened():
    	print "Video Opened\n"
    else:
    	print "Failed to open video\n"


   	## PROCESS

    while(cap.isOpened()):
    	
    	ret, frame = cap.read()

    	# check for go!
    	diff = cv2.matchTemplate(frame, go_template, eval(DIFF_METHOD))
    	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(diff)

    	if max_val > DIFF_THRESHOLD:
    		# Found the start of a game
    		cv2.imshow('Go! Frame', frame)

    	# check for game!
    	diff = cv2.matchTemplate(frame, game_template, eval(DIFF_METHOD))
    	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(diff)

    	if max_val > DIFF_THRESHOLD:
    		# Found the end of a game
    		cv2.imshow('Game! Frame', frame)

    	cv2.imshow('Press \'q\' to stop video', frame)
    	if cv2.waitKey(1) & 0xFF == ord('q'):
			break


   	## CLEANUP

    cap.release()
    cv2.destroyAllWindows()
    
    return 1


if __name__ == '__main__':
    sys.exit(main())