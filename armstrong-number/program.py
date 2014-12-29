def isArmstrong(num):
	temp = num
	sum = 0
	digit = 0

	while(temp != 0):
		digit = temp % 10
		sum = sum + ( digit * digit * digit )
		temp = int(temp / 10)
	

	if(num == sum):
		return True;  #Success

	return False; #Failure
 
if __name__=="__main__":
	print("Enter number: ", end="")
	n = int(input())
	if (isArmstrong(n)):
		print("\n",n," is an armstrong number");
	else:
		print("\n",n," is not an armstrong number");
