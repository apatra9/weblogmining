import csv

file=open("DCoutput.csv","r")
data=[]
userCount=0
heading='user ips'+'\n'

output=open("UIoutput.csv","wb")
output.write(heading)

for x in file:
    (a)=x.split(",")
    data.append(a[0])

data=list(set(data))

print len(data)

for x in data:
    output.write(x+'\n')




