import sys
val=int(sys.stdin.readline().strip())
temp=[]
temp2=[]

for i in range(1,val+1):
	for j in  range(1,val+1):
		temp.append(str(i)+"/"+str(j))
	temp2.append(temp)
	del temp
	temp=[]


for i in temp2:
    print(i)



count=0
i=0
j=0
while count!=val:
    print(temp2[i][j])
    if i==0:
        j+=1
        count+=1
        if j==1:
            i+=1
            j-=1
            count+=1
            print(temp2[i][j])
        
