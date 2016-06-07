"""Script to gather IMDB keywords from 2013's top grossing movies."""
import os
import sys
import math
import numpy
import cv2


DIFF_METHOD = 'cv2.TM_CCOEFF_NORMED'
DIFF_THRESHOLD = 0.9

HOW_MANY_FRAMES_THE_STREAMER_IS_WRONG_BY = 60

GO_TEMPLATE = cv2.imread('image-assets/go.png', 1)
_, w, h = GO_TEMPLATE.shape[::-1]
GO_TEMPLATE_WIDTH = w
GO_TEMPLATE_HEIGHT = h

GAME_TEMPLATE = cv2.imread('image-assets/game.png', 1)
_, w, h = GAME_TEMPLATE.shape[::-1]
GAME_TEMPLATE_WIDTH = w
GAME_TEMPLATE_HEIGHT = h

def main():
	"""Main entry point for the script."""

	## INIT

	FPS = 30

	## GET CAPTURE

	vod_path = 'vods-to-split/fox-puff-game.mp4'

	cap = cv2.VideoCapture(vod_path)

	if cap.isOpened():
		print "Video Opened\n"
	else:
		print "Failed to open video\n"


	## PROCESS

	cap, top_left = initializeGameProcessing(cap, 600)
	cv2.waitKey(1)

	unprocessed_game = True

	while unprocessed_game:
		cap = processGame(cap, top_left);
		unprocessed_game, cap = findNextGame(cap, top_left)

	## CLEANUP

	input("Press Enter to continue...")

	cap.release()
	cv2.destroyAllWindows()

	return 1

# this function takes a timestamp and returns an object containing the information required to continue processing the vod
def initializeGameProcessing(cap, approximate_game_start):
	game_window = approximate_game_start - HOW_MANY_FRAMES_THE_STREAMER_IS_WRONG_BY
	if game_window < 0:
		game_window = 0

	for i in range(1, game_window):
		cap.read()

	while cap.isOpened():
		ret, frame = cap.read()
		assert ret

		diff = cv2.matchTemplate(frame, GO_TEMPLATE, eval(DIFF_METHOD))
		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(diff)

		if max_val > DIFF_THRESHOLD:
			return cap, max_loc

	print "Could not find a melee game start in the provided video"
	assert False


def findNextGame(cap, top_left):
	while cap.isOpened():
		ret, frame = cap.read()
		assert ret

		cropped_frame = frame[
			top_left[1]: top_left[1] + GO_TEMPLATE_HEIGHT,
			top_left[0]: top_left[0] + GO_TEMPLATE_WIDTH
		];

		diff = cv2.matchTemplate(cropped_frame, GO_TEMPLATE, eval(DIFF_METHOD))

		if diff > DIFF_THRESHOLD:
			cap = processGame(cap, top_left)
			return True, cap

	return False, cap

def processGame(cap, top_left):
	print cap.get(1)
	while cap.isOpened():
		ret, frame = cap.read()
		assert ret

		cropped_frame = frame[
			top_left[1]: top_left[1] + GO_TEMPLATE_HEIGHT,
			top_left[0]: top_left[0] + GO_TEMPLATE_WIDTH
		];

		diff = cv2.matchTemplate(cropped_frame, GAME_TEMPLATE, eval(DIFF_METHOD))

		if diff > DIFF_THRESHOLD:
			print cap.get(1)
			return cap

		cv2.imshow('Press \'q\' to stop video', frame)
		cv2.waitKey(1)
	print "Video ended without game end"
	assert False


if __name__ == '__main__':
	sys.exit(main())