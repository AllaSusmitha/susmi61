h1,min1=map(int,raw_input().split())
h2,min2=map(int,raw_input().split())
m1=h1*60+min1
m2=h2*60+min2
d=abs(m1-m2)
t=d%60
t1=(d-t)/60
print t1,t
