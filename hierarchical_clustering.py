from math import sqrt
#Hierarchical clustering continuously merge two most similar groups.

#First we define a group/node, left and right are two subnode
class node:
	def __init__(self, data, left=None, right=None, distance=0.0, id=None): 
		self.left = left
		self.right = right
		self.data = data 
		self.id = id
		self.distance = distance

# Pre-processing file
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

#Define a distance for two nodes
def f(node1, node2):
	pass
	
#Recursively merge two nodes until there's only one node left, data is a list of rows.
def merge(rows, distance=f):
	#find the smallest distance between two rows in the data
	clust = [node(rows[i], id=i) for i in range(len(rows))]
	current_id=-1
	previous ={}
	min_d = 99999999999
	min_pair = (0,0)
	while len(clus) > 1:
		for node1 in clust:
			for node2 in clust:
				if node1 == node2:
					continue
				else:
					d =distance(node1,node2)
				if d <= min_d:
					min_d = d
					min_pair = (node1.id, node2.id)
		merge_data = [(clust[node1.id][data][i]+clust[node2.id][data][i])/2 for i in\
		len(rows[0])]
		new_node = node(merge_data, id=current_id, left=clust[min_pair[0]], \
		right=clustmin_pair[0], distance = min_d)
		current_id-=1
		del clust[min_pair[0]]
		del clust[min_pair[1]]
		clust.append(new_node)
	return clust[0]



#Display the hierarchy 
def display(root, n=0):
	for i in range(n):
		print ' '
	if root.id < 0:
		print '-'
	else:
		print clust.id
	if root.left!=None:display(root.left)
	if root.right!=None:display(root.right)
		
	