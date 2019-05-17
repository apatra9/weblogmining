import matplotlib.pyplot as plt

f=open('ssid.csv','r')
test=f.readlines()
f.close()
sid=raw_input("enter the ssid")
inp={}
for i in range(1,len(test)):
    temp=test[i].split(",")
    if sid==temp[-1].split('\n')[0]:
        if temp[0] in inp :
            inp[temp[0]]+=1
        else:
            inp[temp[0]]=1

activities=[]
slices=[]

for i in inp:
    activities.append(i)
    slices.append(inp[i])

plt.pie(slices, labels = activities,
        startangle=90, shadow = True,
        radius = 1.2, autopct = '%1.1f%%')

plt.title("No. of session ")
plt.legend()
plt.show()