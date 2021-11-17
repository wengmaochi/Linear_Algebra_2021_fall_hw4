import numpy as np
import json
import sys

#read the file
link = []
with open(sys.argv[1],"r") as f:
    link=json.load(f)

#initialize original transition matrix
original_transition = np.zeros((len(link),len(link)))
for i in range(len(link)):
    for o in link[i]:
        original_transition[i][o] = 1

#normalize original transition matrix, avoid devide by 0.
totallink = np.sum(original_transition,axis=0)
for i in range(len(link)):
    if(totallink[i] == 0):
        totallink = 1
original_transition = original_transition / totallink

print("Original transition matrix", original_transition)

initial_vector = np.ones(len(link))/len(link)
ordering_of_websites = np.zeros(len(link))


##########
#TODO: please implement pageran algorithm and turn ordering_of_website into a list representing the web pages. The web page with a higher probability comes first.



##########

print("Your current answer",ordering_of_websites)

#turn your answer from a numpy array to list and output it as a json file
ordering_of_websites = ordering_of_websites.tolist()
with open(sys.argv[2],"w") as f:
    json.dump(ordering_of_websites,f)