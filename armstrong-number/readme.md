Armstrong Number
===============

An Armstrong number is a number such that the sum of its digits raised to the third power is equal to the number itself.  
For example, 371 is an Armstrong number, since 3^3 + 7^3 + 1^3 = 371.  
Another example, 153. 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.

###CODE
```python
def isArmstrong(num):
	temp = num
	sum = 0
	digit = 0

	while(temp != 0):
		digit = temp % 10
		sum = sum + ( digit * digit * digit )
		temp = int(temp / 10)

	if(num == sum):
		return True; #Success

	return False; #Failure
```

With love,  
_Shivaji Varma_
