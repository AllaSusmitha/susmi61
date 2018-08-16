n=int(input())
s=0
while(int(n)>=1):
	d=int(n)%10
	s=s+(d**2)
	n=int(n)//10
	if(n==0):
		print(s)
