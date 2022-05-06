#! /usr/bin/env python3

""" titlecaseclipboard.py
Usage:
    - First way:  titlecaseclipboard.py this is the sentence
        Writes to standard output: This Is the Sentence
    - Second way: titlecaseclipboard.py
        Takes the text in the clipboard (if any), converts it to
        smart title case, copies it back to the clipboard,
        and writes it to standard output.
"""

import sys
import pyperclip
from titlecase import titlecase
import re

# -------------------------------------------------------------------
def main():
    """ Main function. """
    clipboard = False
    argv = sys.argv[1:]

    if not argv or argv[0] == '':
        # try clipboard
        inputtext = pyperclip.paste()
        if inputtext != "".strip():
            clipboard = True
        else:
            # no arguments, no clipboard text
            sys.exit(1)
    else:
        inputtext = ' '.join(argv)
        inputtext = inputtext.strip()

    outputtext = titlecase(inputtext.casefold())
    outputtext = re.sub(r'\n', ' ', outputtext)
    outputtext = re.sub(r' {2,}', ' ', outputtext)

    if clipboard:
        pyperclip.copy(outputtext)

    print(outputtext, file=sys.stdout)


# -----------------------------------------------------------------
if __name__ == '__main__':
    main()
