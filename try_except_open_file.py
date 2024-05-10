# try_except_open_file.py

try:
    #  Run this sensitive code
    with open("data/text.csv", mode="w") as fp:
        text = fp.read()
except Exception as e:
    print(f"{e}")
else:
    print("No error")
finally:
    print("Always executed. Cleanup")
    fp.close()


