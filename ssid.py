
def getSSId(a,b):
    #print a,b
    a=a.split(":")[1:]
    a=" ".join(a)
    a=a.split("]")[0]
    b=b.split(":")[1:]
    b=" ".join(b)
    b=b.split("]")[0]
    if b=="":
        return 1
    a=a.split(" ")
    b=b.split(" ")
    if abs(int(a[0]) - int(b[0])) >0:
        return 1
    return 0


print "Hello World"

f=open('DCoutput.csv','r')
test =f.readlines()
f.close()

print "Hello World"
ssid={}
time={}
for i in range(1,len(test)):
    temp=test[i].split(',')
    ssid[temp[0]]=0
    time[temp[0]]=""
    #print temp[0] ,ssid[temp[0]] , time[temp[0]]
#print len(ssid),len(time)

maxssid=0
label=""
total=[]
for i in range(1,len(test)):
    temp=test[i].split(',')
    tempssid = getSSId(temp[1], time[temp[0]])
    time[temp[0]] = temp[1]
    ssid[temp[0]]+=tempssid

    #print temp[0],ssid[temp[0]]
    if maxssid < ssid[temp[0]]:
        maxssid = ssid[temp[0]]
    else:
        ssid[temp[0]] = maxssid
    total.append(temp[0] + "," + temp[1] + "," + str(maxssid))
    """
    tempssid=getSSId(temp[1],time[temp[0]])
    time[temp[0]]=temp[1]
    print temp[0],tempssid,maxssid,ssid[temp[0]],time[temp[0]]
    try:
        ssid[temp[0]] = str(int(ssid[temp[0]])+ int(tempssid))
    except:
        continue
    if maxssid < ssid[temp[0]] :
        maxssid =ssid[temp[0]]
    else:
        ssid=maxssid
    total.append(temp[0]+","+temp[1]+","+str(maxssid))
    """

f=open("ssid.csv",'wb')
f.write("ip,time,ssid\n")
for i in total:
    f.write(i+"\n")
f.close()