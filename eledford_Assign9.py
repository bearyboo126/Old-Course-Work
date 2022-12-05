#!/usr/bin/python3
# Name: Erin Ledford
# Class: BIOI 3500, Spring 2021
# Assignment #: Assignment 9
# Due Date: April 9th, 2021
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
# This program finds the genes given by the input gene symbols and returns the# genes and their information in a tab-delimited format. 

import sys
import getopt
import psycopg2

class eledford_Assign9:
    def main():

        # The line of the file that is being searched
        searchLine = ''

        # The final output RNA that is written out to the output file
        outputRNAFinal = ''

        # The final output protein that is written out to the output file
        outputProtFinal = ''

        # The final output pubmed that is written out to the output file
        outputPubFinal = ''

        # The connection to the pubmed database
        conn = psycopg2.connect(database = "pubmed")

        # The cursor that executes SQL queries
        cursor = conn.cursor()

        
        # Read in command-line arguments into the opts list
        try:
            opts, args = getopt.getopt(sys.argv[1:], "i:o:")

        except getopt.GetoptError as err:

            # Redirect STDERR to STDOUT (insures screen display)
            sys.stdout = sys.stderr

            # Print help information
            print(str(err))

            # Print usage information; usage is the name of a 
            # function (declared elsewhere) that displays the usage
            # information (just a series of print statements)
            usage()

            # Exit the program
            sys.exit(2)

        # Reads the input file from the command line or prints to terminal
        fileIn = sys.stdin

        # Reads the output file from the command line or prints to terminal
        fileOut = sys.stdout

        # Processes the opt and arg lists displaying the argument
        # for each option
        for (opt, arg) in opts:

            # If opt is given, changes input file to arg
            if (opt == "-i"):
                fileIn = open(arg, 'r')

            # If opt is given, changes output file to arg
            if (opt == "-o"):
                fileOut = open(arg, 'w')


        # Executes queries line by line from the input file
        for line in fileIn:

            # Strips each line of the \n so it can be used for SQL queries
            searchLine = line.strip('\n')
            
            # Executes an SQL query that finds the gene symbol, taxonomy ID,
            # and the gene ID of the search line from the input file
            cursor.execute("SELECT DISTINCT symbol,  tax_id,  gene_id FROM geneinfo WHERE symbol= '" + searchLine + "' ORDER  BY tax_id ASC;")
            
            # The resulting data gathered from the database
            result = cursor.fetchall()
            
            # Executes an SQL query that finds the RNA nucleotide accession
            # number(s) of the search line from the input file
            cursor.execute("SELECT DISTINCT gene2refseq.RNA_nucleotide_accession FROM gene2refseq, geneinfo WHERE geneinfo.symbol = '"+ searchLine + "' AND geneinfo.gene_id = gene2refseq.geneID ORDER BY gene2refseq.RNA_nucleotide_accession ASC;")

            # The resulting RNA nucleotide accession data gathered 
            # from the database
            resultRNA = cursor.fetchall()
            
            # Executes an SQL query that finds the protein accession 
            # number(s) of the search line from the input file
            cursor.execute("SELECT DISTINCT gene2refseq.protein_accession FROM gene2refseq, geneinfo WHERE geneinfo.symbol = '" + searchLine + "' AND geneinfo.gene_id = gene2refseq.geneID ORDER BY gene2refseq.protein_accession ASC;")
            
            # The resulting protein accession number(s) gathered from
            # the database
            resultProt = cursor.fetchall()
            
            # Executes an SQL query that finds the pubmed ID(s) of the 
            # search line from the input file
            cursor.execute("SELECT DISTINCT gene2pubmed.pubmed_id FROM geneinfo, gene2pubmed WHERE geneinfo.symbol = '" + searchLine + "' AND geneinfo.gene_id = gene2pubmed.gene_id ORDER BY gene2pubmed.pubmed_id ASC;")
            
            # The resulting pubmed ID(s) gathered from the database
            resultPub = cursor.fetchall()

            # Formats the output of the gene ID, taxonomy ID, and gene symbol
            for row in result:
                output = '\t'.join(str(x) for x in row)
                fileOut.write(output)

            fileOut.write('\t')
            
            # Formats the output of the RNA nucleotide accession number(s)
            for rowRNA in resultRNA:
                outputRNA = ' '.join(str(x) for x in rowRNA)
                outputRNA = outputRNA.replace('None', '')
                outputRNa = outputRNA.replace("NULL", '-')
                if outputRNA != '-' and outputRNA != '':
                    outputRNAFinal += outputRNA + '|'
                else:
                    outputRNAFinal += outputRNA
            if (outputRNAFinal.endswith('|')):
                outputRNAFinal = outputRNAFinal[:-1]

            fileOut.write(outputRNAFinal)
            fileOut.write('\t')
            
            # Formats the output of the protein accession number(s)
            if resultProt[0][0]:
                for rowProt in resultProt:
                    outputProt = ''.join(str(x) for x in rowProt)
                    if (outputProt != 'None'):
                        outputProtFinal += outputProt + '|'
                if (outputProtFinal.endswith('|')):
                    outputProtFinal = outputProtFinal[:-1]
                fileOut.write(outputProtFinal)
            else:
                    fileOut.write('-')

            fileOut.write('\t')
            
            # Format the output of the pubmed ID(s)
            for rowPub in resultPub:
                outputPub = ''.join(str(x) for x in rowPub)
                outputPub = outputPub.replace('None', '')
                outputPub = outputPub.replace('NULL', '-')
                if (outputPub != '' and outputPub != '-'):
                        outputPubFinal += outputPub + '|'
            if (outputPubFinal.endswith('|')):
                outputPubFinal = outputPubFinal[:-1]
            fileOut.write(outputPubFinal)
            fileOut.write('\n')
            
        # Closes the cursor
        cursor.close()

        # Closes the connection
        conn.close()

        # Closes the input file
        fileIn.close()

        # Closes the output file
        fileOut.close()
    if __name__ == '__main__':
        main()
