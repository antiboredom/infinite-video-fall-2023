# Creating your own command line applications

We've been using a lot of command line applications throughout this course. Every python script is already in a sense a command line program. However, most of the time you make a program you'll want to allow the user to enter in arguments and options.

## Accessing command line arguments

### Using sys.argv

The `sys` module in Python is the simplest way to access to command line arguments. It comes with a variable called `argv` that will become a list of arguments passed to your script.

```python
# args1.py

import sys

print(sys.argv)

```

If we run this program with `python args1.py` the output will be: `['args1.py']`. The first element of the list is always the name of the file.

The command `python args1.py myfile.mp4` will yield: `['args1.py', 'myfile.mp4']`.

And `python args1.py --input myfile.mp4 --search person` will yield: `['args1.py', '--input', 'myfile.mp4', '--search', 'person']`.

If you have a very simple script that only takes one or two arguments you can use `sys.argv` to pass those to your python file.

```
import sys
import moviepy.editor as mp

# grab the 2nd element of the argv list
filename = sys.argv[1]

clip = mp.VideoFileClip(filename)

# ... do more stuff to your file here
```

### Argparse

This gets difficult to manage when you start passing in a bunch of arguments since you have to write code to do all the parsing. It's usually better in these cases to use a library that parses the arguments for you. There are a number of these, including [docopt](https://github.com/docopt/docopt) and [click](https://click.palletsprojects.com/en/8.1.x/).

Python also has a built in library called [argparse](https://docs.python.org/3/library/argparse.html). Let's use that one since you won't need to install anything. 

To use argparse, create a parser object and pass in the name of your program and a short description of what it does. Then use `add_argument` to tell the parser to watch for different arguments that user will provide.

```python
# args2.py

import argparse

# create a parser object 
parser = argparse.ArgumentParser(prog="CutClip", description="Cuts out a clip from a video.")

# add an argument
parser.add_argument("-i", "--input", help="Input file")

# actually parse the input
args = parser.parse_args()

# the --input argument argument will be stored as args.input
print(args.input)
```

`parser.add_argument` can take a bunch of options. First we provide a shorthand of the argument, like `-i`, then a longer version `--input`, then a help message to tell the user what this argument is supposed to do. You can also add default values, set the type of variable that's expected, and make arguments required or optional.

To run the program above, we'd call `python args2.py --input somefile.mp4`. The value `somefile.mp4` will be stored in `args.input`.

Here's a more complex example. We'll make a simple command line program that takes an input video, a start time, an end time, and an output file. The program will cut the video to the start and end times that we specify.


```
# cutclip.py

import argparse
import moviepy.editor as mp

parser = argparse.ArgumentParser(
    prog="CutClip", description="Cuts out a clip from a video."
)

# create an input argument
parser.add_argument("-i", "--input", required=True, help="Input file")

# start time argument
parser.add_argument("-s", "--start", default=0.0, type=float, help="Start time")

# end time argument
parser.add_argument("-e", "--end", required=True, type=float, help="End time")

# output file to save to
parser.add_argument("-o", "--output", required=False, default="output.mp4", help="Output file")

args = parser.parse_args()

video = mp.VideoFileClip(args.input)
clip = video.subclip(args.start, args.end)
clip.write_videofile(args.output)

```

A user can run this program with:

```
python cutclip.py --input myvideo.mp4 --start 1.0 --end 3.0 --output clip.mp4
```

Another nice thing about using argparse is that it will automatically create a little help screen that the user can access with `python cutclip.py --help`. This would output:

```
usage: CutClip [-h] -i INPUT [-s START] -e END [-o OUTPUT]

Cuts out a clip from a video.

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file
  -s START, --start START
                        Start time
  -e END, --end END     End time
  -o OUTPUT, --output OUTPUT
                        Output file
```


## Determining how your python file is being run

There are two ways of executing code in a python file. You can either run the file with `python whatever.py`, or you can `import` your file into other code. Python provides a useful way of figuring out which of these is happening, by automatically populating a variable called `__name__`. If `__name__` is set to `"__main__"` it means the file is being run directly, and not being imported. You can add an `if` statement at the bottom of a file to do different things depending on the value of this variable.

In the following code, we define a function called `hello`, but we only call the function if the file is run with `python greetings.py`.

```python
# greetings.py

def hello():
    print("Hello comrades!")


if __name__ == "__main__":
    hello()

```

This is useful way to have your python code act properly both as importable modules and as command line programs.


## Poetry

Publishing your python code so that others can install it with `pip` can feel a bit intimidating and confusing. I suggest a tool called [poetry](https://python-poetry.org/) to help out. In addition to providing a convenient way to publish packages, Poetry also helps you deal with python dependencies.

To install poetry, run:

```
curl -sSL https://install.python-poetry.org | python3 -
```

You can then use poetry to create a new project or set up an existing project. To create a new project:

```
poetry new mycoolproject
```

This will create a new folder called `mycoolproject` and give you a basic template to work with.

To add poetry to an existing project, cd into your project folder and run

```
poetry init
```

In both cases poetry will create a file called `pyproject.toml`. This file contains info about your project as well as a list of python dependencies, like `moviepy`.

The main difference between a regular python project and a poetry project is managing dependencies and running your code. 

To run code, you'll now need to precede your command with `poetry run`. For example, `python mycode.py` becomes `poetry run python mycode.py`.

To add dependencies, you'll use `poetry add` rather than `pip install`. For example `poetry add moviepy`. You'll notice that when you do this, the `dependencies` section of `pyproject.toml` will change to include your new dependency.

### Creating an installable program

If you'd like users to be able run a program without typing `python` before it (like `videogrep`), you need to make a few changes to your code.

First of all, poetry requires you to put the executable code inside a function. Let's wrap our clip-cutting code into a function called `main`:

```python
import argparse
import moviepy.editor as mp


def main():
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
```


Then you need to add a `scripts` section to your `pyproject.toml` file, that tells poetry what the name of your program is, and what function to execute when the user runs your program.

```toml
[tool.poetry.scripts]
cutclip = 'cutclip:main'
```

`cutclip` will be the name of your program and `cutclip:main` is the function to run.

### Publishing

To publish your code to [pypi](https://pypi.org/) and allow other users to install it, first create an account on pypi. Then go to your account settings, hit add token, copy that token and then pass it to poetry with:

```
poetry config pypi-token.pypi your-api-token
```

Then run:
```
poetry build
poetry publish
```

Now anyone will be able to `pip install cutclip`!

