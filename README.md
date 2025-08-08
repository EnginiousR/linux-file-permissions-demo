# linux-file-permissions-demo

## Overview
This project demonstrates:
1. Understanding **Linux file permissions**.
2. Creating a **flowchart** to explain permissions.
3. Using **Python** to change file permissions with the `chmod` command.

The final goal is to set file permissions to **`rwxrwxr-x`** for a given file.

---

## Flowchart
The flowchart illustrates the process of understanding and applying file permissions

---

## Steps Demonstrated

### 1️ Create a working directory
mkdir ~/perms_demo
cd ~/perms_demo

### 2 Create a sample file
echo "hello" > example.txt

### 3 Write a Python script to change permissions
import os

file_path = "example.txt"
os.chmod(file_path, 0o775)  # rwxrwxr-x
print("Permissions changed to rwxrwxr-x")

### 4 Run the script
python3 change_perms.py

## Project Structure
نسخ الكود
├── permissions_flowchart_fixed.png   # Flowchart explaining file permissions
├── change_perms.py                    # Python script to change permissions
├── chmod_demo.png                     # Screenshot of the chmod process


### Key Learning Points
File permissions format: rwxrwxr-x
r → Read
w → Write
x → Execute
User groups: Owner, Group, Others
Changing permissions in Python: Using os.chmod()
Octal representation: 0o775 → rwxrwxr-x
