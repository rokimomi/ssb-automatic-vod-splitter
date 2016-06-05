# ssb-automatic-vod-splitter

## Running

From project root:

1.
`virtualenv env`

2.
`source env/bin/activate` <- mac/linux
or...
`source env/Scripts/activate` <- windows

3.
`pip install -r requirements.txt`

4.
install open cv:
`pip install opencv_python-3.1.0-cp27-cp27m-win32.whl`

5.
`cd main`
`python main.py`


## Todo

make short 10 second video in dolphin/obs (character select screen to stage select)
capture two full frames from video and attempt to locate when they are in the parent video
capture partial image specific to a particular time (like something from the character select screen and something from the stage select) and locate their time in the clip

Capture sample video in mp4 format from dolphin that showcases 2 matches. Both matches go to character select screen > game! > back to character select screen.

###the ultimate test...###
7 hour vgbc vod
