# os_playground.py

import os

os.system('cls')  # clear terminal window text in Windows OS

# os.system('clear')  # clear terminal window text in Linux OS

# Clear terminal window text based on Windows OS or Linux OS.
if os.name == 'nt':  # Windows OS
    os.system('cls')
    print("cleared the terminal window text in Windows OS")
else:  # Linux OS
    os.system('clear')
    print("cleared the terminal window text in non-Windows OS")


# Check if operating system is Windows and which shell is being used.
if os.name == 'nt':
    # Windows operating system
    if 'POWERSHELL' in os.environ.get('SHELL', ''):
        print('PowerShell')
    elif 'bash' in os.environ.get('SHELL', '').lower():
        print('Git Bash')
    else:
        print('Windows Command Prompt')
else:
    print('Non-Windows OS')