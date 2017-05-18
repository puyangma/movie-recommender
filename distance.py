import numpy
import math

#CALCULATE PEARSON CORRELATION BETWEEN TWO DATA SETS
#dict is a 2d dictionary
#person1 and person2 are user ids in the form of 'id'
def pearson(dict,person1,person2):
    c=[]
    d=[]
    x=[]
    y=[]
    for movie1 in dict[person1]:
        for movie2 in dict[person2]:
            if(movie1==movie2):
                c.append(dict[person1][movie1])
                d.append(dict[person2][movie2])
    if(len(c)!=0 and len(d)!=0):
        cmean=sum(c)/len(c)
        dmean=sum(d)/len(d)
        x=numpy.array(c)-cmean
        y=numpy.array(d)-dmean
        denom=math.sqrt(sum(numpy.array(x)**2)*sum(numpy.array(y)**2))
        num=sum(x*y)
    #if one of the variance is zero, then there is no correlation 
        if(denom==0):
            return 0
        return float(num/denom)
    return 0

#CALCULATE EUCLIDEAN DISTANCE BETWEEN TWO DATA SETS
#dict is a 2d dictionary 
#person1 and person2 are user ids in the form of 'id'
def euclid(dict,person1,person2):
    c=[]
    d=[]
    for movie1 in dict[person1]:
        for movie2 in dict[person2]:
            if(movie1==movie2):
                c.append(dict[person1][movie1])
                d.append(dict[person2][movie2])
    a=np.array(c)
    b=np.array(d)
    dist = numpy.linalg.norm(a-b)
    return dist