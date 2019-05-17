import csv
import re

def get(x):
    #print x

    for i in x.split('http:'):
        if 'http/1.1' in i or 'HTTP/1.1' in i or 'http/1.0' in i or 'HTTP/1.0' in i:
            y=i
    #print y
    test=re.split('http/1.1|HTTP/1.1|http/1.0|HTTP/1.0',y)
    #print test[1]
    if 'GET' in test[0].split('/')[0]:
        temp = 'GET,'+test[0].split('GET')[1]+","+test[1]
    else:
        z=test[0].split('/')
        temp=z[0]+",/"
        for i in range(1,len(z)):
            temp=temp+z[i]
        temp=temp+','+test[1]
    return temp
def extract(x):
    data=re.split(', |- |,-|-,|"',x)
    #print data
    temp=""
    for x in data:
        if x !='-':
            temp=temp+x+" "
    data= temp.split('  ')
    temp=""
    #print data[3]
    for i in range(len(data)):
        if i==1:
            data[i]=data[i].split(' -')[0]+"] "

        temp= temp +data[i]+" "
    data=temp.split("  ")
    temp=""
    #print data[2]
    for i in range(len(data)):
        if i == len(data)-2:
            temp=temp+data[i]
            break
        if i == 2:
            # print data[i]
            data[i] = get(data[i])
        temp=temp+data[i]+','
    #print data
    #print temp
    return temp


if __name__ == '__main__':
    with open('access.txt', 'rb') as f:
        data = f.readlines()
    extract(data[1])
    f=open('data.csv','wb')
    f.write('ip address,'+'time stamp,'+'method,'+'url,'+'http,'+'browser'+'\n')
    for i in range(len(data)):
        print i
        f.write(extract(data[i]))
    f.close()









