# The Command Line

The command line is a text-based interface for interacting with your computer. From the command line you can launch programs, view files, and manipulate your file system by making, moving, and copying files and directories. You can think of it as the Finder in Mac, without the graphic interface, but much more powerful.

## Setup


On a Mac you can access the command line by opening up the `Terminal` application, located in `/Applications/Utilities/Terminal`

To get started on Windows you will need to set up the Windows Subsystem for Linux, which allows you to run Ubuntu (a Linux distribution) from within your current Windows 10 installation.  [Follow this guide to do so](https://tutorials.ubuntu.com/tutorial/tutorial-ubuntu-on-windows). Alternatively, you can install [Git for Windows](https://gitforwindows.org/) which includes many of the commands I'll be covering below.


---


## The Prompt

When you open up your terminal application you'll see something like this:

```bash
sam@SamsComputer ~ % 
```

This is called the "prompt". By default (on a Mac) it shows your username, an `@` symbol, the name of your computer, the directory that you are currently in, and then a `%` sign.

The basic use of the command line is: 1) you type a command, 2) you hit return, and 3) some output of the command is printed to the screen.

Whatever you type will start appearing after the end of the prompt line.

---

## Basic Navigation & File Operations

*Please note I use the word "directory" and "folder" interchangeably.*

When you open a new terminal window, you are placed inside your home folder. On a Mac this is `/Users/myusername` and on Linux, `/home/myusername`.

To see the folder you are currently in, type: `pwd` and hit return. `pwd` stands for "print working directory", or in other words, "show me the directory I am currently working from".

### Getting around, making, deleting and copying files and folders.


**`pwd`** stands for "print working directory". It prints out where you are:

```bash
pwd
```

**`ls`** stands for "list". It lists the contents of current directory.

```bash
ls
```

**`cd`** stands for "change directory". Type `cd` and then the directory you want to go to. For example, change to the Desktop from your home folder:

```bash
cd Desktop
```

To go into the parent folder, up one level in the file structure, type `..` or `../` instead of a folder name, like so:

```bash
cd ..
```

If you type `cd` without a folder name after, it takes you back to your home folder.


**`mkdir`** stands for "make directory". Type `mkdir` and then a name to make a folder. For example, make a folder called "cool_project":

```bash
mkdir cool_project
```

**`mv`** stands for "move". It lets you move files and folders and also rename them. To rename a file:

```bash
mv oldname.txt newname.txt
```

**`cp`** stands for "copy". It lets you duplicate files:

```bash
cp draft.txt draft_copy.txt
```

**`rm`** stands for "remove". It lets you delete files:

```bash
rm bad_selfie.jpg
```

Please note, `rm` will **not** ask for confirmation, and it will not move files to the trash. It'll just delete them immediately, so be careful.


**`file`** provides basic info about a file:

```bash
file mysterfile.what
```

## The Structure of the Filesystem

Everything on your computer is either a file or a folder, and these files and folders are organized hierarchically, like a tree. At the very bottom of the tree is the "root folder", indicated by a single forward slash, like so `/`. Here's a basic example of directory structure:

```bash
/
	Users/
  		sam/
   			Desktop/
	  			trotsky.jpg
	  			the_man_without_qualities.txt
	 		Documents/
	 		Downloads/
		Guest/
	Applications/
	Volumes/
```

Each file and folder has a unique location on the filesystem. This location is called a "path". You can reference files and folders either by their **relative** path, or by their **absolute** or **full** path. In the previous examples I have been using the relative path - that is, I have been referencing files relative to where I currently am. **A path is absolute if it begins with a `/`**

For example the absolute path to `the_man_without_qualities.txt` in the above filesystem is `/Users/sam/Desktop/the_man_without_qualities.txt`. I can look inside the contents of this file, from any working directory, with this command:

```bash
more /Users/sam/Desktop/the_man_without_qualities.txt
```

There are a few shortcuts for dealing paths as well.

`.` (single dot) or `'./'` (single dot with slash) means the current folder that I am in.

`..` (two dots) or `../` (two dots with slash) means the parent folder. For example, if am in my Desktop folder and I want to list the contents of my Downloads folder I could type:

```bash
ls ../Downloads/
```

Finally, the `~` symbol refers to your home folder.

---

## Tips

It can take a while to get used to the command line, but there are a few tips and trick that make it much easier to use.

* Use the up and down arrows to view a history of the commands you have entered.
* Hit the tab key to autocomplete commands and file paths
* Type `open` and then a filename to open the file in its default program
* Type `open .` to open the current folder in the Finder
* Drag a folder or file onto the terminal to fill in its absolute path
* Type `ctrl-a` to move your cursor to the beginning of the line, and `ctrl-e` to the end

---

## Reading and manipulating text files (basics)

**`cat`** stands for "concatenate" and it shows you the contents of a file and also allows you to join two files together. For example, to print out the entirety of the Communist Manifesto:

```bash
cat manifesto.txt
```

**`more`** is like `cat` but will paginate the output if it is larger than the size of your terminal window:

```bash
more manifesto.txt
```
(now use the up and down arrows to go up or down by a line, the space to go down by a page and `q` to exit if needed)


**`sort`** sorts a file alphabetically by line and prints the output to the screen

```bash
sort names.txt
```

**`grep`** searches each line of a file for some input, and prints those lines to the screen. For example, the following searches for all lines in the Communist Manifesto containing the word "Communist".

```bash
grep Communist manifesto.txt
```
---


## Command Line Options and Getting Help

Most commands have extra options that you can input when you run the command.  They are usually preceded by either one or two dashes (`-` or `--`).

The structure of a typical command looks like this:

```bash
command_name [options] arguments
```

("arguments" refers to the file or files your are running the command with)

For example, the `sort` command outputs in ascending order by default, but you can have it use reverse order with the `-r` option, like so:

```bash
sort -r manifesto.txt
```

You can also tell `sort` to only output unique lines (ie, to remove any duplicate lines) with the `-u` option:

```bash
sort -u manifesto.txt
```

Finally you can combine options:

```bash
sort -u -r manifesto.txt
```

Another fun example is the `say` command, which outputs text as computer speech.

```bash
say "a specter is haunting this computer"
```

Sometimes options have parameters. For example, the `say` command allows you to change its voice with the `-v` option, followed by the name of a computer voice.


```bash
say -v Amelie "the specter of communism"
```

You can change the rate at which words are spoken using `-r NUM` where `NUM` is a number.


```bash
say -v Amelie "the specter of communism" -r 100
```

To see all the options and view a manual for any command, use the `man` tool (short for "manual")

```bash
man say
```

When viewing a manual page, use the arrow keys to navigate, and `q` to exit.

And of course, if you can't remember a command or option, just google it! Sometimes it's much easier than searching through the man pages...

---

## Piping and Directing Output

Most commands will produce output on the screen. However we can also automatically save that output to the file system using the `>` character followed by a filename.

Sort a file called "names.txt", and save the output to a new file called "sorted_names.txt":

```bash
sort names.txt > sorted_names.txt
```

`>` will create a file if it does not already exist, or overwrite one if it does. You can use `>>` instead to append to a file.

Unix also has a very powerful concept called "pipes" which allow us to chain commands together, effectively feeding the output of one command into the input of another. To do so, we use the `|` symbol.

Extract all lines of the Communist Manifesto containing "Communist", then sort them.

```bash
grep Communist manifesto.txt | sort -u
```

The `|` here means "take the output of the grep command and send it to sort -u". You can use as many pipes as you desire, and combine this technique with the output redirection.

Extract all lines of the Communist Manifesto containing "Communist", then sort them, then save to a new file called "sorted_communists.txt"

```bash
grep Communist manifesto.txt | sort -u > sorted_communists.txt
```

---

## Intermediate text manipulation

Here are a few slightly more advanced techniques for manipulating text on the command line.

### Breaking lines into words or other segments

**`cut`** cuts out a portion of each line and splits it out according to a delimiter. If you use a space `" "` as a delimiter, it breaks a line up into words:

```bash
cut -d " " manifesto.txt
```

The `-f` option allows you to specify a particular item to grab. `-f 1` grabs just the first word.

```bash
cut -d " " -f 1 manifesto.txt
```

Try combining this with other commands, like `sort` or `grep`.

```bash
cut -d " " -f 2 manifesto.txt | sort -u -R
```

### Finding and replacing

**`sed`** is a somewhat complex tool that allows you to find and replace things in text files. It takes an argument with a command using it's own special syntax, like so `s/FIND/REPLACE/g`.

For example, replace all instances of "you" with "me":

```bash
sed 's/you/me/g' sometext.txt
```

By default, `sed` is case sensitive. To make it case insensitive, add an `i` at the end:

```bash
sed 's/you/me/gi' sometext.txt
```

Sometimes, I'll just find something online that seems useful without really understanding how it works. You should definitely give this a shot. For example, here's how you use `sed` to split a text into sentences: 

```bash
sed 's/[.!?]  */&\n/g' manifesto.txt
```

You can do a ton of other stuff with `sed`. If you want to learn more, take a look at this [tutorial](https://www.digitalocean.com/community/tutorials/the-basics-of-using-the-sed-stream-editor-to-manipulate-text-in-linux)


---

## Downloading stuff

There are two very useful commands for downloading stuff from the internet.


### cURL

**`curl`** makes a http request, and prints the output to the terminal. For example, this grabs the html source of NPR's text only news page:

```bash
curl https://text.npr.org
```

This is a bit hard to read because it's full of html. But there are a bunch of little websites that are specifically designed to be "curled".

To get the weather:

```bash
curl wttr.in
```

Stats about covid:

```bash
curl https://corona-stats.online
```

Generate QR codes:

```bash
curl "qrenco.de/but why"
```

Many more [here](https://github.com/chubin/awesome-console-services)!

### wget

**`wget`** allows you to easily download files:

```bash
wget "https://www.gutenberg.org/cache/epub/61/pg61.txt"
```

You can also specify a name to save the file as with the `-O` option.

```bash
wget "https://www.gutenberg.org/cache/epub/61/pg61.txt" -O manifesto.txt
```

---


## Wildcards

It's possible to reference multiple files using the `*` character in combination with other characters. This can be really useful in a lot of situations.

For example, can list all files that begin with the word "the" like so:

```bash
ls the*
```

List all jpg images:

```bash
ls *.jpg
```

Make a folder called `images` and move all jpeg images into it:

```bash
mkdir images
mv *.jpg images/
```

Combine all text files in a folder:

```
cat *.txt > everything.txt
```
