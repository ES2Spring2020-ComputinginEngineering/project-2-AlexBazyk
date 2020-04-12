#Please place your FUNCTION code for step 4 here.
import KMeansClustering_functions as kmc #Use kmc to call your functions


glucose, hemoglobin, classification = kmc.openckdfile()
k = int(input("What is the number of classifications? "))

glucose, hemoglobin, classification = kmc.normalizeData(glucose,hemoglobin,classification)

centroids = kmc.createcentroids(k)
print("Starting centriod: \n", centroids)

DistancesFromEachCentroid = kmc.findDtoCentroid(glucose,hemoglobin,centroids)
#print(DistancesFromEachCentroid)

for i in range(15000):
    centroids, ClosestClass = kmc.updatecentroid(DistancesFromEachCentroid,centroids,glucose,hemoglobin)

print("Ending centriod: \n", centroids)


#check for any differences
#make sure do false pos and neg tmrw! :)
numDiff = 0
for i in range(len(ClosestClass)):
    if(int(classification[i]) != int(ClosestClass[i])):
        numDiff +=1
#        print(i,classification[i],ClosestClass[i])
#        print("Difference was found! At Location: ", i)
print(numDiff)      
    