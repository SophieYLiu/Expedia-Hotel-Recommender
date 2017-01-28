"""
reformats date and time
"""
import time

#converts date string to [year, month, day, hour, minute, second]
def timestamptolist(T):
    tstruct = time.strptime(T, "%Y-%m-%d %H:%M:%S")
    tlist = [ tstruct[0], tstruct[1], tstruct[2], tstruct[3], tstruct[4], tstruct[5] ]
    return tlist

def datestamptolist(T):
    tstruct = time.strptime(T, "%Y-%m-%d")
    tlist = [ tstruct[0], tstruct[1], tstruct[2] ]
    return tlist

#open the files for input and output
smaller = open("reformatedtraiin.csv", 'w')
original = open("smallTrain.csv")

#copy headers
originalheaders = original.readline().split(",")
tslist = ['TSyear', 'TSmonth', 'TSday', 'TShour', 'TSminute', 'TSsecond' ]
cilist = ['CIyear', 'CImonth', 'CIday' ]
colist = ['COyear', 'COmonth', 'COday' ]
cicolist = cilist+colist
originalheaders = tslist + originalheaders[1:11] + cilist + colist + originalheaders[13:]
commas = [ x+"," for x in originalheaders ]
commas[-1] = commas[-1][:-1]+"\n" #take off comma, put on new line
htext = ""
for x in commas:
    htext += x
print("htext:" + htext)
smaller.write(htext)

#copy data and reformat
for line in original:
    L = line.split(",")
    if L[0] == '' or L[11] == '' or L[12] =='':
        continue
    TS = timestamptolist(L[0])
    CI = datestamptolist(L[11])
    CO = datestamptolist(L[12])
    reformated = TS + L[1:11] + CI + CO + L[13:]
    withcommas = [ str(x)+"," for x in reformated ]
    withcommas[-1] = withcommas[-1][:-1]
    ltext = ""
    for x in withcommas:
        ltext += x
    smaller.write(ltext)
    print(ltext)

smaller.close()
original.close()

