Similar Image Filter

A script that lets you filter all similar images in your image library!

This project was designed to solve my own family's image storage problem. Nobody takes just one photo of a particular scene; we usually take a lot of similar pictures, especially my dad who spams the shutter button on his phone atleast 3 times. This results in a huge amount of photos that are practically the same picture, resulting in a lot of unnecessary storage hog. This script aims to find such similar photos and lets you decide which ones you want to keep, or automatically deletes all but one photos from a group of similar photos. 

What it does :-
-- Recursively goes through the selected folder to identify and index image files.
-- Calcultes the perceptual hash of all image files that it found.
-- Groups images based on the similarity of their perceptual hashes.

Dependencies :-
-- numpy
-- scipy
-- PIL
-- PyQt5

Usage :-
python3  openWindow.py

File Description :-
-- file_io.py : Helper functions for scanning image files recursively through a folder.
-- image.py : Image functions for calculating perceptual hash and grouping.
-- openWindow.py, filterFolder_ui.py, photoSelector_ui.py : PyQt5 python files for GUI.

Screenshots :- 

Main Window
![Alt text](screenshots/mainWindow.png?raw=true "Main Window")



Select Folder
![Alt text](screenshots/selectFolder_selected.png?raw=true "Select Folder")



Processing
![Alt text](screenshots/processing.png?raw=true "Processing")

![Alt text](screenshots/done.png?raw=true "Processing Complete")



Decide which photos to keep
![Alt text](screenshots/selectDelete.png?raw=true "Decide")