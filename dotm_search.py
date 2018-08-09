#!/usr/bin/env python
import sys
import os
import glob
import zipfile
"""
Given a directory path, this searches all files in the path for a given text string 
within the 'word/document.xml' section of a MSWord .dotm file.
"""

# Your awesome code begins here!
def file_search(char, diir):
    print "Searching directory {} for text '{}'...".format(diir, char)
    os.chdir(diir)
    files = glob.glob('*.dotm')
    searched_files = 0
    matches = 0
    for zipped in files:
        reader = zipfile.ZipFile(zipped, 'r')
        information = reader.read('word/document.xml')
        searched_files += 1
        for counter, value in enumerate(information):
            if value == char:
                matches += 1
                money = counter
                print "Match found in file {}\{}".format(diir, zipped)
                print "...{}...".format(information[money-40:money+40])
    print "Total dotm files searched: {}".format(searched_files)
    print "Total dotm files matched: {}".format(matches)

def main():
    directory = "."
    if len(sys.argv) > 2:
        if len(sys.argv) > 3:
            if sys.argv[2] == '--dir':
                character = sys.argv[1]
                directory = sys.argv[3]
                file_search(character, directory)
            else:
                print 'usage: ./dotm_search.py character --dir dir'
            sys.exit(1)
        else:
            print 'usage: ./dotm_search.py character --dir dir'
            sys.exit(1)
    elif len(sys.argv) > 1:
        character = sys.argv[1]
        file_search(character, directory)
    else:
        print 'usage: ./dotm_search.py character --dir dir'
        sys.exit(1)
        

if __name__ == '__main__':
  main()