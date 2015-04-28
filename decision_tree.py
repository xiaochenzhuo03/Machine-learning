#Decision tree

#The last coloum of every row represent the category of the row 

#Build node class
#column: the colum this node used to split the data
#threshod: the threshold this node used to split the data
class node:
	def __init__(self, column, threshold, left=None, right=None):
		self.column = column
		self.threshold = threshold
		self.left = left
		self.right = right

#Use a node to split the data
def split(rows, node):
	column = node.column
	threshold = node.threshold
	#We need to define a split function depends of the type of the data
	if isinstance(value, int) or isinstance(value, float):
		split_function = lambda row: row[column]>threshold
	else:
		split_function = lambda row: row[column] == threshold
	left = [row for row in rows if split_function(row)]
	right = [row for row in rows if not split_function(row)]
	return left, right
 		
#Function to give a score for some split (Gini impurity or Entropy)
def score(true_row, false_row):
	s = 0
	return s 


#Find the best threshold to split the data
def thre(rows, column):
	d = {}
	n = len(rows)
	for i in range(n):
		if rows[i][column] not in d:
			d[rows[i][column]] = 1
	min_s = 999999
	threshold = 0
	for t in d:
		root = node(column, threshod)
		left,right = split(rows, node)
		s = score(left, right)
		if s < min_s:
			min_s = s
			threshod = t
	return threshold


#Recursively build the tree
def build_tree(rows):
	#Number of column:
	n = len(rows[0]-1)
	#Min score
	min_score = 99999
	#For every column:
	for i in range(n):
		#Find the best threshold to split the data using that column
		threshold = thre(rows, i)
		#Build a node
		temp_root = node(i, threshold)
		#Calculate the score of that split
		left,right = split(rows, temp_root)
		s = score(left, right)
		#Compare it the the min_score
		if s < min_score:
			min_score = s
			best_column = i	
	#Build the root with the column and threshold with the highest score
	root = node(best_column, min_score)
	#Split the rows with the score to row_l and row_r
	row_l, row_r = split(rows, root)
	#Recursively build node using row_l and row_r
	left_node = build_tree(row_l)
	right_node = build_tree(row_r)
	#return the root node
	root.left = left_node
	root.right = right_node
	return root 
