#!/usr/bin/python3
# Name: Erin Ledford
# Class: BIOI 3500, Spring 2021
# Assignment #: Assignment 4
# Due Date: February 19th, 2021
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
# This program converts a multirecord Genbank file into a multisequence FASTA file.

import sys
import getopt

class eledford_Assign4:


    def main():

        # Read in the command-line arguments into the opts list
        try:
            opts, args = getopt.getopt(sys.argv[1:], "i:o:l:")
        
        except getopt.GetoptError as err:

            # Redirect STDERR to STDOUT (insures screen display)
            sys.stdout = sys.stderr

            # Print help information
            print(str(err))

            # Print usage information; usage is the name of a
            # function (declared elsewhere) that displays usage
            # information (just a series of print statements)
            usage()

            # Exit the program
            sys.exit(2)
        
        
        # Reads the input file from the keyboard
        fileIn = sys.stdin

        # Reads the output to the screen
        fileOut = sys.stdout

        # The first line of the output file
        firstLine = []

        # The second line of the output file
        secondLine = []

        # The width of the sequence
        width = 70
        
        # Processes the opt and arg lists displaying the argument for
        # each option
        for (opt, arg) in opts:
            
            # If opt is given, the input file is changed to the arg
            if (opt == "-i"):
                fileIn = open(arg, 'r')

            # If opt is given, the output file is changed to the arg
            if (opt == "-o"):
                fileOut = open(arg, 'w')

            # If opt is given, the width of the sequence is changed
            # to the arg
            if (opt == "-l"):
                width = int(arg)


        # The sequence of the file
        sequence = ""
        
        # Reads through the file and finds the first line, second line,
        # and the sequence
        for line in fileIn:
            if (line.startswith("DEFINITION")):
                secondLine = line.replace('DEFINITION', '|')
            if (line.startswith("VERSION")):
                firstLine  = line.replace("VERSION     ", ">accession|")
            if (line.startswith("ORIGIN")):
                while (not line.startswith("//")):
                    sequence += line
                    line = fileIn.readline()


        # First line is added to second line to put them together
        firstLine += secondLine

        # The output is joined together in a string
        outputLines = ''.join(firstLine)

        # Fixes the output string for correct formatting
        outputLines = outputLines.replace("\n", "")

        # Corrects the sequence so it may be formatted in formatSeq
        sequence = sequence.replace("ORIGIN", "")
        sequence = sequence.replace("//", "")
        sequence = sequence.upper()

        # Removes digits from the sequence
        sequence = ''.join([i for i in sequence if not i.isdigit()])

        # A list of the sequence, to be reformatted
        sequenceList = []

        # Sequence is fixed again, removing spaces
        sequence = sequence.replace(" ", "")
        sequence = sequence.replace("\n", "")
        sequence = sequence.replace("\t","")

        for i in range(0, len(sequence), width):
            sequenceList.append(sequence[i:i+width])
        sequence = '\n'.join(sequenceList)
        sequence = '\n' + sequence

        # The def formatSeq that takes a sequence and a width and
        # formats code to user specifications
        def formatSeq(sequence, width):
            sequenceList = []
            
            
            for i in range(0, len(sequence), width):
                sequenceList.append(sequence[i:i+width])
            sequence = '\n'.join(sequenceList)
            sequence = '\n' + sequence
            
            return sequence


        # Call the function
        formatSeq(sequence, width)

        # Write the outputLines into the output file
        fileOut.write(outputLines)

        # Write the sequence into the output file
        fileOut.write(sequence)

        # Close the input file
        fileIn.close()

        # Close the output file
        fileOut.close()


    if __name__ == '__main__':
        main()
        

