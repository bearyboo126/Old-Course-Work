#!/usr/bin/python3
# Name: Erin Ledford
# Class: BIOI 3500, Spring 2021
# Assignment #: Assignment 11
# Due Date: April 30th, 2021
#
# Honor Pledge: On my honor as a student of the Unviersity of Nebraska at
#               Omaha, I have neither given nor received unauthorized help on
#               this programming assignment.
#
# NAME: Erin Ledford
# EMAIL: eledford@unomaha.edu
#
# Partners: NONE
#
# This programming assignment uses Biopython that parses the provided BLAST
# output and outputs the Uniprot ID, the PDB ID of the hit, and the secore,
# percentage identity, and coverage of the best HSP for each query.

import sys
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio.Blast import NCBIXML

class eledford_Assign11:
    def main():
        
        # The input file
        fileIn = open('multiQueryOutput.xml')
        
        # Opening the file to do XML parsing
        blastRecord = NCBIXML.parse(fileIn)

        # The file where the output is recorded
        fileOut = open('eledford_results.txt', 'w')
        
        # Parses the blastRecords using NCBIXML
        for blastRecord in NCBIXML.parse(fileIn):

            # Parses the alignments in the blastRecord
            for alignment in blastRecord.alignments:

                # Grabs the Uniprot ID
                UniprotID = blastRecord.query
                UniprotID = UniprotID.split("|")
                UniprotID = UniprotID[1]

                # Parses the hsps in the alignment
                for hsp in alignment.hsps:
                    
                    # Grabs the PDB ID
                    PDBID = alignment.hit_def
                    PDBID = PDBID.split("_")
                    PDBID = PDBID[0]
                    
                    # Grabs the hsp score
                    hspScore = hsp.score
                    
                    # Finds the percentage identity of the hsp
                    percentageIdentity = hsp.identities / hsp.align_length
                    percentageIdentity = "%.3f" % (percentageIdentity)
                    
                    # Where the hsp aligns with the query sequence
                    # in the beginning
                    startCoverage = hsp.query_start

                    # Where the hsp aligns with the query sequence at the end
                    endCoverage = hsp.query_end
                    
                    # The coverage of the HSP and its formatting
                    coverage = (endCoverage - startCoverage + 1) / blastRecord.query_length
                    coverage = round(coverage, 3)
                    coverage = "%.3f" % (coverage)

                    # Writes out the Uniprot ID, the PDB ID, hsp score,
                    # percentage identity, and coverage to the file
                    fileOut.write(UniprotID)
                    fileOut.write("\t")
                    fileOut.write(PDBID)
                    fileOut.write("\t")
                    fileOut.write(str(hspScore))
                    fileOut.write("\t")
                    fileOut.write(str(percentageIdentity))
                    fileOut.write("\t")
                    fileOut.write(str(coverage))
                    fileOut.write("\n")
        
        # Closes the input file
        fileIn.close()

        # Closes the output file
        fileOut.close()

    if __name__ == '__main__':
        main()


