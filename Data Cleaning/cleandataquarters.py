import pandas as pd
from datetime import datetime as dt
import time

def print_time():
    print(dt.now().isoformat())

input_file = "cleanSmallTrain_2014.csv"
print_time()
print("reading csv...")
data = open(input_file)

output_q1 = open("cleanSmallTrain_2014_q1.csv", 'w')
output_q2 = open("cleanSmallTrain_2014_q2.csv", 'w')
output_q3 = open("cleanSmallTrain_2014_q3.csv", 'w')
output_q4 = open("cleanSmallTrain_2014_q4.csv", 'w')

headers = data.readline()

#print headers
output_q1.write(headers)
output_q2.write(headers)
output_q3.write(headers)
output_q4.write(headers)

print_time()
print("saving files...")
for line in data:
    line_list = line.strip().split(",")

    #pull out month info
    month = time.strptime(line_list[0], "%Y-%m-%d %H:%M:%S").tm_mon
     
    if (month in {1,2,3} ):
        output_q1.write(line)
    if (month in {4,5,6} ):
        output_q2.write(line)
    if (month in {7,8,9} ):
        output_q3.write(line)
    if (month in {10,11,12} ):
        output_q4.write(line)
