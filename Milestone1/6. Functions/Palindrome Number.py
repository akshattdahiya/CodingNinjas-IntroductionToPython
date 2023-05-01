def checkPalindrome(num):
    return num==num[::-1]
num = input()
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
