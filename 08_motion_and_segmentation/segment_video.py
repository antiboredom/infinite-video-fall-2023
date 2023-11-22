from moviepy.editor import VideoFileClip
from PIL import Image
from transformers import pipeline

pipe = pipeline("image-segmentation")

video = VideoFileClip("test.mov")

frame_number = 0
for f in video.iter_frames():
    frame_number += 1
    img = Image.fromarray(f)
    results = pipe(img)

    has_person = False
    for i, r in enumerate(results):
        if r["label"] == "person":
            has_person = True
            img.putalpha(r["mask"])

    img.save(f"frame_{str(frame_number).zfill(5)}.png")
