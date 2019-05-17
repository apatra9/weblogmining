def spil(x):
    x = x.split('/')[-1]
    x = x.split('?')[0]

    try:
        x = x.split('.')[1]
    except:
        pass
    x = x.split(" ")[0]
    x = x.split("-")[0]
    x = x.split(":")[0]

    x = x.split('docs')[0]

    return x


def check(a,b):
    a=a.split('.')
    b=b.split('.')
    count=0
    if len(a) != len(b):
        return 0
    for i in range(len(a)):
        if a[i]==b[i]:
            count+=1
    return count

f=open('DCoutput.csv','r')
lis=f.readlines()
f.close()

f=open('unique.txt','r')
topic=f.readlines()
f.close()

ip=[]
for x in range(1,len(lis)):
    ip.append(lis[x].split(',')[0])
unique=list(set(ip))

test={}
new_ip=raw_input("Enter ip: ")
if new_ip in unique:
    for x in range(1,len(lis)) :
     temp=lis[x].split(',')
     if new_ip == temp[0]:
        try:
            test[spil(temp[3])]+=1
        except:
            test[spil(temp[3])]=1

else:
    for x in range(1, len(lis)):
        temp = lis[x].split(',')
        count=check(new_ip,temp[0])
        if count !=0 :
            try:
                test[spil(temp[3])]+=count
            except:
                test[spil(temp[3])]=count


max=0
label=''
if len(test)==0:
    print "Nothing to show"
    exit()
for i in test:
    if max<test[i]:
        max=test[i]
        label=i
print i,max
f=open('predict/'+i+".txt",'r')
test=f.readlines()
f.close()
print "Possible Visiting Websites"
for i in test:
    print i.split("\n")[0]
