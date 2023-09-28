# Applying commands to multiple files

Some people in class were wondering about how to execute the same command on multiple files. Here's how you do it!

## Quick answer

As an example, let's apply the negate filter to all videos in our current folder:

```
for f in *.mp4; do ffmpeg -i "$f" -vf "negate" "$f.new.mp4"; done
```

Just replace the ffmpeg command with the one above to try it out on your own files.

## Long answer

The above command relies on a few concepts we haven't talked about yet.

### Globs

The first is called the "glob pattern". In the command line, you can specify multiple files using a special wildcard syntax: the `*` character. These are called "globs".

For example, to list all files that end in "mp4":

```
ls *.mp4
```

This means, "give me all files in this folder that starts with *anything* and end in ".mp4".

Another example: list all files that that start with "video" and end in anything:

```
ls video*
```

### The shell

When you open up the terminal, you're actually running *two* programs. One, the terminal application itself which deals with things like showing you a window and scrolling, and another program known as the "shell" which is actually responsible for interpreting all the commands that you're typing in. On a mac, the shell program, by default is called `zsh`. On linux, it's typically `bash`. They are quite similar. The shell let's you execute commands, but it's also a programming environment, with variables, loops, and other normal programmy stuff.

### Variables

In bash/zsh you can store variables by writing

```
VARIABLE_NAME="some value"
```

To reference a variable, write its name, preceded by the `$` character. For example:

```
myfile="shoe.mp4"

ffmpeg -i $myfile output.mp4
```

Surround the variable name with quotes, to prevent weird stuff from happening if the content of our variable has spaces in it. We can also append stuff to the variable:

```
myfile="shoe.mp4"

ffmpeg -i "$myfile" "$myfile.mp3"
```

When bash/zsh sees the above ffmpeg command, it'll swap out "myfile" with the value that we set for it earlier, becoming:

```
ffmpeg -i "shoe.mp4" "shoe.mp4.mp3"
```

### Loops

A loop lets us run a command on multiple inputs, storing the value of each input in a temporary variable. The structure is:

```
for TEMPORARY_VARIABLE_NAME in FILES; do SOME_COMMAND; done
```

Let's look at the example again:

```
for f in *.mp4; do ffmpeg -i "$f" -vf "negate" "$f.new.mp4"; done
```

The above for loop says:

1. Grab every file in the folder that ends with ".mp4"
2. Store the name of those files, one by one, in a variable called "f"
3. Run the ffmpeg command, using "$f" as an input, and "$f.new.mp4" as an output, on each of the files
4. Save the output of the ffmpeg command as the name of the original file, plus the characters ".new.mp4"
