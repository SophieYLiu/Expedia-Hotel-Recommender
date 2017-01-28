#load in large data by batches
#sd<-read.csv("~/train.csv", header = TRUE, nrows = 1)
#classes<-sapply(sd, class)
#library("ff")
#train<-read.csv.ffdf(file="~/train.csv", header=TRUE, VERBOSE=TRUE, first.rows=2000000, 
#                     next.rows=2500000, colClasses=classes)
#require(ffbase)
#data1<-subset(train, is_booking==1)
#mydata<-subset(data1,!is.na(orig_destination_distance))

#The recent attempt just import preprocessed data train_2014_q4
train<-read.csv("train_2014_q4.csv")
#call multinom for learning
require(nnet)
mymodel<-multinom(hotel_cluster~is_package+is_mobile+user_id+duration+srch_children_cnt
                  +srch_destination_type_id, data = train, family=binomial, maxit=200)
#import test data
train<-read.csv("test.csv")
#test data too large, need split 2 times to test
p1<-predict(mymodel, test_b[1:1000000,])
p2<-predict(mymodel, test_b[1000001:2528243,])
tid1<-test_b[1:1000000,,]$id
tid2<-test_b[1000001:2528243,]$id
x1<-data.frame(tid1, p1)
tid1<-tid2
p1<p2
x2<-data.frame(tid1, p1)
#combine into final test results as reqired format
x<-cbind(x1, x2)
colnames(x)<-c("id", "hotel_cluster")
write.csv(x=x, file="submission.csv", row.names=F)
