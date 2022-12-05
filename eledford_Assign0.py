#!/usr/bin/python3
# Name: Erin Ledford
# Class: BIOI 3500, Spring 2021
# Assignment #: Assignment 0
# Due date: January 29th, 2021
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
# This program prompts the user to enter the distance a package is to be
# shipped and the weight of the package. It then calculates and displays
# the shipping charges for that package.

class eledford_Assign0:
    def main():

        # Variable for user input (miles)
        miles = 0

        # Variable for user input (weight)
        weight = 0

        # Variable for rate per 100 miles
        rate = 0

        # Variable for calculating shipping costs
        distanceUnits = 0

        # Prints welcome message
        print("Welcome to the You Package It We Savage It Shipping Company.")

        # Prompts user for an integer between 0 and 60 for weight
        while int(weight) <= 0 or int(weight) >= 60:
            weight = input(["How heavy is your package in pounds (1-60)? "])
            weight = int(weight)

        # Prompts user for an integer greater than 0 for miles
        while int(miles) <= 0:
            miles = input(["How far will you be shipping the package in miles? "])
            miles = int(miles)

        # Finds shipping rate per 100 miles based on weight
        if weight <= 10:
            rate = 5.01
        elif weight <= 20:
            rate = 7.02
        elif weight <= 30:
            rate = 9.03
        elif weight <= 40:
            rate = 11.04
        else:
            rate = 13.05

        # Calculates number to multiply by rate for total cost
        distanceUnits = miles / 100
        if miles % 100 != 0:
            distanceUnits = distanceUnits + 1

        # Prints total shipping cost
        print("Your total shipping cost for " + str(miles) + " miles is $"
                + str(rate * distanceUnits))

    if __name__ == '__main__':
        main()

