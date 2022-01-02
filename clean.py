"""Cleans up artifacts of local documentation build."""

from pathlib import Path
from shutil import rmtree

root = Path(__file__).parent
folders = [root/'HTML']
folder_names = ['__pycache__']
for folder_name in folder_names:
    for folder in root.rglob(folder_name):
        folders.append(folder)

for folder in folders:
    if folder.is_dir():
        rmtree(folder, ignore_errors=True)
