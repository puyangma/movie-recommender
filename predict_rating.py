# predict user rating of movies he/she has not rated yet and include the predicted value in the dictionary
# depend on dictionaries "movies" and "mvrate"

def mean(dict,key):
    import numpy 
    val = []
    for each in dict[key].itervalues():
        val.append(each)     
    return numpy.mean(val)
    
def std(dict,key):
    import numpy
    val = []
    for each in dict[key].itervalues():
        val.append(each)   
    return numpy.std(val)
   
def zscore(dict,movie,user):
    return (dict[user][movie]-mean(dict,user))/std(dict,user)

#prediction with zscore normalization
def predict(dict,user,method):
#mv is the movie name
    num=0
    denom=0
    for mv in movies.itervalues():
        if mv not in dict[user]:
        #a list of users who have rated the mv
            u=mvrate[mv].keys()
            for i in u:
                num=num+(zscore(dict,mv,i)*method(dict,user,i))
                denom=denom+pearson(dict,user,i)
            dict[user][mv]=int(mean(dict,user)+std(dict,user)*(num/denom))
            
#preliminary prediction        
def pred(dict,user,method):
#mv is the movie name
    num=0
    denom=0
    for mv in movies.itervalues():
        if mv not in dict[user]:
        #a list of users who have rated the mv
            u=mvrate[mv].keys()
            if(len(u)>5):
                u=simiuser(dict,user,u,n,method)   #where n is the number of neighbors to use
            for i in u:
                num=num+(rate[i][mv]*method(dict,user,i))
                denom=denom+method(dict,user,i)
            dict[user][mv]=int(num/denom)