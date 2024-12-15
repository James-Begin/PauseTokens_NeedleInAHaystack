import asyncio
import glob
import json
import os
import time
import re

base_dir = os.path.abspath(os.path.dirname(__file__))

source_dir = os.path.join(base_dir, "PaulGrahamEssays")
dest_dir = os.path.join(base_dir, "Essaystest1")

def insert_match(match):
    return match.group(0) + " <PAUSE> "

for file in glob.glob(os.path.join(source_dir, "*.txt")):
    try:
        with open(file, 'r') as f:
            text = f.read()
            edit = re.sub(r'\]', insert_match, text)

        filename = os.path.basename(file)
        new_filename = os.path.splitext(filename)[0] + "test.txt"
        new_file_path = os.path.join(dest_dir, new_filename)

        with open(new_file_path, 'w') as x:
            x.write(edit)
    except IOError as e:
        print(f"Error processing {file}: {e}")



