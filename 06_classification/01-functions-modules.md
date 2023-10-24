# Python Functions and Modules

## Functions

A function lets you execute multiple lines of code together.

To define a function in Python, use the `def` keyword, followed by your function name, opening and closing parentheses, and by a colon.

```python

# define a function
def spectre():
	print("a spectre is haunting this function")
	print("the spectre of python")
	
# call the function
spectre()
```

Functions can take arguments. These are values that get passed into the function when it is called.

```python
def spectre(noun):
	sentence = "a spectre is haunting " + noun
	print(sentence)
	
spectre("computer") # prints 'a spectre is haunting this computer`
```

Multiple arguments are separated by commas:

```python
def spectre(noun, gerund):
	sentence = "a spectre is " + gerund +  " this " + noun
	print(sentence)
	
spectre("script", "heating") # prints 'a spectre is heating this script`
```

Arguments can also have default values:

```python
def spectre(noun, gerund="haunting"):
	sentence = "a spectre is " + gerund +  " this " + noun
	print(sentence)
	
spectre("script") # prints 'a spectre is haunting this script`
```

You send the function arguments in an order, by specifying the argument name when you call the function:

```python
spectre(gerund="heating", noun="terminal")
```

Finally, functions can return values:

```python
def spectre(noun, gerund="haunting"):
	sentence = "a spectre is " + gerund +  " this " + noun
	return sentence
	
words = spectre("script")
print(words)
```

## Modules

A module is a group of functions and variables that can be imported into your scripts. Every python file can act as a module.

Let's imagine we have two files: `app.py` and `greetings.py`.

In `greetings.py` we have a simple function:

```python
# greetings.py

def say_hi(name):
	print("hello " + name)

```

We now import `greetings` into `app.py` *if* they are in the same folder:

```python
# app.py

import greetings

greetings.say_hi("Karl")
```

This lets you write re-usable code.
