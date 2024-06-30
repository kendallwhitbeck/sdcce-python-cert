#-------------------------------------------------------------------------------
# Name:        main
# Purpose:
#
# Author:      Lydell
#
# Created:     20/02/2024
# Copyright:   (c) Lydell 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import module1

def main():
    module1.some_function()
    print(__name__)

# If we are called directly, then proceed to the main().
# If we are called as a module.
if __name__ == '__main__':
    main()
else:
    # This module (main) should do nothing if it's called as an import
    pass
