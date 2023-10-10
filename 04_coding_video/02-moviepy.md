# Moviepy

Moviepy is a Python library that let's you edit video. 

To install it:

```bash
pip3 install moviepy
```

## Basic Editing

### Importing the library

To start, you first need to import moviepy.

```python
import moviepy.editor as mp
```

This imports moviepy with the name `mp`.

### VideoFileClip

A `VideoFileClip` is a container for video files. 

```python
video = mp.VideoFileClip("bush.mp4")
```

This stores a reference to the video "bush.mp4" as a python variable called `video`.

You can trim a clip using the `subclip` method, which takes two arguments, a start time and an end time.

```python
# trim our video, from 10 seconds to 15 seconds
clip = video.subclip(10, 15)
```

You can also run a limited number of effects on clips. For example, `resize` and `fade_in`:

```python
# resize the clip so that it's width is 100, and height is automatically calculated
clip = clip.resize(width=100)

# fade the clip in over 0.5 seconds:
clip = clip.fade_in(0.5)
```

To save an output, call `write_videofile` on a clip:

```python
clip.write_videofile("myclip.mp4")
```

All together:

```python
import moviepy.editor as mp
video = mp.VideoFileClip("bush.mp4")
clip = video.subclip(10, 15)
clip = clip.resize(width=100)
clip = clip.fade_in(0.5)
clip.write_videofile("myclip.mp4")
```


### Basic timeline

To make a basic timeline where one video clip follows another, use the `concatenate_videoclips` method, which takes a list of clips as an argument.

```python
import moviepy.editor as mp

# create variable called "video1" that refers to the video file "punch.mp4"
video1 = mp.VideoFileClip("punch.mp4")

# create variable called "video2" that refers to the video file "shoe.mp4"
video2 = mp.VideoFileClip("shoe.mp4")

# make a list called "clips" that contains our video variables
clips = [video1, video2]

# concatenate_videoclips stiches videos together
# it takes a list of clips as its argument
composition = mp.concatenate_videoclips(clips)

# save the new video 
composition.write_videofile("punch_and_shoe.mp4")
```

Note that `concatenate_videoclips` works with a list of VideoFileClips, or subclips.

### Overlaying and more complex compositions.

To make more complex compositions use `CompositeVideoClip`. `CompositeVideoClip` also takes a list of clips as an input. However, it will overlay the videos rather than play them one after another.

```python
import moviepy.editor as mp

video = mp.VideoFileClip("bush.mp4")

clip1 = video.subclip(0, 5)
clip2 = video.subclip(5, 10)
clip2 = clip2.resize(width=200).set_position("center").set_start(2)

clips = [clip1, clip2]

composition = CompositeVideoClip(clips)
composition.write_videofile("overlayed.mp4")
```

If you are using `CompositeVideoClip` you may need to modify a few other properties of your video clips. In the above example, I'm using [`set_position`](https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html#moviepy.video.VideoClip.VideoClip.set_position) to change the position of the second clip, and `set_start` to tell the moviepy to only start playing the clip after two seconds in the full timeline.

### Other types of clips

In addition to videoclips, moviepy supports text, solid colors, images, and audio. Once created you can use these clips just like `VideoFileClip`.

#### ColorClip

A color clip is a solid color. To use it, you must specify a size, and color. You also have to tell moviepy how long to play the clip with the `set_duration` method. To specify a color, provide three values, a red, green and blue amount, each between 0 and 255.

```python
import moviepy.editor as mp

# make a red color clip that's 1280x720 large, and plays for 10 seconds
redclip = mp.ColorClip(size=(1280, 720), color=(255, 0, 0))
redclip = redclip.set_duration(10)
redclip.fps = 24 # note: you must specifiy frames per second if you aren't including this clip in composition with video
redclip.write_videofile("red.mp4")
```

### ImageClip

`ImageClip` let's you use images:

```python
import moviepy.editor as mp

img = mp.ImageClip("some_image.jpg")
img = img.set_duration(10)
img.fps = 24 # note: you must specifiy frames per second if you aren't including this clip in composition with video
img.write_videofile("my_image.mp4")
```

### TextClip

[`TextClip`](https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html#textclip) let's you draw text, and has many options for specifying fonts, text color, size and position:

```python
import moviepy.editor as mp
txt_clip = mp.TextClip("A Spectre is Haunting this Video File", font="Times-BoldItalic", fontsize=70, color="white")
txt_clip = txt_clip.set_pos('center').set_duration(10)
txt_clip.fps = 24
txt_clip.write_videofile("sometext.mp4")
```

### AudioFileClip

You can also mix in audio with `AudioFileClip`.

```python
import moviepy.editor as mp

audio = mp.AudioFileClip("song.mp3")
```

### Combining Different Types of Clips

You can mix and match different clip types in your compositions.

```
import moviepy.editor as mp

video = mp.VideoFileClip("bush.mp4").subclip(3, 8)

txtclip = mp.TextClip("A Spectre is Haunting this Video File", font="Times-BoldItalic", fontsize=20, color="white")
txtclip = txtclip.set_position('center').set_duration(5)

redclip = mp.ColorClip(size=(100, 100), color=(255, 0, 0))
redclip = redclip.set_duration(3)

imgclip = mp.ImageClip("shoe.jpg")
imgclip = imgclip.set_position(("center", "bottom"))
imgclip = imgclip.resize(width=200)
imgclip = imgclip.set_duration(1)
imgclip = imgclip.set_start(2)

composition = mp.CompositeVideoClip([video, redclip, imgclip, txtclip])
composition.write_videofile("composition.mp4")
```