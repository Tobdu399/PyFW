#!/usr/bin/env python3
import os

x = 80
y = 64

text = ""

green = "\u001b[32m"
red = "\u001b[31m"
blue = "\u001b[36m"
yellow = "\u001b[33m"
reset = "\u001b[0m"

def main():
    try:
        global text

        os.system("clear")
        file_preview = []

        print(yellow + "\u001b[1mPython File Writer v1.0\n" + reset)
        file_name = input(blue + "Give name for your file (optional):\n> " + reset)

        if file_name == "":
            file_name = "unnamed_pyfw_file"

        print()
        print(blue + "="*int(x) + reset)
        print(green + "Width: " + str(x-2) + str(" "*int(x - len("Width:   ")-len("Font:   "))) + "Font: 10" + reset)
        print(green + "Height: " + str(y-2) + str(" "*int(x - len("Height:   ")-len("Size:   "))) + "Size: A4" + reset)
        print(blue + "="*int(x) + reset)

        file_preview.append(("=" * x) + "\n")

        for line in range(0, y-2):
            input_space = 2
            if line > 8:
                input_space = 1
            
            line_text  = input(yellow + str(line+1) + "." + " "*input_space + reset)
            if len(line_text) > x-4:
                print(red + "Line too long!\n" + reset)

                while len(line_text) > x-4:
                    line_text = line_text[:-1]

            try:
                styled_text, style = line_text.split(" -- ")
                free_space = x-2 - len(styled_text)
                
                if "CENTER" in style:
                    text = "*" + (" "*int(free_space/2)) + styled_text
                elif "RIGHT" in style:
                    text = "*" + (" "*int(free_space-1)) + styled_text
            
            except(ValueError):
                text = "* " + line_text

            while len(text) != x-1:
                text += " "
            
            text += "*\n"
            file_preview.append(text)

        file_preview.append(("=" * x) + "\n")


        with open(os.getcwd() + "/" + file_name + ".txt", "w") as output:
            for line_to_write in file_preview:
                output.write(line_to_write)
            output.close()

        print(blue + "="*int(x-1) + reset)
        print(yellow + "\n\u001b[1mFile saved in \"" + blue + os.getcwd() + reset + yellow +"\"\n" + reset)

    except(KeyboardInterrupt):
        print(red + "\n\n\u001b[1mProcess interrupted! File not saved.\n" + reset)

main()
