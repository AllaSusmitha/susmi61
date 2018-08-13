string = raw_input()
char=0
count=0
for i in string:
	char=char+1
	if (i==" "):
		count=count+1
print(char-count)
