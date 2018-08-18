n=int(input())
l=[int(x) for x in raw_input().split()]
sum=0
for i in range(0,n):
	sum=sum+l[i]
	x=sum/n
print x
