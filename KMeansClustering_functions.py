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
    print(total)
    return total

def findDtoCentroid(glucose,hemoglobin,centroids):
    Distance = np.zeros((len(centroids),len(glucose)))
    for i in range(len(centroids)):
        for j in range(len(glucose)):
            dgluc = (centroids[i,0] - glucose[j])**2
            dhemo = (centroids[i,1] - hemoglobin[j])**2
            Distance[i,j] = np.add(dgluc,dhemo)
    Distance = np.sqrt(Distance)
    print(Distance)
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
            

