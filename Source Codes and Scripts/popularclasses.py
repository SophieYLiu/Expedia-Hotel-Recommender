TrainingData = open("train.csv")
TrainingData.readline()

from collections import Counter

class_count = Counter()

for line in TrainingData:
    Line_list = line.strip().split(",")
    hotel_class = Line_list[-1]
    class_count[hotel_class] += 1

print(class_count)

hotel_counts = [ (k,v) for k,v in class_count.items() ]
sorted_hotels = sorted(hotel_counts, key = lambda x: x[1] )

print(sorted_hotels)

top_5 = sorted_hotels[-5:-1:-1]

for each in top_5:
    print(each)


