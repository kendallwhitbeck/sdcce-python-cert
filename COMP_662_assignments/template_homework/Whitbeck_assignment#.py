# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Assignment <#>TODO: <shortTitle>TODO
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 662: Programming Databases with Python
"""

import os  # clear terminal window text based on Windows or Linux/Mac OS.

def function_placeholder(): # TODO
    pass # TODO implement code
    return # TBD

def main():
    # Clear terminal window text.
    if os.name == 'nt':  # Windows OS
        os.system('cls')
    else:  # Linux or MacOS.
        os.system('clear')

    pass # TODO implement code

# Ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()