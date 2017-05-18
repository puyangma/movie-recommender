#!/usr/bin/env python

from Dataiput import rate, movies, mvrate
from userbased_recommender import recommender
from distance import pearson

def group_recommender(group, weights, rate, movies, distance_metric):
	group_recommend = {}
	for p in group:
		p_recommend = recommender(rate,p,distance_metric)
		for score, item in p_recommend:
			if(item not in group_recommend):
				group_recommend.setdefault(item,0)
			group_recommend[item] += weights[p]*score
	ls=[(group_recommend[item],item) for item in group_recommend]
	sorted_ls = sorted(ls)
	return list(reversed(sorted_ls))

