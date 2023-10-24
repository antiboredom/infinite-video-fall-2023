from scenedetect import ContentDetector, detect
from moviepy.editor import VideoFileClip, concatenate_videoclips
from PIL import Image
from transformers import pipeline


# MODEL = "openai/clip-vit-large-patch14" # 1.7gb
MODEL = "openai/clip-vit-base-patch32"  # 600mb
labeler = pipeline(model=MODEL, task="zero-shot-image-classification")


def get_shots(video):
    """returns a shot list and saves the list as a file"""
    shots = []
    scene_list = detect(video, ContentDetector())

    for shot in scene_list:
        item = {
            "start": shot[0].get_seconds(),
            "end": shot[1].get_seconds(),
        }
        shots.append(item)
    return shots


def label_scenes(videofile, scenes, labels):
    out = []
    video = VideoFileClip(videofile)
    for scene in scenes:
        start_time = scene["start"]
        end_time = scene["end"]

        # extract a the first frame of the scene
        frame = video.get_frame(start_time)

        # convert the frame into an image
        img = Image.fromarray(frame)

        # get a label from the image
        results = labeler(img, candidate_labels=labels)

        item = {
            "start": start_time,
            "end": end_time,
            "label": results[0]["label"],
            "score": results[0]["score"],
        }
        out.append(item)
    return out


def make_supercut(videos, labels, search, thresh=0.7, output="supercut.mp4"):
    clips = []
    for v in videos:
        scenes = get_shots(v)
        scenes = label_scenes(v, scenes, labels)
        video = VideoFileClip(v)
        for s in scenes:
            if s["label"] == search and s["score"] >= thresh:
                clips.append(video.subclip(s["start"], s["end"]))
    composition = concatenate_videoclips(clips)
    composition.write_videofile(output)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Create a supercut based on image classification"
    )
    parser.add_argument(
        "--input",
        "-i",
        dest="input",
        nargs="*",
        required=True,
        help="video file or files",
    )
    parser.add_argument(
        "-l", "--labels", nargs="+", help="labels to use", required=True
    )
    parser.add_argument("-s", "--search", help="label to search for", required=False)
    parser.add_argument(
        "-o",
        "--output",
        default="supercut.mp4",
        help="output video file name",
        required=False,
    )
    parser.add_argument(
        "--threshold",
        "-t",
        dest="thresh",
        default=0.7,
        type=float,
        help="threshold for selecting label for supercut, between 0 and 1",
    )
    args = parser.parse_args()

    search = args.search
    if not search:
        search = args.labels[0]

    make_supercut(
        videos=args.input,
        labels=args.labels,
        thresh=args.thresh,
        search=search,
        output=args.output,
    )
