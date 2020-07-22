# PyFW
Python File Writer

# Setup
- Create a "bin" directory in your home folder:
    *sudo mkdir ~/bin*
- Go to the folder where "pyfw.py" is located and make it executable:
    *sudo chmod +x pyfw.py*
- And create a symbolic link to the file
    *ln -s $PWD/pyfw.py ~/bin/pyfw*
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

- Example 1:
    *Presentation -- CENTER*    (to align the text to the center)
- Example 2:
    *Presentation -- RIGHT*     (to align the text to the right)
