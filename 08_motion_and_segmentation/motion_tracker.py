import cv2
import argparse
import json
from moviepy.editor import VideoFileClip


def f_to_s(f, fps):
    return f / fps


def detect(inp, preview=False):
    outname = inp + ".motion.json"
    times = []
    has_motion = False
    prev_had_motion = None

    mog = cv2.createBackgroundSubtractorMOG2()

    clip = VideoFileClip(inp)
    fps = clip.fps

    frames = clip.iter_frames()

    frame_num = 1

    for frame in frames:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        fgmask = mog.apply(gray)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        fgmask = cv2.erode(fgmask, kernel, iterations=1)
        fgmask = cv2.dilate(fgmask, kernel, iterations=1)

        contours, hierarchy = cv2.findContours(
            fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        # Ignore small contours
        contours = [c for c in contours if cv2.contourArea(c) > 1000]

        # If there are any contours, there is motion
        has_motion = len(contours) > 0

        if frame_num == 1:
            times.append({"start": 0, "has_motion": has_motion})
        else:
            # If the motion state has changed, record the time
            if has_motion != prev_had_motion:
                times[-1]["end"] = f_to_s(frame_num - 1, fps)
                times.append(
                    {"start": f_to_s(frame_num, fps), "has_motion": has_motion}
                )

        if preview:
            for contour in contours:
                # Draw bounding box around contour
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imshow("Motion Detection", frame)
            if cv2.waitKey(1) == ord("q"):
                break

        frame_num += 1
        prev_had_motion = has_motion

    times[-1]["end"] = clip.duration

    with open(outname, "w") as f:
        json.dump(times, f, indent=2)

    if preview:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detect camera motion in videos.")
    parser.add_argument(
        "--preview",
        "-p",
        dest="preview",
        action="store_true",
        help="Show preview window.",
    )

    parser.add_argument("input", nargs="+", help="Path of a video or videos.")

    args = parser.parse_args()

    files = args.input

    for f in files:
        print("Processing", f)
        detect(f, preview=args.preview)
