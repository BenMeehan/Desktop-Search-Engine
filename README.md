# Desktop File Index Search
This Python application allows you to search for files and folders super quick especially when there are so many of them.
![Imgur](https://imgur.com/ALWkkjC)
## How to run

Just clone this repository into a folder and run the gui.py file.

## How it works

This project uses several concepts from OS, DBMS and Theory of Computation.

It uses the concept of indexing to store the files and folders list in a object serialized format for later use in the disk the first time it is run on a directory. This makes the subsequent search operations very fast as there is very little Disk I/O happening.

It uses regular expressions to search the files and folders.

## Options

We can index and search 
 - Files
 - Folders 
 
 Search can be done using 
 - Prefix 
 - Suffix 
 - All (searches the whole name)

## Python libraries used

This project uses the following libraries 

 - os module (built-in)
 - re (built-in)
 - pickle (built-in) 

Pickle is used to serialize and deserialize the data.

## Demo

[Youtube Link](https://youtu.be/vVHxux9E3fs)
