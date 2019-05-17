f=open('DCoutput.csv','r')
lis=f.readlines()
f.close()
test=[]
for x in range(1,len(lis)):
    test.append(lis[x].split(',')[3])
temp=[]
for i in test:
    x=i.split('/')[-1]
    if x=='':
        temp.append('no Topic')
        continue
    x=x.split('?')[0]
    try:
        x=x.split('.')[1]
    except:
        pass
    x=x.split(" ")[0]
    x=x.split("-")[0]
    x=x.split(":")[0]
    x=x.split('docs')[0]
    if x.isalpha():
        temp.append(x)
temp=list(set(temp))

f=open('topic.txt','wb')
for x in temp:
    f.write(x+'\n')
f.close()
