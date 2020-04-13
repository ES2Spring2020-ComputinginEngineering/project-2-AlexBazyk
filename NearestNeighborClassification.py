#Please put your code for Step 2 and Step 3 in this file.
# Alex Bazyk


import numpy as np
import matplotlib.pyplot as plt
import random


# FUNCTIONS

#takes no parameters. returns glucose, hemo, class numpy arrays based on 
# the the data stored in the file.
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

#normalizes the data of glucose, hemo, class numpy arrays as a value from 0-1.
#does this through an equation
#returns the new normalized data in numpy arrays
def normalizeData(glucose, hemoglobin, classification):
    g_max = np.amax(glucose)
    g_min = np.amin(glucose)
    h_max = np.amax(hemoglobin)
    h_min = np.amin(hemoglobin)
    c_max = np.amax(classification)
    c_min = np.amin(classification)
    for i in range(len(glucose)):
        normalized = (glucose[i]-g_min)/(g_max-g_min)
        glucose[i] = normalized
    for h in range(len(hemoglobin)):
        normalized = (hemoglobin[h]-h_min)/(h_max-h_min)
        hemoglobin[h] = normalized
    for j in range(len(glucose)):
        normalized = (classification[j]-c_min)/(c_max-c_min)
        classification[j] = normalized
    return glucose , hemoglobin, classification

#graphs the data stored in the glucose, hemoglobin, classification numpy arrays
#returns nothing but prints out the graph
def graphData(glucose,hemoglobin,classification):
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.title("Glucose vs. Hemoglobin")
    plt.legend()
    plt.show()

#Parameters: glucose and hemoglobin numpy arrays not normalized
#Creates test points by creating random numbers between 0 and 1 which is 
#the bounds for the normalized data
#Also creates variables using min and max and the random numbers which are 
#values that are those random numbers scaled to the non normalized data
#Returns all 4 of those numbers just in case either of them are ever needed.
def createTestCase(glucose,hemoglobin):
    g_max = np.amax(glucose)
    g_min = np.amin(glucose)
    h_min = np.amin(hemoglobin)
    h_max = np.amax(hemoglobin)
    newglucose = np.random.rand(1)
    normg = newglucose
    newglucose = np.multiply(newglucose,g_max-g_min)
    newglucose = np.add(newglucose,g_min)
    newhemoglobin = np.random.rand(1)
    normh = newhemoglobin
    newhemoglobin = np.multiply(newhemoglobin,h_max-h_min)
    newhemoglobin = np.add(newhemoglobin,h_min)
    
    return newglucose, newhemoglobin, normg, normh

#takes in the test point(numpy arrays) and glucose, hemoglobing numpy arrays
#calculates the distance between the test case and every point in the 
#gluc and numpy arrays
#returns a distance numpy array that holds all those distances
def calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin):
    Distance = np.zeros(len(glucose))
    for i in range(len(Distance)):
        d1 = (newglucose[0] - glucose[i])**2
        d2 = (newhemoglobin[0] - hemoglobin[i])**2
        Distance[i] = np.add(d1,d2)
    Distance = np.sqrt(Distance)
    return Distance

#parameters: glucose, hemoglobin, classification numpy arrays as well as the test cases in numpy arrays
#Calls upon calculate distance function and stores that in a distance numpy array
#Use np.argmin(distance) to find the minimum index
#Get the classification of that minimum distance
#Return that classification
def nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    Distance = calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
    MinIndex = np.argmin(Distance)
    TheClassification = classification[MinIndex]
    return TheClassification

#takes in test point, gluc, hemo, classification numpy arrays and the class for the test point
#graphs all of that data on a graph
#returns nothing.
def graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification, newclass):
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    if(newclass == 1): 
        plt.scatter(newhemoglobin,newglucose,c = "black", s = 100)
    else:
        plt.scatter(newhemoglobin,newglucose, c= "red", s = 100)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.title("Glucose vs. Hemoglobin with Test Point")
    plt.legend()
    plt.show()

#parameters: k points to observe, test case hemoglobin and glucose, and numpy arrays of 
#glucose and hemoglobin and classification
#Calls upon distance function created earlier for test case and real cases and stores 
#that in a numpy array
#Sorts the distance function using np.argsort
#Grabs the k classifications from that. This new variable is a numpy array that 
#stores the k nearest point’s classifications.
#From there, the average classification of array is found and if the average is above 
#.5 it is treated as 1 and below is 0. This value is then returned.
def kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classification):
    Distance = calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
    sorted_indices = np.argsort(Distance)
    #print("sorted ind", sorted_indices)
    k_indices = sorted_indices[:k]
    #print("hemos: ", hemoglobin[k_indices], " \nglucos: ", glucose[k_indices])
    k_classifications = classification[k_indices]
    print(k_classifications)
    #print(k_classifications.size)
    sum = 0
    for i in range(k):
        sum +=k_classifications[i]
    sum = sum/k
    print("Average classification is: ", sum)
    if(sum > .5):
        return 1
    else:
        return 0

            


# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()

plt.figure()
plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
plt.xlabel("Hemoglobin")
plt.ylabel("Glucose")
plt.legend()
plt.show()
#original script is above new script is below this comment


newg, newh, normnewg, normnewh = createTestCase(glucose,hemoglobin)
print(newg,newh, normnewg, normnewh)

gnorm,hnorm,cnorm = normalizeData(glucose,hemoglobin,classification)

ClassForNewPoint = nearestNeighborClassifier(normnewg,normnewh,gnorm,hnorm,cnorm)
print(ClassForNewPoint)

graphTestCase(normnewg,normnewh,gnorm,hnorm,cnorm,ClassForNewPoint)

#graphData(gnorm,hnorm,cnorm)
k = int(input("How many nearest points should be taken into consideration?: "))
k_classes = kNearestNeighborClassifier(k, normnewg, normnewh, glucose, hemoglobin, classification)
graphTestCase(normnewg,normnewh,gnorm,hnorm,cnorm,k_classes)

