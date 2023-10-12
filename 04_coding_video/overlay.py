from moviepy.editor import VideoFileClip, CompositeVideoClip

video = VideoFileClip("bush.mp4")

all_clips = []
start = 4
duration = 5
skip = 2
timeline_start = 0
clip_width = video.size[0]

for i in range(5):
    clip = video.subclip(start, start + duration)
    clip = clip.resize(width=clip_width)
    clip = clip.set_position("center")
    clip = clip.set_start(timeline_start)
    all_clips.append(clip)

    clip_width = clip_width * 0.8
    timeline_start = timeline_start + 1

composition = CompositeVideoClip(all_clips)
composition.write_videofile("overlayed.mp4")
