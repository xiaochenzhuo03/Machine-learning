from math import sqrt

#Suppose the rating of different people is in the following format
#Mike has rated movie 1 and 2. Mary has rated movie 2 and 4.
rating={
	'Mike':{'Movie_1':10,'Movie_2':9},
	'Mary':{'Movie_2':5,'Movie_4':7}
	}
	
#Then we need to define the distence between two people in a rating record.
#The way we do it is we first find a set of movies rated by both people, then calculate\
#the inverse of the euclidean between then.The people has similar rating will have larger\
#score.
def eucli_sim(rating, person1, person2):
	#Find common movies
	share = {}
	for item in rating[person1]:
		if item in rating[person2]:
			share[item] = 1
			
	if len(share) == 0: return 0
	
	#Calculate sum of euclidean distance
	sum_of_squares = sum([pow(rating[person1][item]-rating[person2][item], 2) \
	for item in share])
	
	return 1/(1+sqrt(sum_of_squares))
	
#another way to determin the similarity between two people is to use the correlation score
def cor_sim(rating, person1, person2):
	#Find common movies
	share = {}
	for item in rating[person1]:
		if item in rating[person2]:
			share[item] = 1
	n = len(share)
	if n == 0: return 0
	
	#Calculate sum,sum of square,sum of product
	sum1 = sum([rating[person1][item] for item in share])
	sum2 = sum([rating[person2][item] for item in share])
	sum1Sq = sum([pow(rating[peason1][item], 2) for item in share])
	sum2Sq = sum([pow(rating[peason2][item], 2) for item in share])
	pSum = sum(rating[peason1][item]*raing[peason2][item] for item in sharing)
	
	#Calculate the score
	a  = pSum-(sum1*sum2/n)
	den = sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
	if den == 0:return 0
	return a/den
	
#Now we can recomment a list of movies for a person based on a certain similarity function and a rating record
def recommend(rating, person1, similarity=cor_sim):
	recommendation = []
	sim = {}
	score = {}
	movies= {}
	#Find all the movie that are not rated by person1 but rated by other people
	for person in rating:
		for movie in person:
			if movie not in person1:
				movies[movie] = 1
	
	#Calculate the similarity of all other people towards person1		
	for person in rating:
		sim[person] = (similarity(rating, person, person1))

	
	#Calculate the score for all these movies score = sum(similarity*rating)
	for movie in moives:
		for person in rating:
			if moive not in person: continue
			else:
				score.setdefault(movie, 0)
				score[movie]+=sim[person]*rating[person][movie]
				
	sorted_score = sorted(score.items(), key=lambda x:x[1])	
	person = [person for person, score in sorted_score]	
	
	#Find the top five movie and recommend	
	recommendation = person[:5]
	return recommendation
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		