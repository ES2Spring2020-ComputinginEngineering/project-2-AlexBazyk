#Please place your FUNCTION code for step 4 here.

import numpy as np
import matplotlib.pyplot as plt
import random


def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def createcentroids(k):
    total = np.zeros((k,2))
    for i in range(k):
        rgluc = np.random.rand(1)
        rhemo = np.random.rand(1)
        total[i,0] = rgluc
        total[i,1] = rhemo
    return total

def findDtoCentroid(glucose,hemoglobin,centroids):
    Distance = np.zeros((len(centroids),len(glucose)))
    for i in range(len(centroids)):
        for j in range(len(glucose)):
            dgluc = (centroids[i,0] - glucose[j])**2
            dhemo = (centroids[i,1] - hemoglobin[j])**2
            Distance[i,j] = np.add(dgluc,dhemo)
    Distance = np.sqrt(Distance)
    return Distance


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


#look at distance for each
#see which is smallest
#find average of all which are closes to it
#update it.


def updatecentroid(distance,centroid,glucose,hemoglobin):
    ClosestDist = np.ones((len(distance[0])))
    ClosestDist = np.add(ClosestDist,10)
    ClosestClass = np.zeros((len(distance[0])))
    for i in range(len(distance)): #i is each centroid's distance
        for j in range(len(distance[0])): # loops through each distance
            if(distance[i,j] < ClosestDist[j]):
                ClosestDist[j] = distance[i,j]
                ClosestClass[j] = i
#    print(ClosestDist)                
#    print(ClosestClass)
    
    #updates centroid
    counter = 0
    
    for k in range(len(centroid)):
        centroid[k,0] = 0
        centroid[k,1] = 0
        #print("start ", centroid[k,0])
        for l in range(len(distance[0])):
            if(ClosestClass[l] == k):
                centroid[k,0] = centroid[k,0] + glucose[l]
                centroid[k,1] = centroid[k,1] + hemoglobin[l]
                #print(centroid[k,0])
                counter +=1
        centroid[k,0] = centroid[k,0] / counter
        #print(centroid[k,0])
        centroid[k,1] = centroid[k,1] / counter
        counter = 0
    #print(centroid)
    return centroid, ClosestClass


def graphingKMeans(glucose, hemoglobin, assignment, centroids):
    plt.figure()
    for i in range(int(np.amax(assignment))+1):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[assignment==i],glucose[assignment==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(centroids[i, 1], centroids[i, 0], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()

