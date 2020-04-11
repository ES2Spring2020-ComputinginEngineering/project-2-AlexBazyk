#Please place your FUNCTION code for step 4 here.
import KMeansClustering_functions as kmc #Use kmc to call your functions


glucose, hemoglobin, classification = kmc.openckdfile()
k = int(input("What is the number of classifications?"))

glucose, hemoglobin, classification = kmc.normalizeData(glucose,hemoglobin,classification)

centroids = kmc.createcentroids(k)
blessrng = kmc.findDtoCentroid(glucose,hemoglobin,centroids)