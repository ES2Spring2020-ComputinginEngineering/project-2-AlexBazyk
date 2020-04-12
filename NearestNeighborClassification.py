#Please put your code for Step 2 and Step 3 in this file.
# Alex Bazyk


import numpy as np
import matplotlib.pyplot as plt
import random


# FUNCTIONS
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

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

def graphData(glucose,hemoglobin,classification):
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.title("Glucose vs. Hemoglobin")
    plt.legend()
    plt.show()

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

def calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin):
    Distance = np.zeros(len(glucose))
    for i in range(len(Distance)):
        d1 = (newglucose[0] - glucose[i])**2
        d2 = (newhemoglobin[0] - hemoglobin[i])**2
        Distance[i] = np.add(d1,d2)
    Distance = np.sqrt(Distance)
    return Distance

def nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    Distance = calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
    MinIndex = np.argmin(Distance)
    TheClassification = classification[MinIndex]
    return TheClassification

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
print(type(ClassForNewPoint))

graphTestCase(normnewg,normnewh,gnorm,hnorm,cnorm,ClassForNewPoint)

#graphData(gnorm,hnorm,cnorm)
k = 9
k_classes = kNearestNeighborClassifier(k, normnewg, normnewh, glucose, hemoglobin, classification)
graphTestCase(normnewg,normnewh,gnorm,hnorm,cnorm,k_classes)

