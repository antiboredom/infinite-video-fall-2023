import json
import os

from moviepy.editor import VideoFileClip
from PIL import Image
from transformers import pipeline

from shots import get_shots

# change me to change the model
MODEL = "nlpconnect/vit-gpt2-image-captioning"

captioner = pipeline("image-to-text", model=MODEL)


def caption_scenes(videofile, scenes):
    # file name to save the captions to
    outname = videofile + ".captions.json"

    # if the file already exists, don't re-caption, just load the file
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

        # get a caption from the image
        results = captioner(img)
        caption = results[0]["generated_text"]

        print(i, start_time, caption)

        # add the caption, start time and end time to our output list
        item = {"content": caption, "start": start_time, "end": end_time}
        out.append(item)

    # save all the captions
    with open(outname, "w") as outfile:
        json.dump(out, outfile, indent=2)

    # return the list of captioned scenes
    return out


if __name__ == "__main__":
    import sys

    for f in sys.argv[1:]:
        scenes = get_shots(f)
        caption_scenes(f, scenes)
