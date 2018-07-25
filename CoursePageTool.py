'''This is a project for generating clean tables of course information from the raw HTML
output by Auburn's Course Search tool.  It will take in the HTML as a text file and output a .csv file.
I want to use BeautifulSoup to parse the HTML and get the right pieces, pandas to get it into a data frame,
and then when it comes time to write the file I want to create a filename based on user input.'''

import re
import sys
import os
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup


def get_soup():
    rawHTML = open(sys.argv[1], 'r')
    soup = BeautifulSoup(rawHTML, 'html.parser')
    rawHTML.close()
    return soup

def get_courses(soup):
    links = soup.find_all('a')
    textList = []
    for link in links:
        text = link.get_text()
        textList.append(text)
    mess = '\n'.join(textList)
    regex = re.compile(r'(.* - .*)')
    courseList = re.findall(regex, mess)
    return courseList


def clean_courses(courseList):
    readyList = []

    for i in courseList:
        readyList.append(i.split(" - "))
    return readyList


def assemble_filename():
    filename = str(sys.argv[2]) + str(sys.argv[3]) + str(sys.argv[4]) + '.csv'
    return filename

pageMess = get_soup()

courseList = get_courses(pageMess)

# instList = ["Carmen P Brysch", "Adam Andrew Payne", "Carmen P Brysch", "James Alan Norwood",
#            "Carmen P Brysch", "James Alan Norwood", "James Alan Norwood", "TBA",
#            "Adam Andrew Payne", "TBA", "Philip Lynn Chaney", "Adam Andrew Payne",
#            "Ronald Dale Lewis", "Carmen P Brysch", "Stephanie Rose Rogers", "TBA",
#            "TBA", "TBA", "TBA", "Chandana Mitra", "Adam Andrew Payne", "Philip Lynn Chaney",
#            "Stephanie L. Shepherd", "Luke Jonathon Marzen", "Stephanie Rose Rogers", "Donn Andrew Rodekohr",
#            "Christopher George Burton", "TBA", "Chandana Mitra", "Adam Andrew Payne",
#            "Philip Lynn Chaney", "Stephanie L. Shepherd", "Luke Jonathon Marzen", "Stephanie Rose Rogers",
#            "Donn Andrew Rodekohr", "Christopher George Burton", "TBA", "TBA", "TBA", "TBA",
#            "TBA", "TBA", "TBA", "Christopher George Burton", "Philip Lynn Chaney", "Luke Jonathon Marzen",
#            "Chandana Mitra", "Stephanie L. Shepherd"]

courseData = pd.DataFrame(clean_courses(courseList), columns = ["Course Title", "CRN", "Course Number", "Section"])

# instData = pd.DataFrame(instList, columns = ["Instructor"])

# finalFrame = pd.concat([courseData, instData], axis = 1)

finalTable = courseData.to_csv(assemble_filename(), header = True, index = False)
