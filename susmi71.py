m,n=map(int,input().split())
c=1
if(m>n):
	if((m%n)==0):
		print(m)
	else:
		while(c>=1):
			q=m*c
			if((int(q)%n)==0):
				print(q)
				break
			else:
				c+=1
elif(m<n):
	if((n%m)==0):
		print(n)
	else:
		while(c>=1):
			q=n*c
			if((int(q)%m)==0):
				print(q)
				break
			else:
				c+=1
else:
	print(m)
