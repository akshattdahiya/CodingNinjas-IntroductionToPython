def printTable(start,end,step):
	for i in range(s,e+1,step):
		celsius=int((5/9)*(i-32))
		print(i , celsius , sep="\t")
	return celsius
	pass
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)
