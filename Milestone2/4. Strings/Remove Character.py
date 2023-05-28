from sys import stdin


def removeAllOccurrencesOfChar(string, ch) :
	newstr = ""
	for i in string:
		if i == ch:
			continue
		else:
			newstr += i
	return newstr

string = stdin.readline().strip()
ch = stdin.readline().strip()[0]

ans = removeAllOccurrencesOfChar(string, ch)

print(ans)
