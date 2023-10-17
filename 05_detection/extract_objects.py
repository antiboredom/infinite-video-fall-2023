from moviepy.editor import VideoFileClip
from PIL import Image
from transformers import pipeline

# searches through a video and extracts images of particular objects

# the label we are looking for
LABEL = "person"

# run the code only ever X frames (5 by default)
SKIP = 5

pipe = pipeline("object-detection", model="hustvl/yolos-tiny")


def save_images(videofile, search=LABEL):
    clip = VideoFileClip(videofile)
    index = 0
    frame_no = 0

    for frame in clip.iter_frames():
        frame_no += 1
        if frame_no % SKIP != 0:
            continue

        print("Detecting objects in frame", frame_no)

        image = Image.fromarray(frame)

        results = pipe(image)

        for r in results:
            print(r)
            if r["label"] == search:
                box = r["box"]
                clipped = image.crop((box["xmin"], box["ymin"], box["xmax"], box["ymax"]))
                clipped.save(f"{videofile}_{search}_{str(index).zfill(4)}.jpg")
                index += 1


if __name__ == "__main__":
    import sys

    for f in sys.argv[1:]:
        save_images(f, LABEL)
