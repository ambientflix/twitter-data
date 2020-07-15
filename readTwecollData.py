import re

f = open("Allen_Lin_.dat")

following = list()
infoList = list()

for x in f:
    info = x.split(",")

    # A parsing system I came up with to try to parse the names better... it works for some names and deletes others...
    '''splitS = re.findall('[A-Z][^A-Z]*', info[1])
    parseName = ""
    for word in splitS:
        parseName = parseName + word + " "
    '''

    # Appending their twitter ID, twitter name, and twitter location into a list
    infoList.append([[str(info[0]).rstrip()+"\n"], [info[1].rstrip()+"\n"], [info[10].rstrip()+"\n"]])

followerData = open("followerData.txt", "w")
for row in infoList:
    for val in row:
        followerData.writelines(val)
