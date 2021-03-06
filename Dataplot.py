#!/usr/bin/evn python
from matplotlib import pyplot as plt
import numpy as np
*************************************************
#plot a figure with two users as axis and each point is the rating by the two users on a single movie

x=[]
y=[]
mvname=[]

#movie1 and movie2 are movie names
for movie1 in rate['548']:
    for movie2 in rate['713']:
        if(movie1==movie2):
            x.append(rate['548'][movie1])
            y.append(rate['713'][movie2])
            mvname.append(movie1)
x=x[:6]
y=y[:6]
fig=plt.figure()
plt.scatter(x,y)
rg=[0,1,2,3,4,5,6]
plt.plot(rg, np.poly1d(np.polyfit(x, y, 1))(rg))
plt.axis([0,6,0,6])
plt.xlabel('user 548')
plt.ylabel('user 713')
for i,txt in enumerate(mvname[:6]):
        plt.annotate(txt,(x[i],y[i]))
plt.savefig('fig1')
*********************************************
#Plot a figure with two movies as axis and each point is the rating by a user for the two movies

a=[]
b=[]
username=[]
for user1 in mvrate[movies['340']]:
    for user2 in mvrate[movies['345']]:
        if(user1==user2):
            a.append(mvrate[movies['340']][user1])
            b.append(mvrate[movies['345']][user2])
            username.append(user1)
a=a[:10]
b=b[:10]
fig=plt.figure()
plt.scatter(a,b)
plt.axis([0,6,0,6])
plt.xlabel(movies['340'])
plt.ylabel(movies['345'])
list=username[:10]
for i,txt in enumerate(list):
        plt.annotate(txt,(a[i],b[i]))
plt.savefig('fig11')