#return a tuple list of top n neighbors with their distance metrics
def simiuser(dict,person,n,distance_method):
    t=[]
    for id in dict:
        if(id!=person):
            value=float(method(dict,person,id))
            t.append((id,value))   
            
    t.sort(key=lambda tup:tup[1],reverse=True)  
    top=t[:n]
    print top
    
##return n most similar users to person from a group    
def simiuser(dict,person,group,n,distance_method):
    t=[]
    for id in group:
        if(id!=person):
            value=float(method(dict,person,id))
            t.append((id,value))   
            
    t.sort(key=lambda tup:tup[1],reverse=True)  
    top=t[:n]
    import operator
    top=map(operator.itemgetter(0), top)
    return top

#get neighbors based on a threshold value of a distance metric
def neighbor(dict,person,threshold,distance_method):
    t=[]
    for id in dict:
        if(id!=person):
            value=float(method(dict,person,id))
            t.append((id,value))   
            
    t.sort(key=lambda tup:tup[1],reverse=True)
    t2=[i for i in t if i[1]>threshold]
    return t2

#return a dictionary of neighbors for all keys(user/item) in the preference dict
def similaritydict(dict,threshold):
    result={}
    for i in dict:
        result[i]=neighbor(dict,i,threshold,pearson)
    return result

#dictionary = similaritydict(rate,0.6)