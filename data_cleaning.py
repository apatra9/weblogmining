import csv

file=open("log/data.csv","r")

co=0
count=0
heading='ip address,'+'time stamp,'+'method1,'+'url,'+'http1,'+'http2,'+'browser'+'\n'
output=open("DCoutput.csv","wb")
output.write(heading)

#Data Cleaning
k=0
for x in file:
    (a)=x.split(",")
    if len(a)>5:
        if a[4]=="200":
            if (not(a[3].endswith(".jpg") or a[3].endswith(".ico") or a[3].endswith(".gif") or a[3].endswith(".css"))):
                output.write(x)
                count += 1


print count
