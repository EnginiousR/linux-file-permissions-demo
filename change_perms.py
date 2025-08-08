import os

# Change permissions of example.txt to rwxrwxr-x
os.chmod("example.txt", 0o775)

print("Permissions changed to rwxrwxr-x")


