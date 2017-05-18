#!/usr/bin/evn python
from Datainput import mvrate, movies
from distance import pearson

def recommender(dict, user, distance_metric, n):
    #recommend items for the user in the format of (predicted rating, item_name)
    weighted_rating={}
    weights={}
    threshold=0.2
    for neib in dict:
        if(neib != user):
            dist=distance_metric(dict,user,neib)
            for mv in dict[neib]:
                if(mv not in dict[user] and dist>threshold):
                    if(mv not in weighted_rating):
                        weighted_rating.setdefault(mv,0)
                        weights.setdefault(mv,0)
                        
                    weighted_rating[mv] += dist*dict[neib][mv]
                    weights[mv] += dist
    result = [(weighted_rating[i]/weights[i],i)for i in weights]
    result.sort(key=lambda tup:tup[0],reverse=True)
    top=result[:n]
    return top