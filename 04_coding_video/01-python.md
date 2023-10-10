# Intro to Python

## Prerequisites

**NOTE: You should already have python installed if you've been following along in class**

There are two versions of Python, Python 2 and Python 3. For this guide we will be using Python 3, which you will need to install on your computer. The easiest way to do this, on a Mac, is with Homebrew, a tool that allows you to install and manage command line programs.

### Mac

#### Install Homebrew

Visit [Homebrew's website](https://brew.sh/) and follow the instructions there, or just copy and paste the following into your terminal:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

#### Install Python 3

Once Homebrew is done, you can use it to install Python and a number of other extremely useful command line tools.

```bash
brew install python3
```

### Windows

Download and install Python here: https://www.python.org/downloads/

---

### Install a Text Editor

To create and edit Python files you'll need a good text editor, specifically designed to edit code. Here are a few options (there are many more!):

* [Visual Studio Code](https://code.visualstudio.com/)
* [Atom](https://atom.io/)
* [Sublime](https://www.sublimetext.cm/) (not free)


---

## Python Basics

Python is a command line application, just like `cat`, `grep` and `sort`.

To execute Python code you run the `python` command with a text file as an argument. The `python` command reads the contents of your file, and executes the instructions that you put into it.

If you don't put a file as an argument, and just type `python` you will enter an interactive interpreter, where you can type python code line by line. This can be handy for quickly testing things out.

To exit the interpreter, just type `CTRL-D` or `exit()`.

To start, let's make a simple program that prints a message on the terminal. To do this we will use the `print` command.

Create a new file called `hello.py` and put this in it:

```python
print("Hello comrade")
```

**Tip**

You can create a new file with the `touch` command: `touch hello.py` 

And then open that file in your text editor with the `open` command: `open hello.py`


Open your terminal and navigate to the directory where the file is saved, and then type:

```python
python hello.py
```

You should see "Hello comrade" printed on the screen.


### Expressions

An "expression" is a set of instructions for the computer to execute. Python will read or evaluate your expressions and return a result. For example you can do some basic arithmetic:

```python
print(1+1)
print(10/2)
print(100 * 6.2 - 70/3.5)
```

---

### Comments

Any line that starts with the `#` character is a "comment", and will not be evaluated by Python when you run your program. You can use comments to write notes in your code, or simply to disable a line of code that you don't want to run.

```python

# this is a comment!
# python will ignore me!
```


### Variables

You can store the value of expressions inside named variables using the `=` symbol.

```python
x = 2
y = 5
z = x + y
print(x * 100)
print(z)
```

#### Types

Values have different "types" or categories. For example, 1 is an integer, 1.5 is a float.

You can see what type a value is is by using the `type` function:

```python
print(type(1))
```

Some important types are:

```python
a_number = 1 				# an integer
another_number = 5.1 		# a float
some_string = "Hello!" 		# a string
some_boolean = True 		# a boolean (notice the capitalization)
a_list = ["a bunch", "of", "stuff", a_number, some_string]
a_dictionary = {"key1": 10, "key2": "a string"} # a dictionary (key/value pairs)
```

In Python you do not need to declare variable types, or even that you are declaring a variable, you simply type a name, the equals sign, and then a value or expression.

---


### Strings

Strings are a variable type that stores text. To create a string, surround some text within quotation marks. It doesn't matter if you use single or double quotes as long as you are consistent.

```python
first_name = "Karl"
last_name = 'Marx'

print(first_name)
print(last_name)
```

If you add two or more strings together with the `+` sign, Python will create a new string for you, combining the two.

```python
first_name = "Karl"
second_name = "Marx"

# You can join strings together
full_name = first_name + last_name
# results in "KarlMarx"

# We'll add a space in between
full_name = first_name + " " + last_name
# results in "Karl Marx"
```

You can repeat a string with the multiplication symbol `*`:

```python
word = "revolution "
chant = word * 1000
print(chant)
```

Each character in a string is indexed numerically, and can access individual characters using `[]` square brackets. 

```python
name = "Karl Marx"
first_letter = name[0]
print(first_letter)

second_letter = name[1]
print(second_letter)
```

The character index begins with the number 0. If you wish to access the last character, you use `-1`. The second to last, `-2` and so on.

```python
name = "Karl Marx"
last_letter = name[-1]
print(last_letter)
```

You can also get a range of characters in a string by entering a starting and ending index in your square brackets:


```python
name = "Karl Marx"
first_three_letters = name[0:3]
print(first_three_letters)
```

To get the total length of a string, use the `len()` function.

```python
print(len("hello!"))
```

You can also determine if a string exists within another string with the `in` keyword.

```python
sentence = "A spectre is haunting Europe"
print("spectre" in sentence)
```


#### String methods

Python's string implementation comes with many useful methods that allow you to transform and get information about strings.

For example, to make a string uppercase:

```python
sentence = "hello there!"
uppercase = sentence.upper()
print(uppercase)
```

Here are a few more examples of things that you can do

```python
sentence = " A spectre is haunting Europe."

# make it uppercase
lowercase_sentence = sentence.lower()

# make it title case
titlecase_sentence = sentence.title()

# swap the case
titlecase_sentence = sentence.swapcase()

# remove empty white space at the start and end
stripped = sentence.strip()

# add 10 whitespace padding to both sides
centered = sentence.center(10, " ")

# replace one set of characters with another
replaced_sentence = sentence.replace("Europe", "Computation")

# replace spaces (you don't have to use english)
replaced_sentence2 = sentence.replace(" ", "👏")
```

Please note that these string methods do not alter your original string, they return a *new* string.

Here's a full list: [https://docs.python.org/3.7/library/stdtypes.html#string-methods](https://docs.python.org/3.7/library/stdtypes.html#string-methods)

---

### If/Else

Two equal signs together `==` allow us to test for equality, or to see if two expressions have the same value.

```python
print(1==1) # this will print True
print(1==5) # this will print False
```

Sometimes you only want code to run if certain conditions are true. To do this, use the `if` keyword, followed by an expression that evaluates to True or False, followed by an indented block of code.

```python
year = 1848

if year == 1848:
  print("Time for revolution")
```

You can use an `else` statement to do something if the condition is not met:

```python
year = 1847

if year==1848:
  print("Time for revolution")
else:
  print("Not time for revolution")
```

---

### Lists

A list is a numerically ordered collection of values, also known as an array.

```python
# make an empty list
my_list = []

# add something to our list with the "append" method
my_list.append("hi") # the list will now look like this: ["hi"]

# add some more stuff
my_list.append(45)
my_list.append(100.2)
my_list.append("whatever")

# now our list will look like this:
# ["hi", 45, 100.2, "whatever"]

# get the length of a list
len(my_list)

# you can access individual items in the list by referrring to their index value
print my_list[0] # prints "hi"
print my_list[2] # prints 100.2

# use negative numbers to start at the back
print my_list[-1] # prints "6" - the last item

# you can access part of a list with a ":"
my_list[1:3] # will be [45, 100.2, "whatever"]
```

#### Loops

Loops allow us to execute code, or perform actions, for every item inside of a list.

Here the variable `val` represents the value of each item in our list. The indented code will run once for each item.

```python
my_list = ["one", "two", "three"]

# the following will print "one" "two" "three" each on their own line
for val in my_list:
	print(item)
```

You can also make a loop with the `while` keyword. `while` takes an expression, and will run the indented code as long as the expression you provide evaluates to `True`.

```python

year = 1800

# print out the year, as long as it is less than 1848

while year < 1848:
	print(year)
	year = year + 1
```


#### Sorting

You can sort a list with the `sorted` method:

```python
words = ["a", "spectre", "is", "haunting", "europe"]
sorted_words = sorted(words)
```

---

### Dictionaries

A dictionary is a data structure that stores key and value pairs. It's like a list, but instead of being indexed numerically, it's indexed with keys that you provide. Keys are typically strings, but can be other data types as well. Values can be any Python data type.

```python
person = {"first_name": "Karl", "last_name": "Marx", "is_alive": False}
```

To access a value in a dictionary, reference it's key like so:

```python

# prints "Karl"
print(person["first_name"])

# prints "Marx"
print(person["last_name"])

```

Modify an existing value:

```python
# changes the value of "first_name" to "Karla"
person["first_name"] = "Karla"
```

Add a new key/value:

```python
person["age"] = 205
```

### Converting strings to lists and back

`join()` converts a list to a string, and `split()` converts a string to a list. This is really useful for doing things like extracting all the words of a sentence, editing them, and then turning them back into another sentence.

```python
sentence = "A specter is haunting Europe"

# transform the sentence into a list, split by the character I provide
words = sentence.split(" ")

# sort the words alphabetically
words = sorted(words)

# take a list and turn it back into a single string
# You give it a joining character, and call the join([list]) function on it
new_sentence = " ".join(words)
```

### Randomness

Sometimes it's fun to let the computer make decisions for you. Sometimes it is not fun. If you want to do this, you can use the `random` module. Although this module comes with Python, we need to tell Python that we want to make use of it with the `import` keyword in order to access its methods.

```python
# import the "random" module, to access its functions
import random

words = ["A", "spectre", "is", "haunting", "my", "computer"]

# reorder our words list into a random order. NOTE: it modifies the original list
random.shuffle(words)

# get a random item
random_item = random.choice()

# get a random integer value between 1 and 10:
random_number = random.randint(1, 10)

# get a random floating point number between 1 and 100:
random_float = random.uniform(1, 100)
```

### Repeating yourself

If you need to run the same operation multiple times, you can use Python's built in `range()` method, which returns a series of numbers.

```python
# prints the numbers 0 through 9
for i in range(10):
  print(i)
```

You can combine this with `random.choice()` to generate a list of random words:

```python

words = ["spectre", "ghost", "usb microphone", "wool coat"]

for i in range(10):
  print("A " + random.choice(words) + " is haunting Europe.")
```

### Reading files

To open a file in Python, use the `open()` keyword function. The function takes two arguments. The first is the name of the file to open, and the second is a flag that states if we are opening the file with the intent of *reading* to it (use "r"), or *writing* to it (use "w").

Once we have opened a file, we use the `read` function to grab it's contents and return then as a string.

In this example, we open a file and store its contents in a string. We then uppercase the entire file and print it to the screen.

```python
content = open("communist_manifesto.txt", "r").read()
loud_manifesto = content.upper()
print(loud_manifesto)
```

You can also store a file as a list of lines using `readlines()` instead of `read()`

This example prints the first 5 characters of a text file.

```python
all_lines = open("communist_manifesto.txt", "r").readlines()
for line in all_lines:
  print(line[0:5])
```

### Saving output

You can save the output from a Python script in the same way you might for any command line application. You can also pipe the output to other command line programs:

```bash
# pipe the output of python to say
python3 hello.py | say

# save the output of python to a file
# python3 hello.py > output.txt
```

When you write a Python script it's like you're making a little command line program of your own.

#### Writing to a file

You can also use the `write()` method in python to save a file:

```python
content = open("manifesto.txt").read()

content = content.replace(" ", "!")

# We create an output file
# we use the open() function, but for writing
# and write the contents
open("new_manifesto.txt", "w").write(content)
```

