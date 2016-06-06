[![](https://img.shields.io/badge/python-2.7-yellow.png "Python versions supported")](https://github.com/cztomczak/cefpython#cef-python)

# Super Smash Brothers Automatic Vod Splitter

This project aims to automate the splitting of long tournament captures (8+ hours) of games in the Super Smash Brothers series. The end goal is to provide as much automation and naming assistance in the creation of these smaller sets as possible and to eventually upload them to YouTube

## Getting Started

### Project Dependencies

**Windows** (unsure of how generalized this project can be to other platforms)

**Python Virtual Environment**

**Git Large File Storage**: https://git-lfs.github.com/ 
* Run: `git lfs pull` to get the video and image assets

### Installation/running

Clone the repo. Then from project root:

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

## Misc

#### Usecase 1:

After a long 8 hour day of streaming a local weekly, the streamer can input their saved vod into this application and not have to spend several more hours just to separate out the videos they were just watching/streaming all day.

#### Usecase 2:

A local streamer has been streaming quite a few tournaments and has several saved vods but the matches for those tournaments have not been uploaded to youtube for one reason or another. After quite a few tournaments, the work has piled up and no one wants to dedicate a solid day's work to re-watch the vods and split the tournament sets. They then use this application to automatically split up videos and reduce the backlog of tournament sets that have been left collecting dust on some hard drive.

### Todo

* Re-record video and image go/game assets in 1080p quality and size
* Locate start/stop times of a single small video
* Add an "approach" section to readme to brief others who want to help out how this project aims to find begining and end of matches
* Save text file of game start/stop times to text file of the same name as the video being analyzed
* Using the saved timestamps, split the video into separate files
* Incoperate GUI with 3 core buttons:
  * **Process VOD** (choose vod, spit out file with timestamps)
  * **Split VOD** (spits out videos split according to the timestamps file)
  * **Upload matches to YouTube**
    * (needed? or no? worth the time/effort of authenticating?)
* **Future**: Incorperate proof of concept by splitting an 8 hour Xanadu VOD from YouTube


