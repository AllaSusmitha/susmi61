x,y=map(int,raw_input().split())
if x <= 100000:
	t=x
	x=y
	y=t
print x,y
