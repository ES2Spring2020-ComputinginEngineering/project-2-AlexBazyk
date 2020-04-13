This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org).

Alex Bazyk

Files and How to Run:
NearestNeighBorClassification.py
	Part 2 and Part 3 code
	Running:
	Running will print out: a graph without the point, the randomly generated point's
	glucose, and hemo, the normalized version of that, and the points classification
	it then prints out a graph with the point in it.
	The user is then prompted to see how many points should be looked at for k nearest points
	The console then prints out the classification for each of the k closest points
	followed by the classification for the new point. it then prints all the points 
	with the new points classification based on the k points nearest to it.

KMeansClusteringdriver.py
	contains part 4 code.
	How to Run:
	enter how many clusters
	it prints out the starting centroids (glucose,hemoglobin)
	it prints out then the ending centroids
	it graphs all of that.
	to get the false positives and the like, unocmment the code at the end that is 
	marked as "--------------------" (lines 30-51)
	this will print out the extra data neeeded.
	
	
	
	
	

KmeansClusteringFunctions.py
	Holds all the functions for kmeansclusteringdriver.py
	openckdfile
		#takes no parameters
		#opens file and grabs the data
		#returns numpy arrays of glucose, hemoglobin, and classification

	createcentroids (k)
		#takes a parameter k which is the amount of centroids to create
		#returns the randomly generated k centroids in a numpy array (k by 2)
	
	finddtocentroid	
		#takes in gluc, hemo, and centroids numpy arrays
		#finds the distance from each point to all the centroids
		#returns this numpy array which is k by length of data long

	normalizedata
		#normalizes the data given in gluc, hemo,class numpy arrays
		#uses normalization algorithim
		#returns the gluc, hemo,class numpy arrays

	update centroid
		#parameters: distance, centroid, gluc, hemo numpy arrays
		#updates the centroid position based on the average distance between
		#all the points closest to it.
		#returns the updated centroid and a numpy array that holds all the data
		#about which data is closest to each centroid
	graphingkmeans
		#params: glucose, hemo, assignment, centroids
		#graphs the data stored in glucose, hemoglobin, assignment, and centroids 
		#numpy arrays
		#returns nothing but prints out the graph
ckd
	Holds all the glucose, hemoglobin, classification data.