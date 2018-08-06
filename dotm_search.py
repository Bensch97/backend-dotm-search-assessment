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
    if len(sys.argv) < 3:
        if len(sys.argv) < 2:
            print 'usage: ./dotm_search.py {--text | --dir}'
            sys.exit(1)
        else:
            character = sys.argv[1]
            directory = "./dotm_files"
            file_search(character, directory)
    character = sys.argv[1]
    directory = sys.argv[2]
    file_search(character, directory)

if __name__ == '__main__':
  main()