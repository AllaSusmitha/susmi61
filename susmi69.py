n=int(input())
n1=1
n2=1
c=0
while c < n:
	print n1,
	nth = n1 + n2
	n1 = n2
	n2 = nth
	c = c+1
