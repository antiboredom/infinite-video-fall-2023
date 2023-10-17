# Detecting cuts/scenes in video

There are a few ways to automatically find cuts in videos. FFmpeg actually comes with a scene detection filter, which you can run like so:

```bash
ffmpeg -i test.mp4 -filter_complex "scdet" -f null -
```

This will print out the timestamps whenever ffmpeg thinks a scene has changed. It works OK, but I've found that it isn't always the best solution. Instead I reccomend a program called [`PySceneDetect`](https://github.com/Breakthrough/PySceneDetect) which is both a command line tool, and module that you can import into python.

To install:

```bash
pip3 install "scenedetect[opencv]"
```

You can then run it with:

```bash
scenedetect -i video.mp4
```

If you want to automatically create individual clips for each scene:

```bash
scenedetect -i video.mp4 split-video
```

You can also use it within python using the `detect` method, which returns a list of scenes with start and end times.

```python
from scenedetect import ContentDetector, detect

video = "myvideo.mp4"
scene_list = detect(video, ContentDetector())

for shot in scene_list:
	start_time = shot[0].get_seconds()
	end_time = shot[1].get_seconds()
 	print("Start:", start_time)
 	print("End:", end_time)
```

I've included an example file called `shots.py` which will run the scene detection on a video (or videos) that you provide, and save the results as a `.json` file. 

To use `shots.py`:

```bash
python3 shots.py myvideo.mp4
```

I suggest using `shots.py` rather than running `scenedetect` because it will cache the shot start and  end times, rather than regenerate them each time your run the script. For example, here's how you would use shots.py to shuffle all the scenes in a video:

```python
from moviepy.editor import VideoFileClip, concatenate_videoclips
from shots import get_shots
import random

VIDEO = "myvideo.mp4"

# get the start and end times in a video
scenes = get_shots(VIDEO)

vidfile = VideoFileClip(VIDEO)

# create an empty list of clips
clips = []

# create a subclip for each scene and add to the clips list
for s in scenes:
    clip = vidfile.subclip(s["start"], s["end"])
    clips.append(clip)

# randomize the order of the clips
random.shuffle(clips)

# save a video
composition = concatenate_videoclips(clips)
composition.write_videofile("randomized.mp4")
```

