# Super Smash Brothers Automatic Vod Splitter

## Goals & Usecase

This project aims to automate the splitting of long tournament captures (8+ hours) of games in the Super Smash Brothers series. The end goal is to provide as much automation and naming assistance in the creation of these smaller sets as possible and to eventually upload them to YouTube

###Usecase 1:

After a long 8 hour day of streaming a local weekly, the streamer can input their saved vod into this application and not have to spend several more hours just to separate out the videos they were just watching/streaming all day.

###Usecase 2:

A local streamer has been streaming quite a few tournaments and has several saved vods but the matches for those tournaments have not been uploaded to youtube for one reason or another. After quite a few tournaments, the work has piled up and no one wants to dedicate a solid day's work to re-watch the vods and split the tournament sets. They then use this application to automatically split up videos and reduce the backlog of tournament sets that have been left collecting dust on some hard drive.

## Prerequisite to working with mp4 files in `vods-to-split`

Install Git Large File Storage:
`https://git-lfs.github.com/`

## Running

From project root:

1. Build virtual environment (only necessary first time you clone)
  ```
  virtualenv env
  ```

2. Activate source (`Scripts` is exclusive to windows virtual environment implementation)
  ```
  source env/Scripts/activate
  ```

3. Install the python libraries
  ```
  pip install -r requirements.txt
  ```

4. Install open cv (the library used to analyze video/images)
  ```
  pip install opencv_python-3.1.0-cp27-cp27m-win32.whl
  ```

5. Go to `/main` and run `main.py` 
  ```
  cd main
  python main.py
  ```
  
## Todo

make short 10 second video in dolphin/obs (character select screen to stage select)
capture two full frames from video and attempt to locate when they are in the parent video
capture partial image specific to a particular time (like something from the character select screen and something from the stage select) and locate their time in the clip

Capture sample video in mp4 format from dolphin that showcases 2 matches. Both matches go to character select screen > game! > back to character select screen.

###the ultimate test...###
7 hour vgbc vod
