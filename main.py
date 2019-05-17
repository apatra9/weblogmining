file=open("log/data.csv","r")
data=[]
co=0
count=0

#Data Cleaning

for x in file:
    (a)=x.split(",")
    if len(a)>5:
        if a[4]=="200":
            if (not(a[3].endswith(".jpg") or a[3].endswith(".ico") or a[3].endswith(".gif") or a[3].endswith(".css"))):
                data.append(a)
                count += 1
print count

#User Identification

userips=[]
usercount=0
count=0

for i in range(10):
    print data[i]

"""for x in data:
    if  x[0] not in userips:
        userips.append(x[0])
        usercount+=1
    count+=1
    print count

print usercount
"""
#session Identification
