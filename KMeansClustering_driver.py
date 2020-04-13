#Please place your FUNCTION code for step 4 here.
import KMeansClustering_functions as kmc #Use kmc to call your functions


glucose, hemoglobin, classification = kmc.openckdfile()
k = int(input("What is the number of classifications? "))
glucose, hemoglobin, classification = kmc.normalizeData(glucose,hemoglobin,classification)
centroids = kmc.createcentroids(k)
print("Starting centriod: \n", centroids)
DistancesFromEachCentroid = kmc.findDtoCentroid(glucose,hemoglobin,centroids)
#print(DistancesFromEachCentroid)


#runs the algorithim 1000 times (or any number of times) and moves
#the centroid each time.
for i in range(1000):
    DistancesFromEachCentroid = kmc.findDtoCentroid(glucose,hemoglobin,centroids)
    centroids, ClosestClass = kmc.updatecentroid(DistancesFromEachCentroid,centroids,glucose,hemoglobin)
    #print(centroids)
    #kmc.graphingKMeans(glucose, hemoglobin, ClosestClass, centroids)

#print(ClosestClass)
print("Ending centriod: \n", centroids)


#check for any differences
#this section only works for 2 clusters
#below this can be uncommented to print out the percentages of 2 clusters.----
#--------------------------------------------------------------------------
#pos = 0
#neg = 0
#falsepos = 0
#falseneg = 0
#totalcases = len(classification)
#for i in range(len(ClosestClass)):
#    if(ClosestClass[i] != classification[i]):
#        if(ClosestClass[i] == 1):
#            falseneg+=1
#        else:
#            falsepos+=1
#if(falseneg!=0):
#    print("Number incorrectly labeled as being in class 1: ", falseneg)
#    print("Percentage out of total patients: ", falseneg/totalcases*100, "%")
#else:
#    print("No Incorrectly labeled class 1 cases")
#if(falsepos!=0):
#    print("Number incorrectly labeled as being in class 0: ", falsepos)
#    print("Percentage out of total patients: ", falsepos/totalcases*100,"%")
#else:
#    print("No Incorrectly labeled class 1 cases")
#    

kmc.graphingKMeans(glucose, hemoglobin, ClosestClass, centroids)

    