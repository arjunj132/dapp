# Dependencies
from pydoc import cli
import sys
from tkinter import *

# under this comment, you can add functions and 
# run the functions in 
# your dapp app's buttons
# here's a demo:

def demo():
    print('Hello World!')

# okay, you can stop editing now, for security reasons

# define all vars
global root
global code
global args
root = ''
code = ''
args = ''

# define all commands in dapp
def COMMANDS():
    global root
    if x == 'init' or x == ' init':
        root = Tk()
    elif 'title:' in x  or ' title:' in x:
        root.title(x.split(':')[1])
    elif 'text:' in x or ' text:' in x:
        Label(root, text = x.split(':')[1]).pack()
    elif 'geometry:' in x or ' geometry:' in x:
        root.geometry(x.split(':')[1])
    elif 'img:' in x or ' img:' in x:
        photo = PhotoImage(file=x.split(':')[1].split('=')[0])
        img = Label(root, image=photo)
        img.image = photo
        img.place(x=x.split(':')[1].split('=')[1], y=x.split(':')[1].split('=')[2])
    elif 'button:' in x or ' buttons:' in x:
        test = x.split(':')[1]
        test1 = test.split('=')
        Button(root, text=test1[0], command=lambda: exec(test1[1])).pack()
        sys.stdout.flush()
    elif x == ' ':
        pass
    elif x == '':
        pass
    elif '//' in x:
        pass
    elif x == 'exit':
        sys.exit()
    else:
        print("DAPP: ERROR: Unrecognized expression at '" + x + "'")

# get every command that user inputted
args = sys.argv
del args[0]
for f in args:
    code = code + f
code = code.split(',')

# find if cli is active, else activate the commands
if (code[0] == 'cli'):
    try:
        with open('version.txt', 'r') as f:
            print('Dapp ' + f.read() + ' on Python ' + sys.version + ' on ' + sys.platform)
            while True:
                ask = input('>>> ')
                code = ask.replace(',', '').split(',')
                for x in code:
                    COMMANDS()
    except:
        print('Dapp ' + 'UNKNOWN' + ' on Python ' + 'VERSION UNKNOWN' + ' on ' + 'PLATFORM UNKNOWN')
        while True:
            ask = input('>>> ')
            code = ask.replace(',', '').split(',')
            for x in code:
                COMMANDS()
    
else:
    # loop through every line of code
    for x in code:
        COMMANDS()
    # Run app
    try:
        root.mainloop()
    except:
        print('DAPP: WARNING: App not initilized')
    sys.stdout.flush()