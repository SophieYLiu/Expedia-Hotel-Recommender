d = {}

def makeDict(train, d):
   for index, row in train.iterrows():
     c = row["hotel_cluster"]
     id = row["srch_destination_type_id"]
     if id in d:
       if c in d[id]:
         d[id][c]+=1
       else:
         d[id].update({c:1})
     else:
       d.update({id:{c:1}})
   return d

d = makeDict(train, d)


for i in d.keys():
    d[i]=sorted(d[i], key=d[i].get, reverse=True)[:5]

# Now we have list of each search destination type id, and the 5 most common clusters

# Submission Generation
import csv

with open("predictions.csv", "w+") as file:
    writer = csv.writer(file)
    writer.writerow(["id","hotel_cluster"])
    for index, row in test.iterrows():
        id = row["srch_destination_type_id"]
        cluster = [str(x) for x in d[id]]
        writer.writerow([index, cluster[0]+" "+cluster[1]+" "+cluster[2]+" "+cluster[3]+" "+cluster[4]])
