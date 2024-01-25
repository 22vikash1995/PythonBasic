import os

if os.path.exists("D://Python/file"):
    os.rmdir("D://Python/file")
else:
    print("The file does not exist")

