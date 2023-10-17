import sys
from moviepy.editor import VideoFileClip, concatenate_videoclips
from shots import get_shots
from label_shots import label_scenes
import random

VIDEO = sys.argv[1]
SEARCH = sys.argv[2]

scenes = get_shots(VIDEO)
labels = label_scenes(VIDEO, scenes)

vidfile = VideoFileClip(VIDEO)

clips = []

for scene in labels:
    found = False

    # for label in scene["labels"]:
    #     if SEARCH in label["label"]:
    #         found = True

    if SEARCH in scene["content"]:
        found = True

    if found:
        clip = vidfile.subclip(scene["start"], scene["end"])
        clips.append(clip)

composition = concatenate_videoclips(clips)
composition.write_videofile("search.mp4")
