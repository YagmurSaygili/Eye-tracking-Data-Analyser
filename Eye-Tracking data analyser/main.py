#Author: Yağmur Saygılı & İlyas Coşkun
#Version: 1.8

import sys
from re import *
from copy import deepcopy
import matplotlib.pyplot as plt

# Function for comparing total number of datas for the whole image. Autism vs NotAutism People
def totalCompare(letters,segment_dict):
    #Inıtializing sum values of datas seperately
    sum_of_total_time_viewed_ASD = 0
    sum_of_total_no_of_people_ASD = 0
    sum_of_total_no_of_fixations_ASD = 0

    sum_of_total_time_viewed_CONTROL = 0
    sum_of_total_no_of_people_CONTROL = 0
    sum_of_total_no_of_fixations_CONTROL = 0

    #Calculating the sums by adding the datas in segments one by one going through every segment in the image by looping
    for record in segment_dict:
      sum_of_total_time_viewed_ASD += segment_dict[record]["ASD"]["Total time viewed"]
      sum_of_total_no_of_people_ASD += segment_dict[record]["ASD"]["Total number of people"]
      sum_of_total_no_of_fixations_ASD += segment_dict[record]["ASD"]["Total number of fixations"]

      sum_of_total_time_viewed_CONTROL += segment_dict[record]["CONTROL"]["Total time viewed"]
      sum_of_total_no_of_people_CONTROL += segment_dict[record]["CONTROL"]["Total number of people"]
      sum_of_total_no_of_fixations_CONTROL += segment_dict[record]["CONTROL"]["Total number of fixations"]

    #Getting type input from user to decide which type of data want to be displayed
    typeOfView = int(input("Enter the type that you want to display\nFor Total Time Viewed: 1\nFor Total Number of Fixations: 2\nFor Total Number of people: 3\nEnter your choice:"))

    match typeOfView:
        #Total time viewed for an image is displayed
                case 1:
                    groups = ["People with Autism", "People Without Autism"]
                    values = [sum_of_total_time_viewed_ASD,sum_of_total_time_viewed_CONTROL]
                    plt.bar(groups, values)
                    plt.xlabel('Groups')
                    plt.ylabel('Total time viewed')
                    plt.title('Comparison Between People With & Without Autism for Image ')
                    plt.show()
        #Total no of fix for an image is displayed
                case 2:
                    groups = ["People with Autism", "People Without Autism"]
                    values = [sum_of_total_no_of_fixations_ASD,sum_of_total_no_of_fixations_CONTROL]
                    plt.bar(groups, values)
                    plt.xlabel('Groups')
                    plt.ylabel('Total Number Of Fixations')
                    plt.title('Comparison Between People With & Without Autism for Image')
                    plt.show()
        #Total no of people for an image is displayed
                case 3:
                    groups = ["People with Autism", "People Without Autism"]
                    values = [sum_of_total_no_of_people_ASD,sum_of_total_no_of_people_CONTROL]
                    plt.bar(groups, values)
                    plt.xlabel('Groups')
                    plt.ylabel('Total number of people')
                    plt.title('Comparison Between People With & Without Autism for Image')
                    plt.show()

#Function for comparing datas for each image segments. Autism vs NoAutism
def compareDataPeople(letters,segments_dict):
    # Getting inputs from user for which segment and which type of view they want to display
    segment = input("Please enter the segment that you want to display (A B C D ...): ")
    typeOfView = int(input("Enter the type that you want to display\nFor Total Time Viewed: 1\nFor Total Number of Fixations: 2\nFor Total Number of people: 3\nEnter your choice:"))
    #Looping through letters list to catch the segment that user want to be displayed
    for item in letters:
        if segment == item:
            match typeOfView:
                case 1:
                    groups = ["People with Autism", "People Without Autism"]
                    values = [segments_dict[segment]["ASD"]["Total time viewed"], segments_dict[segment]["CONTROL"]["Total time viewed"]]
                    plt.bar(groups, values)
                    plt.xlabel('Groups')
                    plt.ylabel('Total time viewed')
                    plt.title('Comparison Between People With & Without Autism for Element ' + str(segment))
                    plt.show()
                case 2:
                    groups = ["People with Autism", "People Without Autism"]
                    values = [segments_dict[segment]["ASD"]["Total number of fixations"], segments_dict[segment]["CONTROL"]["Total number of fixations"]]
                    plt.bar(groups, values)
                    plt.xlabel('Groups')
                    plt.ylabel('Total Number Of Fixations')
                    plt.title('Comparison Between People With & Without Autism for Element ' + str(segment))
                    plt.show()
                case 3:
                    groups = ["People with Autism", "People Without Autism"]
                    values = [segments_dict[segment]["ASD"]["Total number of people"], segments_dict[segment]["CONTROL"]["Total number of people"]]
                    plt.bar(groups, values)
                    plt.xlabel('Groups')
                    plt.ylabel('Total number of people')
                    plt.title('Comparison Between People With & Without Autism for Element ' + str(segment))
                    plt.show()


# Basic menu function for operating basic operations
def menu(option,letters,segment_dict):
    match option:
        case 1:
            compareDataPeople(letters,segment_dict)
        case 2:
            totalCompare(letters,segment_dict)
        case 3:
            exit(0)


# Function for analyzing the files and assigning values into the dictionaries # fixations, # people, #duration for each segment
def analyze_data(PeopleRecord, filename, lettercounter):
    people_id_counter = 0
    people_list = []
    added_people = []

    for record in PeopleRecord:
        fields = record.split(",")
        if fields[0] == '0':  # If fixation id which is fields[0] is 0 it means a new person in record
            people_id_counter += 1  # To check if the people with the given ID exists in the segment
            people_list.append(people_id_counter) # To record the id of people which look at the segment initially

        # Calculating the places to put fixations
        # If the given condition is satisfied, which means the fixation in the corresponding segment, save the data in the dictionaries
        if (width <= int(fields[1]) <= ((row + 1) * grid_x)) \
                and (height <= int(fields[2]) <= ((column + 1) * grid_y)):
            segments_dict[segments[letter_counter]][filename]["Total number of fixations"] += 1
            segments_dict[segments[letter_counter]][filename]["Total time viewed"] += int(fields[3])
            # If statement to check if the person in operation is included in the segment (total no of people) or not
            if people_list.count(people_id_counter) == 1 and added_people.count(people_id_counter) == 0:
                segments_dict[segments[letter_counter]][filename]["Total number of people"] += 1
                added_people.append(people_id_counter)

#Getting file names and grid size and image size from user via command line
people_with_autism_file = sys.argv[1]
people_without_autism_file = sys.argv[2]
image_size_name = sys.argv[3]
grid_size_name = sys.argv[4]

#Seperating image size with findall according to x and y, REGULAR EXPRESSION
image_size = findall("\d+", image_size_name)

# Grid size is stored in 2 element list
grid_size = findall("\d+", grid_size_name)

grid_x = int(image_size[0]) / int(grid_size[1])  # The multiple of x_axis
grid_y = int(image_size[1]) / int(grid_size[0])  # The multiple of y_axis

# Getting how many segment in the grid by simply multiplying grid rows and columns
elementsize = int(grid_size[0]) * int(grid_size[1])

try:
    people_without_autism = open(people_without_autism_file, "r")
    people_with_autism = open(people_with_autism_file, "r")
except IOError:
    print("Files could not be opened")
    exit(1)

next(people_with_autism)  # To skip the first line where unnecessary info is given ASD
next(people_without_autism)  # To skip the first line where unnecessary info is given in Control
AutismPeopleRecord = people_with_autism.readlines() # All the lines in the file stored in AutismPeopleRecord variable
NoAutismPeopleRecord = people_without_autism.readlines()# All the lines in the file stored in NoAutismPeopleRecord variable

# The dictionary where total # people , # time viewed and # fixations are kept
record_dictionary = {}
record_dictionary["Total number of people"] = 0
record_dictionary["Total time viewed"] = 0
record_dictionary["Total number of fixations"] = 0

# Creation of file name dictionary
filename_dictionary = {}
filename_dictionary["ASD"] = deepcopy(record_dictionary)
filename_dictionary["CONTROL"] = deepcopy(record_dictionary)
segments = []# The list which holds the segments inside
letter_ascii = 65 # Ascii number of letters
segments_dict = {} # Outer dictionary the main one which holds whole the data inside as nested

# Creating elements for grid
for letter in range(int(elementsize)):
    segments.append(chr(letter_ascii))

    segments_dict[chr(letter_ascii)] = deepcopy(filename_dictionary)
    letter_ascii += 1 # Updating the letter by increasing ascii value one, see the ascii table

letter_counter = 0  # A : 0 ,B : 1 , C : 2 .....

for column in range(int(grid_size[0])):  # Counts y points in the grid , like --> l0*300, 1*300, 2*300
    height = column * grid_y  #
    for row in range(int(grid_size[1])):  # Counts x points in the grid : like --> 0*600, 1* 600, 2*600 gibi
        width = row * grid_x

        analyze_data(AutismPeopleRecord, "ASD", letter_counter) # Calls the function for fill the data in dictionary for people have autism

        analyze_data(NoAutismPeopleRecord, "CONTROL", letter_counter) # Calls the function for fill the data in dictionary for people dont have autism

        letter_counter += 1  # Determines which letter are we searching

option = 0

while option != 3:
    print("1. Compare the total number of people, the total time viewed, and the total number of fixations for people with and without autism for a particular element on an image")
    print("2. Compare the total number of people, the total time viewed, and the total number of fixations for people with and without autism on an image")
    print("3. Exit")
    option = int(input("\nEnter your choice to operate: "))
    if option!= 1 and option != 2 and option !=3:
        print("Please enter a valid number (1-2-3) !!!")
    else:
        menu(option, segments, segments_dict)

