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

	STREAMER_FIRST_GAME_GUESS = 600
	HOW_MANY_FRAMES_THE_STREAMER_IS_WRONG_BY = 60

	GO_TEMPLATE   = cv2.imread('image-assets/go.png',   1)
	GAME_TEMPLATE = cv2.imread('image-assets/game.png', 1)
	_, TEMPLATE_WIDTH, TEMPLATE_HEIGHT = GO_TEMPLATE.shape[::-1]

	cap = cv2.VideoCapture('vods-to-split/fox-puff-set.mp4')
	fourcc = cv2.cv.CV_FOURCC(*'XVID')

	## SANITY

	# ensure all templates are the same size
	_, GAME_TEMPLATE_WIDTH, GAME_TEMPLATE_HEIGHT = GAME_TEMPLATE.shape[::-1]
	assert GAME_TEMPLATE_WIDTH == TEMPLATE_WIDTH and GAME_TEMPLATE_HEIGHT == TEMPLATE_HEIGHT

	# ensure capture successfully opened
	if cap.isOpened():
		print "Video Opened\n"
	else:
		print "Failed to open video\n"


	## PROCESS

	game_window = STREAMER_FIRST_GAME_GUESS - HOW_MANY_FRAMES_THE_STREAMER_IS_WRONG_BY
	if game_window < 0:
		game_window = 0

	for i in range(1, game_window):
		cap.read()

	i = 0
	game_count = 0
	in_game = False
	templates = {False:GO_TEMPLATE, True:GAME_TEMPLATE}
	while cap.isOpened():
		ret, frame = cap.read()
		if not ret:
			break

		if 'top_left' in locals():
			cropped_frame = frame[
				top_left[1] : top_left[1] + TEMPLATE_HEIGHT,
				top_left[0] : top_left[0] + TEMPLATE_WIDTH
				]
		else:
			cropped_frame = frame

		diff = cv2.matchTemplate(cropped_frame, templates[in_game], eval(DIFF_METHOD))
		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(diff)

		if max_val > DIFF_THRESHOLD:
			if not ('top_left' in locals()):
				top_left = max_loc
			in_game = not in_game
			if in_game:
				out = cv2.VideoWriter(str(game_count) + '.avi', -1, FPS, (frame.shape[1],frame.shape[0]))
			if not in_game:
				out.release()
				game_count += 1

		if not(i%30) or (not(i%5) and in_game):
			cv2.imshow('Press \'q\' to stop video', frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

		if in_game:
			out.write(frame)

		i += 1
		if 0xFF == ord('q'):
			break


	## CLEANUP

	cap.release()
	out.release()
	cv2.destroyAllWindows()

	return 1


if __name__ == '__main__':
	sys.exit(main())
