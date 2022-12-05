#!/usr/bin/python3
# Name: Erin Ledford
# Class: BIOI 3500, Spring 2021
# Assignment #: Assignment 1
# Due date: January 29th, 2021
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
# This program prompts the user for a DNA sequence. It then calculates and
# displays the GC-content of the DNA fragment and its reverse complement.

class eledford_Assign1:
    def main():

        # List for DNA sequence fragment given by the user
        sequenceList = []

        # The GC-content of the DNA sequence fragment
        GC = 0

        # Counts the number of As in the DNA sequence fragment
        counterA = 0

        # Counts the number of Ts in the DNA sequence fragment
        counterT = 0

        # Counts the number of Gs in the DNA sequence fragment
        counterG = 0

        # Counts the number of Cs in the DNA sequence fragment
        counterC = 0
        
        # Prompts the user to enter a DNA sequence fragment
        sequenceList = input(["Enter a sequence:  "])

        # Makes sure that the input given by the user is all in upper case
        sequenceListUp = sequenceList.upper()

        # Counts the number of As, Ts, Gs, and Cs in the sequence fragment,
        # if it is not A, T, G, or C it replaces the letter with X
        for x in sequenceListUp:
            if str(x) == "A":
                counterA += 1
            elif str(x) == "T":
                counterT += 1
            elif str(x) == "G":
                counterG += 1
            elif str(x) == "C":
                counterC += 1
            else:
              sequenceListUp = sequenceListUp.replace(x, "X")
        
        # Figures out the GC content within the DNA sequence fragment
        GC = ((counterG + counterC)
        / (counterA + counterT + counterG + counterC)) * 100

        # Prints the GC content of the DNA sequence fragment
        print("%GC content:  " + str(GC) + "%")

        # Replaces A with t, T with a, G with c, and C with g to get the
        # complement of the DNA sequence fragment
        complement = sequenceListUp.replace("A","t")
        complement = complement.replace("T","a")
        complement = complement.replace("G","c")
        complement = complement.replace("C","g")
        complement = complement.upper()

        # Prints the complement out for the user to see
        print("Complement:  " + complement)

        # Iterates backwards through the complement to get the reverse
        reverseComplement = complement[::-1]

        # Prints the reverse complement for the user to see
        print("Reverse complement:  " + reverseComplement)


    if __name__ == '__main__':
        main()
