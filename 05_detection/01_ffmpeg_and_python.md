# Running FFMpeg (or anything else) from Python

You can run any command line program from Python. To do so, you must first import the `subprocess` module. You can then call `subprocess.run` with the command you'd like to run, which takes a list of strings as an argument. For example to run this `say` command:

```bash
say "hello class"
```

You'd write:

```python
import subprocess

subprocess.run(["say", "hello class"])
```

To convert from command line command to running the same thing in Python, just imagine that you're splitting the command into little chunks, based on where the spaces are.

```
ffmpeg -i hello.mp4 -vf negate output.mp4
```

The parts of this command are "ffmpeg", "-i", "hello.mp4", "-vf", "negate", and "output.mp4". This translates to:


```python
import subprocess

subprocess.run(["ffmpeg", "-i", "hello.mp4", "-vf", "negate", "output.mp4"])
```

For longer commands, it's helpful to store the argument list in a variable. You can also replace individual elements of the list with variables:

```python
import subprocess

inputvideo = "hello.mp4"
output = "hello.gif"

args = ["ffmpeg", "-i", inputvideo, output]

subprocess.run(args)
```

## String Interpolation

To pass arguments to ffmpeg filters, you may find it helpful to use *string interpolation*. This lets you stick different strings together in a convenient way.

To make an interpolated string, your precede the `"` character with an `f`. You can then toss in other variables by surrounding them with `{}` characters.

For example:

```python

name = "Karl"
adjective = "cool"

sentence = f"I think {name} is very {adjective}."
# prints out "I think Karl is very cool.
```

To use this with the colorize filter, which takes arguments like `ffmpeg -i punch.mp4 -vf "colorize=hue=100:saturation=0.9" output.mp4` we could make a `hue_amount` variable and a saturation_amount variable:

```python

import subprocess

hue_amount = 100
saturation_amount = 0.9

args = [
	"ffmpeg",
	"-i",
	"punch.mp4",
	"-vf",
	f"colorize=hue={hue_amount}:saturation={saturation_amount}"
	"output.mp4"
]

subprocess.run(args)
```

Note that I'm also splitting the args list into multiple lines to make it easier to read.

This can be helpful when playing with randomness, or using loops to incrementally alter variable amounts.


## Globs in Python

In the command line you can list files using a wild card pattern known as a "glob". You can also do this in python to work with multiple files in a loop. Imagine we have a folder called `my_videos` filled with mp4s. Using `glob` we can create a list of all the mp4 files in that folder.

```python
import glob
import subprocess

# all_videos will become a list like ["one.mp4", "another.mp4", "punch.mp4"]
all_videos = glob.glob("my_videos/*.mp4")

# loop over all the videos, convert them to gifs, and use the negate filter on them
for video in all_videos:
	subprocess.run(["ffmpeg", "-i", video, "-vf", "negate", video + ".negated.gif"])
```