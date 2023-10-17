import json
import os

from moviepy.editor import VideoFileClip
from PIL import Image
from transformers import pipeline

from shots import get_shots

# change me to change the model
MODEL = "google/vit-base-patch16-224"

labeler = pipeline("image-classification", model=MODEL)


def label_scenes(videofile, scenes):
    # file name to save the labels to
    outname = videofile + ".labels.json"

    # if the file already exists, don't re-label, just load the file
    if os.path.exists(outname):
        with open(outname, "r") as infile:
            return json.load(infile)

    clip = VideoFileClip(videofile)

    out = []

    # go through every scene in the video
    for i, scene in enumerate(scenes):
        start_time = scene["start"]
        end_time = scene["end"]

        # extract a the first frame of the scene
        frame = clip.get_frame(start_time)

        # convert the frame into an image
        img = Image.fromarray(frame)

        # get a label from the image
        results = labeler(img)

        print("scene", i, start_time)
        for r in results:
            print(r["score"], r["label"])

        item = {
            "start": start_time,
            "end": end_time,
            "content": results[0]["label"],
            "labels": results,
        }

        out.append(item)

    # save all the labels
    with open(outname, "w") as outfile:
        json.dump(out, outfile, indent=2)

    # return the list of labeled scenes
    return out


if __name__ == "__main__":
    import sys

    for f in sys.argv[1:]:
        scenes = get_shots(f)
        label_scenes(f, scenes)
