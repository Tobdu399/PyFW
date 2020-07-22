# PyFW
Python File Writer

# Setup
- Create a "bin" directory in your home folder:
    _sudo mkdir ~/bin_
- Go to the folder where "pyfw.py" is located and make it executable:
    _sudo chmod +x pyfw.py_
- And create a symbolic link to the file
    _ln -s $PWD/pyfw.py ~/bin/pyfw_
- Done!

# Usage
- Run the program by simply typing "pyfw" in your terminal
- The program asks for a file name, in what you would like to save your text
- You have 62 lines to write in, and after you have gone through every line, the program saves the text in a text file with the name you specified.
- You can cancel/discard changes by pressing CTRL+C

# Commands
- This program has a couple text align commands:
- CENTER
- RIGHT

- Example:
    _Presentation -- CENTER_    (to align the text to the center)
    _Presentation -- RIGHT_     (to align the text to the right)
