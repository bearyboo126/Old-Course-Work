#!/usr/bin/python3
# Name: Erin Ledford
# Class: BIOI 3500, Spring 2021
# Assignment #: Assignment 7
# Due Date: March 19th, 2021
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
# This program takes a Uniprot FASTA file and outputs the Uniprot ID, the positions of the match, and the piece of the sequence that matches the REGEX.

import re
import sys
import getopt

class eledford_Assign7:

    def main():

        # Read in the command line arguments into the opts list
        try:
            opts, args = getopt.getopt(sys.argv[1:], "i:o:e:")
        
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

        # Reads the input from the keyboard
        fileIn = sys.stdin

        # Reads the output to the screen
        fileOut = sys.stdout

        # The motif that is being searched for if user does not give input
        motif = re.compile("C\w\wC\w{12}H\w{3}H")

        # A list of locations of matches
        location =[]
        
        # The group of letters found in the match
        g = ""

        # The uniprot-ID of the sequence
        seqID = ""

        # The lines of the file that correspond to where the match is found
        seq = ""

        # A boolean used to find a match
        firstSeq = True

        # A starting index of where the match is found where the index is a
        # one based index
        match_i = 1

        # An end index of where the match is found, where the index is a
        # one based index
        match_e = 1

        # Processes the opt and arg lists displaying the argument
        # for each option
        for (opt, arg) in opts:

            # If opt is given, fileIn is changed to arg
            if (opt == "-i"):
                fileIn = open(arg, 'r')

            # If opt is given, fileOut is changed to arg
            if (opt == "-o"):
                fileOut = open(arg, 'w')

            # If opt is given, motif is changed to arg
            if (opt == "-e"):
                motif = re.compile(str(arg))

        # Finds the matches of user input or original motif in the file
        for line in fileIn:

            # If the line starts with a > it is in the right spot to start a
            # search
            if line[0] == ">":
                if not firstSeq:
                    
                    # Searches for the motif in the seq
                    m = re.search(motif, seq)

                    # If there is a match, write said match and its location
                    # out to the output file
                    if m:
                        g = seq[m.start():m.end()]
                        match_i = (m.start() + 1)
                        match_e = (m.end() + 1)
                        seqID = line[1:].split("|")[1]
                        header = True
                        fileOut.writelines(seqID)
                        fileOut.writelines("\t")
                        fileOut.writelines(str(match_i))
                        fileOut.writelines("\t")
                        fileOut.writelines(str(match_e))
                        fileOut.writelines("\t")
                        fileOut.writelines(str(g))
                        fileOut.writelines("\n")
                        seq = ""
                firstSeq = False

            # If there is no > then it skips that line and searches the next
            # one
            else:
                seq += line[:-1]

        # Closes the input file
        fileIn.close()

        # Closes the output file
        fileOut.close()

    if __name__ == '__main__':
        main()
