def spe(s):
	c=0
	for i in range (0,len(s)):
		a=s[i]
		if ((a>='a' and a<='z')or (a>='A'and a<='Z')):
			pass
		elif (a>='0'and a<='9') or (a=='_'):
		
				pass
		else:
			c=c+1
	return c
s=raw_input()
print spe(s)
