import json
import os

from scenedetect import ContentDetector, detect


def get_shots(video):
    """returns a shot list and saves the list as a file"""

    print("Finding shots in", video) 

    outname = video + ".shots.json"

    if os.path.exists(outname):
        with open(outname, "r") as infile:
            return json.load(infile)

    shots = []

    scene_list = detect(video, ContentDetector())

    for shot in scene_list:
        item = {
            "start": shot[0].get_seconds(),
            "end": shot[1].get_seconds(),
        }
        shots.append(item)

    with open(outname, "w") as outfile:
        json.dump(shots, outfile, indent=2)

    return shots


if __name__ == "__main__":
    import sys

    for f in sys.argv[1:]:
        shots = get_shots(f)
        for s in shots:
            print(f"{s['start']} -> {s['end']}")
