x,y=map(int,raw_input().split())
for i in range(x,y):
	l=len(str(i))
	sum=0
	temp=i
	while(i>0):
		z=i%10
		sum=sum+(z**l)
		i=i/10
	if(sum==temp):
		print temp,
	
