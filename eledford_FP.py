#!/usr/bin/python3
# Name: Erin Ledford
# Class: BIOI 3500, Spring 2021
# Assignment #: Final Project
# Due Date: May 7th, 2021
#
# Honor Pledge: On my honor as a student of the University of Nebraska at
#               Omaha, I have neither given nor received unauthorized help on
#               this programming assignment.
#
# NAME: Erin Ledford
# EMAIL: eledford@unomaha.edu
#
# Partners: NONE
#
# This programming assignment reads in a FASTA file containing one or more
# sequences (either DNA or protein sequences), performs a BLAST search
# (either locally or remotely using the NCBI web server via Biopython)
# for each sequence, and prints out the results of the search.

import re
import sys
import getopt
import os
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio.Blast import NCBIXML
from Bio.Blast import NCBIWWW
from Bio.Blast.Applications import NcbiblastpCommandline
from Bio.Blast.Applications import NcbiblastnCommandline

class eledford_FP:

    def main():

        # Read in the command line arguments into the opts list
        try:
            opts, args = getopt.getopt(sys.argv[1:], "i:o:d:e:l:n:")

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
            
        # The database to be used for a blast search
        database = ""

        # The e-value used for the blast search
        eV = 0.001

        # The value used to decide if local or online blast search
        localOrOnline = 2

        # The value used to decide the maximum number of results shown
        maxRes = 0

        # Processes the opt and arg lists displaying the argument
        # for each option
        for (opt, arg) in opts:

            # Specifies the name of the file containing the input
            # sequence(s)
            if (opt == '-i'):
                fileIn = arg
                    
            # Specifies the name of the output file. If this option
            # is not used, output should be sent to standard output
            # (i.e., the screen)
            if (opt == '-o'):
                fileOut = open(arg, 'w')

            # Specifies the name of the database to search against
            if (opt == '-d'):
                database = arg

            # Specifies the e-value cutoff of the blast search
            if (opt == '-e'):
                eV = float(arg)

            # Specifies whether BLAST should be run locally (0 option)
            # or through the NCBI web server (1 option)
            if (opt == '-l'):
                localOrOnline = int(arg)
            # Specifies the maximum number of results to show for each
            # query sequence
            if (opt == '-n'):
                maxRes = int(arg)



        # A function that figures out whether or not the sequences entered 
        # are protein or DNA sequences
        def protOrDNA (fileIn):
            # All of the records in the file
            allRecords = ""

            # The re to use as a search
            alphabet = re.compile('^[acgt]*$', re.I)

            # Opens the file and allows for parsing
            validationForSeq = SeqIO.parse(fileIn, 'fasta')
            # Parses the file and grabs all sequences
            for record in validationForSeq:
                allRecords += record.seq
            # If the sequences are DNA, validSeq returns true,
            # otherwise it is a protein sequence
            if alphabet.search(str(allRecords)) is not None:
                validSeq = True
            else:
                validSeq = False
            return validSeq

        # The function that figures out where to go if it is a protein or DNA
        # and if it is either running locally or online
        def whereToGo(validSeq):

            if (validSeq == False and localOrOnline == 0):
                blastKind = "Prot local"
            if(validSeq == False and localOrOnline == 1):
                blastKind = "Prot online"
            if (validSeq == True and localOrOnline == 0):
                blastKind = "Nucleotide local"
            if (validSeq == True and localOrOnline == 1):
                blastKind = "Nucleotide online"
            return blastKind
        
        # The function that runs the blast of the file locally
        def blastLocal():

            count = 1

            # If the sequences are protein sequences it runs blastp
            if (blastKind == "Prot local"):
                blastCommand = NcbiblastpCommandline(query = fileIn, 
                        db = database, evalue = eV, outfmt = 5, 
                        out = 'intermediate_Results.xml')
                stdout, stderr = blastCommand()
                fileIntermediateOut = open('intermediate_Results.xml')
                blastRecord = NCBIXML.parse(fileIntermediateOut)

            # If the sequences are DNA sequences it runs blastn
            if (blastKind == "Nucleotide local"):
                blastCommand = NcbiblastnCommandline(query = fileIn, 
                        db = database, evalue = eV, outfmt = 5, 
                        out = 'intermediate_Results.xml')
                stdout, stderr = blastCommand()
                fileIntermediateOut = open('intermediate_Results.xml')
                blastRecord = NCBIXML.parse(fileIntermediateOut)

            # Makes sure that no prot online or prot local makes its way
            # into this function
            if (blastKind == "Prot local" or blastKind == "Nucleotide local"):
                
                # Parses through the intermediate file for the hsps, percent
                # identity, coverage, hit def, and header of the query
                # and writes them out to fileOut
                for blastRecord in NCBIXML.parse(fileIntermediateOut):
                    header_of_query = blastRecord.query
                    count = 1
                    fileOut.write(header_of_query)
                    for alignment in blastRecord.alignments:
                        for hsp in alignment.hsps:
                            header_of_query =  blastRecord.query
                            definition_of_hit = alignment.hit_def
                            definition_of_hit = str(count) + ". " + definition_of_hit[0:maxRes] + "..."
                            identity = hsp.identities / hsp.align_length
                            identity = "%.3f" % (identity)
                            coverage = (hsp.query_end - hsp.query_start + 1) / blastRecord.query_length
                            coverage = round(coverage, 3)
                            coverage = "%.3f" % (coverage)
                            count += 1
                            fileOut.write("\n")
                            fileOut.write(definition_of_hit)
                            fileOut.write("\t")
                            fileOut.write(str(identity))
                            fileOut.write("\t")
                            fileOut.write(str(coverage))
                            fileOut.write("\n")          
        
        # The function that blasts the input file online
        def blastOnline():
            # Keeps track of the hits
            count = 1

            # if the file contains protein sequences the blastType is blastp
            if (blastKind == "Prot online"):
                blastType = "blastp"

            # if the file contains DNA sequences the blastType is blastn
            if (blastKind == "Nucleotide online"):
                blastType = "blastn"
            # Makes sure to only look at the correct types and makes sure
            # no local files run
            if (blastKind == "Prot online" or blastKind == "Nucleotide online"):
                # Opens the fileIn to be used in the blast search
                fastaString = open(fileIn).read()
                # Blasts the fileIn
                resultHandle = NCBIWWW.qblast(blastType, database, fastaString)
                # Writes the blast results to an XML file
                blast_result = open("intermediate_Results.xml", 'w')
                blast_result.write(resultHandle.read())
                blastRecord = NCBIXML.parse(blast_result)

                # Parses the blast results to search for hsps, hit def,
                # header of the query, percent identity, and coverage
                # and writes them into fileOut
                for blastRecord in NCBIXML.parse(blast_result):
                    header_of_query = blastRecord.query
                    count = 1
                    for alignment in blastRecord.alignments:
                        for hsp in alignment.hsps:
                            definition_of_hit = alignment.hit_def
                            definition_of_hit = str(count) + ". " + definition_of_hit[0:maxRes] + "..."
                            identity = hsp.identities / hsp.align_length
                            identity = "%.3f" % identity
                            coverage = (hsp.query_end - hsp.query_start + 1) / blastRecord.query_length
                            coverage = round(coverage, 3)
                            coverage = "%.3f" % coverage
                            count += 1
                            fileOut.write(header_of_query)
                            fileOut.write("\n")
                            fileOut.write(definition_of_hit)
                            fileOut.write("\t")
                            fileOut.write(identity)
                            fileOut.write("\t")
                            fileOut.write(coverage)
                            fileOut.write("\n")
                
                # Closes the blast_result file
                blast_result.close()


        # The main function calls and stores the result from the protOrDNA
        # function
        validSeq = protOrDNA(fileIn)

        # The main function calls and stores the result from the whereToGo
        # function
        blastKind = whereToGo(validSeq)

        # Calls the blastLocal function
        blastLocal()

        # Calls the blastOnline function
        blastOnline()

        # Deletes the intermediate files if they exist
        if os.path.exists("intermediate_Results.xml"):
            os.remove("intermediate_Results.xml")

        # Closes the out file
        fileOut.close()

    if __name__ == '__main__':
        main()

