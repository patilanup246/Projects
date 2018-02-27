"""
Authors: Dr. Berardinelli and ???
Date: November 2017
File: Lab10starter.py
Description: Starter file for MATH 146 Programming 1 Fall 2017
    Includes function stubs for
    And complete function definitions for 
    The main function in this file reads a CSV file of quarterback 
    stats and outputs a CSV file of QB ratings.
"""

from statistics import median
import csv

def writeQBratings(filename, ratinglist):
    """ This function should open a csv file given by the string filename.
    ratinglist is a list of lists: each element in ratinglist is 
    of the form [ QBlastname, teamname, QBrating ]
    This function should write this information in csv format to filename
    and return nothing """

    
    # Student: Write this function!
    
    file_export = open(filename, 'w', newline='',encoding='utf-8')
    wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
    for i in ratinglist:
        wr.writerow(i)

    print("Function not written yet")

def computeQBrating(statlist):
    """ This function takes in a list of the form 
    [completions, attempts, passingyards, interceptions, touchdowns]
    for a single QB and returns the passer rating. """

    comp = float(statlist[0])
    att = float(statlist[1])
    yds = float(statlist[2])
    int = float(statlist[3])
    td = float(statlist[4])

    a = median([(comp / att - 0.3) * 5, 0, 2.375])
    b = median([(yds / att - 3) * 0.25, 0, 2.375])
    c = median([td / att * 20, 0, 2.375])
    d = median([2.375 - (int / att * 25), 0, 2.375])
    
    return (a+b+c+d)/6*100

def main():
    """ This function should read QB data from Lab10input.csv
    compute the QB rating for each line of the file,
    then write the QB rating to Lab10output.csv """


    """ This first part opens the csv file Lab10input.csv,
    reads the contents using the reader in the csv python 
    module, then process the input, computes the QB rating,
    and stores that information in the list qbratings. """
    with open("Lab10input.csv", 'r') as csvfile:
        allqbstats = csv.reader(csvfile, delimiter=',')

        qbratings = []
        first_row = True
        for row in allqbstats:
            # skip the column headers
            if first_row:
                qbratings.append(["Last Name", "Team", "QB rating"])
                first_row = False
                continue
            
            qbratings.append([row[0],row[1],computeQBrating(row[2:])])


    """ This is where your csv writing function is called """
    writeQBratings("Lab10output.csv",qbratings)
    #print ('Value of qbratings - '+str(qbratings))
        

    print("Done.")
    return

main()
