import face_recognition
import cv2
import json
from moviepy.editor import VideoFileClip, concatenate_videoclips
import argparse


def f_to_s(f, fps):
    return f / fps


def find_face(face_encodings, known_face_encodings):
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        if True in matches:
            return True

    return False


def face_on(videofile, face_image_paths, resize=1.0, skip=1):
    known_face_encodings = []

    for p in face_image_paths:
        image = face_recognition.load_image_file(p)
        encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(encoding)

    video = VideoFileClip(videofile)
    fps = video.fps

    times = []
    start = None

    frame_num = 0
    for f in video.iter_frames():
        frame_num += 1
        if frame_num % skip != 0:
            continue

        seconds = f_to_s(frame_num, fps)

        if resize != 1.0:
            f = cv2.resize(f, (0, 0), fx=resize, fy=resize)

        face_locations = face_recognition.face_locations(f)
        face_encodings = face_recognition.face_encodings(f, face_locations)

        has_face = find_face(face_encodings, known_face_encodings)

        if has_face:
            if start is None:
                start = seconds
                times.append({"start": start, "end": video.duration})
        else:
            if start is not None:
                times[-1]["end"] = seconds
                start = None

    return times


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create a supercut based on looking for a particular face in a collection of video"
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
        "--faces",
        "-f",
        dest="faces",
        nargs="*",
        required=True,
        help="Path(s) to images of faces to find",
    )
    parser.add_argument(
        "--skip",
        "-s",
        dest="skip",
        default=2,
        type=int,
        help="Number of frames to skip",
    )
    parser.add_argument(
        "--resize",
        "-r",
        dest="resize",
        default=1.0,
        type=float,
        help="Resize frame factor (between 0.1 and 1.0)",
    )

    args = parser.parse_args()

    for f in args.input:
        times = face_on(f, args.faces, resize=args.resize, skip=args.skip)
        with open(f + ".found_faces.json", "w") as outfile:
            json.dump(times, outfile)
        video = VideoFileClip(f)
        clips = [video.subclip(t["start"], t["end"]) for t in times]
        comp = concatenate_videoclips(clips)
        comp.write_videofile(f + ".face.mp4")
