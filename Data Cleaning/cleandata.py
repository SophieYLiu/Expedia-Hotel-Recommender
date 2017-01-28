import pandas as pd
from datetime import datetime as dt
import time

def print_time():
    print(dt.now())

input_file = "train.csv"
print_time()
print("reading csv...")
data = pd.read_csv(input_file, header=0)
data = data.dropna()
features_to_keep = ['date_time','site_name', 'user_id', 'is_mobile', 'srch_ci', 'srch_co', 'srch_adults_cnt', 'srch_children_cnt', 'is_booking', 'srch_destination_type_id', 'hotel_cluster' ]
train2 = data.loc[:,features_to_keep]
#next line doesnt work to exclude non-bookings
#train3 = train2[train2.loc[:'is_booking'] > 0:,:]

print_time()
print("number of rows in initial file")
print(train2.size)

train4 = train2[train2['is_booking']==1]
print_time()
print("number of rows after filtering by booking")
print(train4.size)
train4 = train4.dropna()
new_features = features_to_keep[0:4] + ["duration"] + features_to_keep[6:]
output_2014 = open("cleanSmallTrain_2014.csv", 'w')
output_2013 = open("cleanSmallTrain_2013.csv", 'w')

#print headers
sep = ","
output_2014.write(sep.join(new_features)+"\n")
output_2013.write(sep.join(new_features)+"\n")
print_time()
print("saving files...")
for e in train4.iterrows():
    ind, dat = e
    data_list = dat.tolist()
    #pull out check in and check out times
    co_time = time.mktime(time.strptime(data_list[4], "%Y-%m-%d"))
    ci_time = time.mktime(time.strptime(data_list[5], "%Y-%m-%d"))
    #get duration of stay
    D = dt.fromtimestamp(ci_time) - dt.fromtimestamp(co_time)
    duration = D.days

    #pull out year info
    year = time.strptime(data_list[0], "%Y-%m-%d %H:%M:%S").tm_year
    
    processed = data_list[0:4] + [duration] + data_list[6:]
    #print(processed)
    out_string = sep.join([str(x) for x in processed])+"\n" 
    if (year == 2014):
        output_2014.write(out_string)
    if (year == 2013):
        output_2013.write(out_string)
