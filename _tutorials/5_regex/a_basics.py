#!/usr/bin/env python3
import re

# ************************
# \d any number
# \D any but number

# \s any whitespace
# \S any but space

# \w any word
# \W any but word

# \b space followed by word
# \e escape
# \f formfeed
# \n newline
# \r carriage return 
# \t tab

# ************************
# ? 0 or 1 repetitions
# * 0 or more repetitions
# \d{5} 5 digits


file = "./data/randomcharacters.txt"
with open(file, 'r') as f:

    strToSearch = ""

    for line in f:
        strToSearch += line
    
    # print(strToSearch)

    regex = "Lorem"
    # pathFinder = re.compile(regex)
    pathFinder = re.compile(regex, re.IGNORECASE)
    findPath = re.search(pathFinder, strToSearch)

    print(findPath.group())
    print(findPath.start())
    print(findPath.end())
    print(findPath.span())

    findAllPath = re.findall(pathFinder, strToSearch)

    for i in findAllPath:
        print(i)