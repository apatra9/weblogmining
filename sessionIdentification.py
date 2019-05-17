from operator import itemgetter

file=open("DCoutput.csv","r")

userips=[]
timestamps=[]
sessionid=[]

userCount=0
session=0
heading='user ips,'+'Recent Timestamp,'+'Session Id'+'\n'

output=open("SIoutput.csv","wb")
output.write(heading)
co=0

def sub(prev,next):
    global session
    #print timestamps[prev],next[0]
    y = timestamps[prev].split(':')
    a = next[0].split(':')
    temp = ""
    temp2 = ""
    for i in range(len(y)):
        if i == 0:
            continue
        if i == 1:
            temp = temp + y[i]
            temp2 = temp2 + a[i]
            continue
        temp = temp + " " + y[i]
        temp2 = temp2 + " " + a[i]

    temp = temp.split(']')[0]
    temp2 = temp2.split(']')[0]
    #print temp, '\n', temp2

    temp = temp.split(' ')
    temp2 = temp2.split(' ')
    temp3 = ""

    temp3 += str(abs(int(temp[0]) - int(temp2[0])))
    #print int(temp3)
    if int(temp3)>1:
        timestamps[prev]=next[0]
        sessionid[prev]=session
        session+=1

for x in file:
    if co==0:
        #print co
        co+=1
    else:
        y=[]
        y+=x.split(',')[:1]
        if y[0] not in userips:
            userips+=y
            timestamps+=x.split(',')[1:2]
            sessionid+=[session]
            session+=1
        else:
            prev=userips.index(y[0])
            sub(prev,x.split(',')[1:2])

d=[]

for i in range(0,len(userips)):
    temp=[]
    temp.append(userips[i])
    temp.append(timestamps[i])
    temp.append(sessionid[i])
    d.append(temp)

d=sorted(d,key=itemgetter(2))

for i in range(10):
    print d[i]


for i in range(0,len(userips)):
    output.write(str(d[i][0])+','+str(d[i][1])+','+str(d[i][2])+'\n')

