# K-mean clustering
from math import sqrt

#Pre-processing of data.
def prepro(filename):
	lines = [line for line in file(filename)]
	attributes = lines[0].strip().split('\t')[1:]
	rownames = []
	rows = []
	for line in lines[1:]:
		data = lines[0].strip().split('\t')
		rownames.append(data[0])
		rows.append([float(x) for x in data])
	return attributes, rownames, rows
	
#Randomly pick k points
def initial(rows, k):
	n = len(rows)
	m = len(rows[0])
	data_range = []
	random_k = []
	data_range = [(min(row[i][j] for j in range(n)),max(row[i][j] for j\
	 in range(n))) for i in range(m)]
				
	for i in range(k):
		random_k.append([data_range[i][0]+random().data_range[i][1]] \
		for i in range(n))
	return random_k
	
#Recursively update until the data doesn't change at some iteration.
#First element of every row is the category it belongs to
def k_mean(rows, k, distance=f)
	random_k = initial(rows, k)
	last_label = []
	while True:
		#For every row determine its category
		for i in range(len(rows)):
			for j in range(k):
				d = distance(random[j],rows[i])
				if d < min_d:
					min_d = d
					rows[0] = j
	
		#Clear the label
		for i in range(len(random_k)):
			for j in range(len(random_k[0])):
				random_k[i][j] = 0				
		#Update the k label
		count = [0 for i in range(k)]
		for j in range(n):
			for i in range(k):
				if rows[j][0] != i: continue
				else:
					count[i] += 1
					for p in range(len(row[0])):
						rank_k[i][p] += rows[j][p]
		for i in range(k):
			for j in range(len(random_k[0])):
				random_k[i][j] /= count[i]		
	
		#If the label has not changed, then we are done
		if last_label == random_k:
			break			
		#Store the label
		last_label = random_k	 
	return rows
									 
					 
					 
					 
					 
					 
					 
					 
					 
					 
					 
					 
					 
					 
		
	