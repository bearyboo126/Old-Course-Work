#!/usr/bin/python3
# Name: Erin Ledford
# Class: BIOI 3500, Spring 2021
# Assignment #: Assignment 3
# Due date: February 12th, 2021
#
# Honor Pledge: On my honor as a student of the University of Nebraska at
#               Omaha, I have neither given nor recieved unauthorized help on
#               this programming assignment.
#
# NAME: Erin Ledford
# EMAIL: eledford@unomaha.edu
#
# Partners: NONE
#
# This program converts a multisequence human reference sequence GenBank
# FASTA file into a tab-delimited format.

import getopt
import sys

class eledford_Assign3:
   
    def main():

        # Read in the command-line arguments into the opts list
        try:
            opts, args = getopt.getopt(sys.argv[1:],"i:o:s")

        except getopt.GetoptError as err:

            # Redirect STDERR to STDOUT (insures screen display)
            sys.stdout = sys.stderr

            # Print help information
            print(str(err))

            # Print usage information; usage is the name of a
            # function (declared elsewhere) that displays usage
            # information (just a series of print statements
            usage()

            # Exit the program
            sys.exit(2)

        # Reads the input file from the keyboard
        fileIn = sys.stdin

        # Reads the output to the screen
        fileOut = sys.stdout

        # A variable to check if the sequence is included in the file
        includeSeq = False

        # Process the opt and arg lists displaying the argument of 
        # each option
        for (opt, arg) in opts:

            # If -i is chosen, the input file is changed based
            # on input from the command-line
            if (opt == '-i'):
                fileIn = open(arg, 'r')
            
            # If -o is chosen, the output file is changed based
            # on input from the command-line
            if (opt == '-o'):
                fileOut = open(arg, 'w')
            
            # If -s is chosen, the sequence is included in the file
            if (opt == '-s'):
                includeSeq = True

        # A variable to find the specific line and not include the
        # sequence
        searchKey = ">gi|"

        # The output lines grabbed from searching the input file
        outputLines = []

        # If includeSeq is false, it searches for specific lines
        # and changes them into a tab delimited format
        if includeSeq == False:
            for line in fileIn:
                if searchKey in line:
                    outputLines += line
                line = fileIn.readline()
            outputLines = ''.join(outputLines)
            outputLines = outputLines.replace(">gi|", "")
            outputLines = outputLines.replace("|", "\t")
            outputLines = outputLines.replace("ref", "")
            
            # Writes out the output to the file or screen based on 
            # command-line arguments
            fileOut.write(outputLines)

        # Else if includeSeq is true, it simply replaces unneeded lines
        # with lines required for tab delimited format
        else:
            for line in fileIn:
                line = line.replace(">gi|","")
                line = line.replace("|", "\t")
                line = line.replace("ref", "")
                
                # Writes out the output to the file or screen based on
                # command-line arguments
                fileOut.write(line)
                line = fileIn.readline()
                
        # Closes the input file
        fileIn.close()

        # Closes the output file
        fileOut.close()
    
    if __name__ == '__main__':
        main()
