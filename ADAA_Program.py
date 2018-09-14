#NP_project.py
#Source code for the Subset Sum Problem
#This program is a proof of concept that uses dynamic programming to find a soulution to the Subset Sum Program in psuedo polynomial time
#February 24 2018, Grant Kalfus, Nathaniel Maciejewski, Andrew Miller 
import numpy as np
import random
import time

def subset_sum(random_list, LIST_SIZE, random_val):
    #This 2-D array is a means to dynamically store what possible sums can be computed with elements in the set.
    #When a sum is found to be possible, the element will be set to true
    #The array has n rows and m columns, where n is the length of the random set and m is the random value we are trying to sum to
    data_keeper = np.zeros((LIST_SIZE, random_val+1), dtype = bool)


    #This check will quit the program if the sum overruns the max possible sum within the subset to improve the worst case
    if (random_val > np.sum(random_list)):
        print("Sum is too high to possibly be computed from elements in the set returning to loop...")
        return;

    #initializes the first columnn to true. This is necessary for how the algortithm checks sums using numbers within the set
    for i in range(0, LIST_SIZE):
        data_keeper[i][0] = True





    #This loop sets the first row of the data keeper matrix elements to true.
    for i in range (0, LIST_SIZE):
        if (random_val >= random_list[i]):#Check to make sure array is not overrun
            data_keeper[0][random_list[i]] = True #This statement sets all numbers found within the set to true on the 0th row of the data_keeper array


    #This next loop should iterate through the rest of the data keeper matrix. It will set any entry to true if it is possible to form that sum given our set of numbers.
    for i in range (1, LIST_SIZE):
        #print("starting row " + str(i))
        for x in range (1, random_val+1):
            if (data_keeper[i-1][x] == True): #Condition 1 for whether the sum can be calculated with the current number set: if the value in the column above is true, then the current value is also true
                data_keeper[i][x] = True
            if (x - random_list[i] >= 0): #Needs to be checked to make sure the bounds of the matrix is overrun
                if(data_keeper[i-1][x-random_list[i]] == True): #Condition 2 for whether the sum can be calculated with the current number set: if the value in the column above shifted left by the corresponding indexed value in the sorted random list is true, the sum can be caluclated, so the current value is true
                    data_keeper[i][x] = True




    sum = False #A boolean to print whether or not the sum can be computed using a subset

    #This loop iterates through the data_keeper array to determine if the sum is found
    #Only the last column is of any interest because that is the column that corresponds to the sum we are checking
    for i in range(0, LIST_SIZE):
            if (data_keeper[i][random_val] == True): #If any row of the last column is found to be true, we automatically know the sum can be sound within the number set, so we set sum to true
                sum = True
                break


def Writecsv(myList1, myList2): #A function to write lists to a csv file
    dataFile = open("list.csv", "w+")
    for i in range (0, 1000): #Iterates through list writing both the runtime and n value in coumns
        dataFile.write("%s," % myList1[i])
        dataFile.write("%s,\n" % myList2[i])
    dataFile.close()


listsizes = []
runtimes = []

for y in range (0, 1000):
    listsizes.append(y)
    LIST_SIZE = 50
    LIST_BOUNDS = 1000
    print("Currently on LIST_SIZE = " + str(y))
    #Generate a LIST_SIZE large list of sorted random numbers from 0 to LIST_BOUNDS
    random_list = np.sort(np.random.randint(0,LIST_BOUNDS,LIST_SIZE))
    
    #this is the value that we are looking for
    random_val = random.randint(0, y * np.random.randint(0, 10))

    begin = time.clock()
    subset_sum(random_list,LIST_SIZE, random_val)
    end = time.clock()
    runtime = end - begin
    runtimes.append(runtime)

Writecsv(listsizes, runtimes)