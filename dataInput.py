# Getting address

import sys, pyperclip

def dataInput():
    """
    Getting input address
    """
    if len(sys.argv) > 1:
        # Getting the address from the command line.
        address = ' '.join(sys.argv[1:])
    else:
        # Getting the adress from the clipboard
        address = pyperclip.paste()
    
    return address