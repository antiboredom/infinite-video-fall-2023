import argparse
import moviepy.editor as mp

parser = argparse.ArgumentParser(
    prog="CutClip", description="Cuts out a clip from a video."
)

parser.add_argument("-i", "--input", required=True, help="Input file")
parser.add_argument("-s", "--start", default=0.0, type=float, help="Start time")
parser.add_argument("-e", "--end", required=True, type=float, help="End time")
parser.add_argument(
    "-o", "--output", required=False, default="output.mp4", help="Output file"
)

args = parser.parse_args()

video = mp.VideoFileClip(args.input)
clip = video.subclip(args.start, args.end)
clip.write_videofile(args.output)
