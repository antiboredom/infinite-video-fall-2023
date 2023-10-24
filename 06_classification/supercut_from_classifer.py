import sys
from custom_classifier_video import label_scenes
from shots import get_shots
from moviepy.editor import VideoFileClip, concatenate_videoclips

LABEL = "soda"
CONF = 0.7

clips = []

for f in sys.argv[1:]:
  scenes = get_shots(f)
  labels = label_scenes(f, scenes)

  vid = VideoFileClip(f)

  for l in labels:
    if l["labels"][0]["label"] == LABEL and l["labels"][0]["score"] >= CONF:
      start = l["start"]
      end = l["end"]
      print(start, end)
      clip = vid.subclip(start, end)
      clips.append(clip)

comp = concatenate_videoclips(clips)
comp.write_videofile("testttt.mp4")