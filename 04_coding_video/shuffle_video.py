from moviepy.editor import VideoFileClip, concatenate_videoclips
import random

# This script will shuffle a video

# change this to change the length of each segment
clip_duration = 1

# the video to work with
video = VideoFileClip("bush.mp4")

total_duration = video.duration

start = 0
all_clips = []

while start < total_duration:
    end = start + clip_duration

    if end > total_duration:
        end = total_duration

    clip = video.subclip(start, end)
    
    start = start + clip_duration

    all_clips.append(clip)

random.shuffle(all_clips)

composition = concatenate_videoclips(all_clips)
composition.write_videofile("shuffled.mp4")
