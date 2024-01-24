# Dapp
**The Desktop APP programming language**

Welcome to DAPP, a python based language. You can create your own desktop app with dapp.

## Installation

### How to run
Enter the commands into a file.

Then run this:
```bash
chmod u+x run
./run /path/to/commands.txt
```

Check the [API](#api) Section for the docs for the commands.

### App
Run the following commands for a nice try it zone:
```bash
npm i
npm start
```

NOTE: You need node.js, npm, and python and bash

# Documentation
## Tutorial

Welcome! This tutorial will cover parts of the Dapp programming language.


### Setup and Introduction

Before we actual get into the tutorial, we will just clone and `cd` into the directory.

```bash
git clone https://github.com/arjunj132/dapp.git
cd dapp
```

Let's start our tutorial! We'll first start our development enviroment:

First we install the dependencies:

```bash
npm i
```

(You need node, python and npm)

That good. Now we just run the app:

```bash
npm start
```

Now a screen pops up. It has 2 fields: The executable and the code

Nice. Now, use <kbd>Control</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd>, or open the `View` menu and click `Toggle Developer Tools`.

This helps because the developer tools logs all the errors from the dapp source.

Start by typing your executable into the 1st box. It is usually `python3` for linux and mac, and `py` or `python` for windows.

Now click run. Nothing will happen. But one thing will log in the console:

```javascript
DAPP: WARNING: App not initilized
```

That's not good. That bascally means, we are doing nothing.

Now here is the exiting part.

Lets fix that. The easiest way is just to initilize it. That's not hard. Type this into the `Enter code here` box:

```javascript
init
```

Nice. The app window's appear's and we are now saved. But there is noting on it. So what do we do?

We now code!!! By the end of this tutorial, you will be able to build a interactive `Hello World!` app.

### Quick Start

To start this app, we need to learn how to put a word on our screen. Let's write "Hello World" on the widget.

This is really easy. The syntax for it is:

```javascript
text:text
```

So, following this, we should get:
```javascript
init,
text:Hello World!
```

Notice we added a comma after `init` becuase that is a seperator for each line of code.

So lets run it.

You should see the words `Hello World!` at the app.

Congrats! You made your first app. But this is not all. You can check the `API` section for more tools that you can use.

## API

### **Seperators:**

### `,` (comma) seperator

The character `,` seperates 2 commands.

For example:
```javascript
init,
// another command ,
```

### `//` (comment)

This symbol is completly ignored by Dapp.

After the comment, you add a `,` (Command seperator) and add the next line of code under it.

An example of a comment would be:

```javascript
// A comment!! ,
init
```

### `:` (colon) seperator
The colon sepeator seperates 2 parts of a command. The 2nd half is used as data necassary for the app.

An example of this is:

```javascript
// ... ,
title: A app
```

In this example, the `A app` is a the data being sent to the server.

### `=` (equal) seperator

The equal seperator is used when you need more data when using the colon seperator. It can have unlimited halves, and are used to seperate the data from each other. For example:

```javascript
// ... ,
button: Click me!=print('Hello world!')
```

Here, we created a button that prints `Hello World`. For more information, check the `button` API.

### `init`

A command to start the Tkinter window. This command is nessasary to do any other command in Dapp.

Example to create a blank app:

```javascript
init
```

### `title`

The title API sets a title to the current Tkinter window. 


For example, in this we initilize a app and add a title to the app:

```javascript
init,
title: A dapp app
```

### `text`
Add a text widget to your app.

```javascript
init,
text: Some text
```

### `geometry`

Change the size of your app.

```javascript
init,
geometry: 1000x1000
```

### `img`

The image feature has 3 arguments using the `=` seperator.

1. The image src
2. The image's x coordinate
3. The image's y coordinate

An example of this command:

```javascript
init,
img: src.png=0=0
```

This places the image `src.png` at the x and y coordinates `0x0`.

### `button`

**NOTE**: The button attribute is the only attribute that allows you to run python code in your app. Please do not misuse this command because it can be dangerous. Do not run code without knowing what it does.

This command inserts a button that runs a python script when clicked.

It takes 2 arguments:

1. The name of the button
2. The python code it does

For example, this app creates a button that can be clicked and then it prints 'Hello World' in the console.

```javascript
init,
button: Print "Hello World"=print('Hello World!')
```

### `cli`
The CLI (Command Line Interface) command is a command to start the Dapp CLI.

The CLI must be the first command in your script. You can also start the CLI by running the source script directly:

```bash
python3 -m app cli
```

The CLI has 2 sessions. So, exit the CLI, you must use the `exit` command 2 times: to exit the defualt version and to exit the `UNKNOWN` version.

### `exit`
Raise a `SystemExit` in the current session. 

---
&copy; Arjun
