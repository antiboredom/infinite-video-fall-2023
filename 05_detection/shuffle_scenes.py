import sys
from moviepy.editor import VideoFileClip, concatenate_videoclips
from shots import get_shots
import random

VIDEO = sys.argv[1]

scenes = get_shots(VIDEO)

vidfile = VideoFileClip(VIDEO)

clips = []

for s in scenes:
    clip = vidfile.subclip(s["start"], s["end"])
    clips.append(clip)

random.shuffle(clips)

composition = concatenate_videoclips(clips)
composition.write_videofile("randomized.mp4")
