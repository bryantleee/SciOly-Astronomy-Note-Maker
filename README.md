# Astronomy Science Olympiad Notes Starter
A quick script I made that automatically saves webpages as PDFs to use as notes for later in the Astronomy Science Olympiad. It will Google each topic and automatically save all websites from the first page of results in Google. Each topic gets its own folder.   

It is not perfect and some pages will have errors, but it is a good place to start and hopefully will save some time.

## How to Use
In the command line:
```
$ python make_notes.py <PATH_TO_TEXT_FILE_WITH_TOPICS> <PATH_TO_SAVE_FOLDERS_IN>
```
Note that if you do not input a path to save folders in, it will default to saving the files in the current directory.

For example:  
```
$ python make_notes.py requirements.txt ./Astronomy
```
will read the requirements from requirements.txt and save the notes in the folder "Astronomy".

## Formating the Topics
Save the requirements in a text file, with one topic on each line. 

## Dependencies
- pdfkit
- bs4