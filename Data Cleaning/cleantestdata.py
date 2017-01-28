import pandas as pd
from datetime import datetime as dt
import time

input_file = "test.csv"
data = pd.read_csv(input_file, header=0)
data = data.dropna()
features_to_keep = ['site_name', 'user_id', 'is_mobile', 'srch_ci', 'srch_co', 'srch_adults_cnt', 'srch_children_cnt', 'is_booking', 'srch_destination_type_id', 'hotel_cluster' ]
train2 = data.loc[:,features_to_keep]
#next line doesnt work to exclude non-bookings
#train3 = train2[train2.loc[:'is_booking'] > 0:,:]
print(train2.size)

train4 = train2[train2['is_booking']==1]
print(train4.size)

new_features = features_to_keep[0:3] + ["duration"] + features_to_keep[5:]
output = open("cleanSmallTrain.csv", 'w')
for feature in enumerate(new_features):
    output.write(str(feature[1]))
    if feature[0] < len(new_features) - 1:
        output.write(",")
    else:
        output.write("\n")
for e in train4.iterrows():
    ind, dat = e
    #print(dat.tolist()) 
    data_list = dat.tolist()
    co_time = time.mktime(time.strptime(data_list[3], "%Y-%m-%d"))
    ci_time = time.mktime(time.strptime(data_list[4], "%Y-%m-%d"))
    D = dt.fromtimestamp(ci_time) - dt.fromtimestamp(co_time)
    duration = D.days
    processed = data_list[0:3] + [duration] + data_list[5:]
    #print(processed)
    out_string = ""
    for s in processed:
        out_string += str(s) + ","
    out_string = out_string[0:-1] + "\n" #take off last comma
    output.write(out_string)

#train4.to_csv(path_or_buff=output, header = features_to_keep, index=False)
